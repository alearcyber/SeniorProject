"""
@Author Aidan lear

This file deals with the backend stuff for purchasing tickets
"""
import json
import pickle
import Constants
import sqlite3
from Constants import Payment

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
side_orc_rows = [6,7,7,6,6,6,6,5,5,5,5,5,5,4]
main_orc_rows = [8,9,10,11,11,12,12,12,12,12,12,12,12,10,9,7]
balc_rows = [24,23,22,23,22,23]



###########################################################################
# read in the json info for seat locations of the playhouse.
# This function SHOULD NOT be used EVER without asking Aidan first.
# This reads and cleans up the data from the JSON file. I already read and cleaned
# the data. The data can be accessed by calling load_playhouse_data() below.
###########################################################################
def construct_playhouse_info():
    file = open('PlayhouseInfo.json')  # open the file
    data = json.load(file) # read the JSON text into a dictionary
    file.close() # close the file. The contents have already been read into memory.
    seats = data['seats']
    new_data = dict() # place to store the new data


    #construct the main_orch seats
    new_data['main_orch'] = []
    row = 0
    number = 0
    for seat in seats['main_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'main_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= main_orc_rows[row]:
            row += 1
            number = 0
        new_data['main_orch'].append(new_seat)


    #construct the left_orch seats
    new_data['left_orch'] = []
    row = 0
    number = 0
    for seat in seats['left_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'left_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= side_orc_rows[row]:
            row += 1
            number = 0
        new_data['left_orch'].append(new_seat)



    #construct the right_orch seats
    new_data['right_orch'] = []
    row = 0
    number = 0
    for seat in seats['right_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'right_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= side_orc_rows[row]:
            row += 1
            number = 0
        new_data['right_orch'].append(new_seat)


    #construct the balc seats
    new_data['balc'] = []
    row = 0
    number = 0
    for seat in seats['balc']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'balc'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= balc_rows[row]:
            row += 1
            number = 0
        new_data['balc'].append(new_seat)




    #construct single row seats
    section_names = ['right_box', 'right_loge', 'left_box', 'left_loge']
    for sec_name in section_names:
        # construct the foyer seats
        new_data[sec_name] = []
        number = 0
        for seat in seats[sec_name]:
            number += 1
            new_seat = dict()
            new_seat['x'] = seat['x']
            new_seat['y'] = seat['y']
            new_seat['sec'] = sec_name
            new_seat['number'] = number
            new_seat['row'] = 'A'
            new_data[sec_name].append(new_seat)
            print(new_seat)



    #write it to a file
    f = open("PlayhouseInfo.pkl", "wb")
    #pickle.dump(new_data, f)  # COMMENTED OUT INCASE SOMEONE TRIES TO USE IT.
    f.close()


###########################################################################
# This loads the playhouse seat data from the file into memory.
# The file is 'PLayhouseInfo.pkl'
###########################################################################
def load_playhouse_data():
    file = open('PlayhouseInfo.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    return data



###########################################################################
# Send general Query to the database
###########################################################################
def query(query_text):
    # establish connection with database
    connection = sqlite3.connect(Constants.DB_PATH)
    cursor = connection.cursor()

    # Execute the query and get the results
    result = cursor.execute(query_text).fetchall()

    # close the connection
    connection.close()

    # return a list of results
    return result



###########################################################################
# Is the given seat reserved already?
# returns a boolean.
# seat_ids can either be a list of seat_ids or a single seat_id
###########################################################################
def is_seat_available(seat_ids):

    #check type of seat_ids
    if isinstance(seat_ids, int): # only need to check a single seat_id

        # Establish Connection with database
        connection = sqlite3.connect(Constants.DB_PATH)
        cursor = connection.cursor()

        # construct the query, execute it, grab the result, and close the connection
        query = f"SELECT user_id FROM Seat WHERE id={seat_ids};"
        result = cursor.execute(query).fetchone()
        connection.close()

        #check to make sure that the seat id exists in the first place.
        assert len(result) > 0, f'ERROR: the seat_id, {seat_ids}, does not belong to any existing seat/ticket.'

        #user_id is the first element of result. result is a tuple.
        user_id = result[0]

        #if the user id is None, the seat is NOT reserved
        #if the user id is some number, the seat IS reserved
        if user_id is None:
            return True
        else:
            return False


    elif isinstance(seat_ids, list): #need to check through the entire list of seat_ids
        #recursivly call is_seat_reserved for all the integers
        for seat_id in seat_ids:
            if not is_seat_available(seat_id):
                return False
        return True



    else: # input is of an invalid type if the code makes it here
        assert False, 'ERROR: seat_ids should either be a list or an int. The type you put in was ' + str(type(seat_ids))




###########################################################################
# Used when the seat is already taken
###########################################################################
class SeatTaken(Exception):
    pass



###########################################################################
# Purchase Tickets
# Params:
#   seat_ids - a list of seat_ids of the seats being purchase
#   email - email of the user who is purchasing the tickets
#   performance_id - id of the performance the tickets are being purchase for.
#   payment_method - a string. How the tickets are being paid for.
#       The only acceptable values for payment method are None, 'card', 'cash'
#
###########################################################################
def purchase_tickets(seat_ids, email, performance_id, payment_method):
    # check that a valid payment_method was entered
    assert payment_method in Payment.all, "ERROR: payment method should be either " \
                                                      "None, 'card', 'check, or 'cash'. " \
                                                      "You entered " +str(payment_method)



    # Check that seats are available
    if not is_seat_available(seat_ids): # seats are not available, Throw exception
        raise SeatTaken('One of the seats you requested is taken')

    # TODO finish this
    #grab user id for the given email
    results = query(f"SELECT user_id from User WHERE email='{email}'")

    #check that the email acutaly belonged to some user
    assert len(results) > 0, f'ERROR: The email, {email}, does not belong to any users.'

    #parse out the user_id from that user.
    user_id = results[0][0]

    print(user_id)

    #assign tickets to the user








##########################################################################################
#####################################   TESTS    #########################################
##########################################################################################


############################
##Test is_seat_available(...)
############################
def test_is_seat_available():
    print('Should be True -> ', is_seat_available(1))
    print('Should be False -> ', is_seat_available(2))
    print('Should be False -> ', is_seat_available([1,2]))
    print('Should be True -> ', is_seat_available([1]))



############################
##Test purchase_tickets(...)
############################
def test_purchase_tickets():
    purchase_tickets(1, 'brenda@gmail.com', 4, 'card')


################################
# tests for this file
################################
if __name__ == "__main__":
    test_purchase_tickets()
