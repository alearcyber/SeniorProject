"""
@Author Aidan lear

This file deals with the backend stuff for purchasing tickets
"""
import json
import pickle
import Constants
import sqlite3
from Constants import Payment
from collections import defaultdict

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
side_orc_rows = [6,7,7,6,6,6,6,5,5,5,5,5,5,4]
main_orc_rows = [8,9,10,11,11,12,12,12,12,12,12,12,12,10,9,7]
balc_rows = [24,23,22,23,22,23]

# mapping month number to month string
months = ['nada', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

# create seat map
# inserting into -> seat_map[x][y] = amount
seat_map = defaultdict(lambda: defaultdict(dict))   # 3d dictionary used to know the seat number for each thing
file = open('PlayhouseRawData.json')  # open the file
data = json.load(file) # read the JSON text into a dictionary
file.close() # close the file. The contents have already been read into memory.
sections = data['seats']
for s in sections:
    seats = sections[s]
    for seat in seats:
        x = seat['x']
        y = seat['y']
        id = seat['id']
        seat_map[x][y] = id






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
def purchase_tickets(seat_ids, email, performance_id, payment_method, exchange_ids = []):
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
    for seat_id in seat_ids:
        pass




###########################################################################
# Grab seat/ticket info for the user to select.
# The returned information is used to populate the view
#   of the seating selection chart
###########################################################################
def get_seating_chart(performance_id):

    #get seating data from db
    query_one = f"SELECT " \
                f"id, row, number, x, y, price, section, user_id " \
                f"FROM Seat WHERE performance_id={performance_id}"
    results = Constants.query(query_one)


    #transform the output to JSON
    tickets = [] # tickets are stored here
    for s in results: # iterate over all the seats
        #create new seat and parse in the information
        n = dict() # new seat
        n['id'] = s[0]
        n['row'] = s[1]
        n['number'] = s[2]
        n['x'] = s[3]
        n['y'] = s[4]
        n['price'] = s[5]
        n['section'] = s[6]
        n['user'] = s[7]
        tickets.append(n)


    #build output and return
    out = json.dumps({'tickets': tickets})
    return out




###########################################################################
# Wrapper function for seating chart that delivers the data formatted
#   as expected by the frontend.
# Example data format:
#{
# performance: {
#    title: 'Phantom of the Opera', venue: 'Civic Center Playhouse', date: 'May 09, 2023', time: '7:00 PM', id: 1
#},
# tickets: [
#    {seat_id: 1, user_id: null, performance_id: 1, price: 1, id: 1},
#    {seat_id: 2, user_id: null, performance_id: 1, price: 2, id: 2},
#    ....,
#   ]
# }
###########################################################################
def seating_chart_f(performance_id):
    # grab data specific to the performance
    query_text = f"""
        SELECT
        prod.title, perf.time, prod.venue_id, perf.performance_id
            FROM
        Performance perf JOIN Production prod ON perf.production_id=prod.id
            WHERE
        perf.performance_id={performance_id}
        """
    results = Constants.query(query_text)

    #parse out performnace info
    r = results[0]
    title = r[0]
    datetime = r[1]
    venue = 'Civic Center Playhouse' if r[2] == 2 else 'Civic Center Concert Hall'
    performance_id = r[3]

    # make datetime into date and time
    tokens = datetime.split(' ')  # split on the space
    date = tokens[0]
    time = tokens[1]
    d_tokens = date.split('-')
    t_tokens = time.split(':')

    # date
    month = months[int(d_tokens[1])]
    year = d_tokens[0]
    day = d_tokens[2]

    # time
    hour = int(t_tokens[0])
    min = t_tokens[1]
    suffix = 'a.m.'
    if hour == 12:
        suffix = 'p.m.'
    elif hour > 12:
        hour = hour - 12
        suffix = 'p.m.'

    # formatting
    date = f'{month} {day}, {year}'  # example: "May 3, 2023"
    time = f'{hour}:{min} {suffix}'  # example: "6:00 p.m."

    # properly formatted performance section
    performance = {'title': title, 'date': date, 'time': time, 'venue': venue, 'performance_id': performance_id}



    #now get the seating data
    query_text = f"SELECT " \
                f"id, row, number, x, y, price, section, user_id " \
                f"FROM Seat WHERE performance_id={performance_id}"
    results = Constants.query(query_text)

    #format the 'ticket' data
    # the correct format is like so for each one:
    #{seat_id: 4, user_id: null, performance_id: 1, price: 4, id: 4},
    #They are grouped by the section they are in
    tickets = []
    seats = dict()
    for r in results:
        """
        seat_id = int(r[0])
        row = r[1]
        seat = r[2] # the number, so like seat B7 is row b seat 7
        x = r[3]
        y = r[4]
        price = r[5]
        sec = r[6]
        user_id = r[7]
        """
        row = r[1]
        seat = r[2]  # the number, so like seat B7 is row b seat 7
        sec = r[6]
        id = int(r[0])
        user_id = r[7]
        #already have performance_id in function parameters
        price = r[5]
        x = r[3]
        y = r[4]
        seat_id = seat_map[x][y]
        new_ticket = {'seat_id':seat_id, 'user_id':user_id, 'performance_id':performance_id, 'price':price, 'id': id}

        #check to see if the section exists
        if sec not in seats.keys():
            seats[sec] = []

        #add new ticket to the
        tickets.append(new_ticket)


        #SEATS HERE FOR the thing
        #Now do seats
        new_seat = {'x': x, 'y':y, 'r':'68.5', 'sec':sec, 'row':row, 'seat':seat, 'venue':venue,'id': seat_id}
        seats[sec].append(new_seat)

    #combine data into one map
    data = {'performance':performance, 'tickets': tickets, 'seats':seats}
    return data





###########################################################################
# List of upcoming performances so the user can select which
#   one to purchase a ticket for.
###########################################################################
def upcoming_performances():
    #query for upcoming shows
    query_text = """
    SELECT
    prod.title, perf.time, prod.venue_id, perf.performance_id
        FROM
    Performance perf JOIN Production prod ON perf.production_id=prod.id
        WHERE
    perf.time > datetime()
    """


    #execute and grab the results
    results = Constants.query(query_text)
    formatted_results = []
    for r in results:
        title = r[0]
        datetime = r[1]
        venue = 'Civic Center Playhouse' if r[2] == 2 else 'Civic Center Concert Hall'
        performance_id = r[3]

        #make datetime into date and time
        tokens = datetime.split(' ') # split on the space
        date = tokens[0]
        time = tokens[1]
        d_tokens = date.split('-')
        t_tokens = time.split(':')

        #date
        month = months[int(d_tokens[1])]
        year = d_tokens[0]
        day = d_tokens[2]

        #time
        hour = int(t_tokens[0])
        min = t_tokens[1]
        suffix = 'a.m.'
        if hour == 12:
            suffix = 'p.m.'
        elif hour > 12:
            hour = hour - 12
            suffix = 'p.m.'

        #formatting
        date = f'{month} {day}, {year}'  #example: "May 3, 2023"
        time = f'{hour}:{min} {suffix}'  #example: "6:00 p.m."

        #append new map
        #example name: "Hamilton", date: "May 7", time: "6:00 p.m.", venue: "Civic Center Concert Hall", performance_id: "2"
        new_result = {'name': title, 'date': date, 'time': time, 'venue':venue, 'performance_id':performance_id}
        formatted_results.append(new_result)

    #return the results in the appropriate format
    return formatted_results







##########################################################################################
#####################################   TESTS    #########################################
##########################################################################################


#test upcoming performances
def test_upcoming_performances():
    results = upcoming_performances()
    for r in results:
        print(r)




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
# test retrieving seating chart
################################
def test_seating_chart():
    id = 15
    result = get_seating_chart(id)
    print(result)

################################################################
# test retrieving seating chart WITH FORMATTING
################################################################
def test_seating_chart_f():
    id = 21
    results = seating_chart_f(id)

    tickets = results['tickets']
    seats = results['seats']

    print('==TICKETS==')
    for t in tickets:
        print(t)

    print('==SEATS==')
    for section in seats:
        print('section:', section)
        for item in seats[section]:
            print(item)


################################
# tests for this file
################################
if __name__ == "__main__":
    test_seating_chart_f()

