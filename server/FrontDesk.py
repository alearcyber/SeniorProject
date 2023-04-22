"""
This file has to do with every that goes on with operating the front desk for a performance.
"""
import Constants
import difflib

####################################################################
########################## EXCEPTIONS ##############################
####################################################################

#occurs when their is an attempt to accept payment for a seat that has already been payed for
class SeatAlreadyPaid(Exception):
    pass

#occurs when trying to accept payment and the payment type is invalid
class InvalidPayment(Exception):
    pass



#utility function for matching strings
def closest_payment(input_str):
    strings_list = [Constants.Payment.card, Constants.Payment.cash, Constants.Payment.check]
    # get the closest match of the input string in the list of strings
    match = difflib.get_close_matches(input_str, strings_list, n=1, cutoff=0.6)
    if match:
        return match[0]
    else:
        return Constants.Payment.cash



####################################################################
########################## MAIN FUNCTIONS ##########################
####################################################################

####################################
# Accept payment for a seat
# Params:
#   seat_id - id of the seat/ticket being purchased
#   payment_method - by what means they are paying for the seat/ticket.
#       Is of the enum Constants.Payment
#   email - optional,email/username of the person attempting to buy the seat.
#       if email is None, a reserved seat is being paid for.
#       if email is given, then an available seat is being purchased outright.
# Returns True on success, False otherwise
####################################
def accept_payment(seat_id, payment_method, email=None):

    #check that it is a proper payment type
    if not(payment_method in Constants.Payment.all):
        raise InvalidPayment()

    #check that it is not already paid, raise exception if already paid

    #Run query to mark it as paid
    #Place the email in the query if it needs to be.

    #return true on success



#######################################
# List of upcoming performances.
# only show future performances that are part of organizations the user volunteers with.
# params:
#   email - email of the volunteer
# returns a list of tuples where each tuple is a performance.
#   This is the same format the data is returned
#   in from the database.
#######################################
def upcoming_performances(email):
    result = Constants.query(
        "SELECT Performance.performance_id, Performance.time, Production.title, "
        "Production.venue_id FROM Volunteer "
        "JOIN User JOIN Production JOIN Performance "
        "ON User.user_id=Volunteer.user_id AND Performance.production_id=Production.id AND Production.org_id=Volunteer.org_id "
        "WHERE User.email=?",
        params=(email,))

    performances = []
    for id, datetime, title, venue_id in result:
        # parse out venue
        venue = 'Playhouse' if venue_id == 2 else 'Concert Hall'

        #parse out time
        tokens = datetime.split(' ')  # split on the space
        date = tokens[0]
        time = tokens[1]
        d_tokens = date.split('-')
        t_tokens = time.split(':')
        month = Constants.months[int(d_tokens[1])]
        year = d_tokens[0]
        day = d_tokens[2]
        hour = int(t_tokens[0])
        min = t_tokens[1]
        suffix = 'a.m.'
        if hour == 12:
            suffix = 'p.m.'
        elif hour > 12:
            hour = hour - 12
            suffix = 'p.m.'
        date = f'{month} {day}, {year}'  # example: "May 3, 2023"
        time = f'{hour}:{min} {suffix}'  # example: "6:00 p.m."

        #create the performance dictionary and append to list
        #performance = {'id': id, 'title':title,'date':date, 'time': time, 'venue': venue}
        performance = {'id': id, 'title': title, 'content': f'In the {venue} | {date} @{time}'}
        performances.append(performance)

    return performances




##############################################################################
# For when a seat is purchased from the front desk
# handles both buying an available ticket and processing payment for a reserved ticket
##############################################################################
def handle_payment(performance_id, number, row, section, payment_method):
    #get seat info from db
    q = f"""
    SELECT id, payment_method, user_id
    FROM Seat 
    WHERE performance_id={performance_id} AND number={number} AND section='{section}' AND row='{row}'
    """
    results = Constants.query(q)
    print(f'Received request to handle payment, query results:', results)
    user_id = results[0][2]

    #check that the seat exists
    if len(results) <= 0:
        return False

    seat_id = int(results[0][0]) #id of the seat
    payment_method = closest_payment(payment_method)

    #set the payment method
    Constants.query(f"""UPDATE Seat SET payment_method='{payment_method}' WHERE id={seat_id}""")

    #if seat has no User, assign it to the dummy User
    if user_id is None:
        Constants.query(f'UPDATE Seat SET user_id=33 WHERE id={seat_id}') #33 is of frontdesk user
    else:
        Constants.query(f'UPDATE Seat SET user_id={user_id} WHERE id={seat_id}')

    #return true for successful operation
    return True


#grabs the info for a seat, returns status and price
def get_seat_info(performance_id, number, row, section):
    print('Received request from front desk to get info for a seat')
    #TODO get the seat info here
    q = f"""
        SELECT user_id, payment_method, price
        FROM Seat 
        WHERE performance_id={performance_id} AND number={number} AND section='{section}' AND row='{row}'
        """
    results = Constants.query(q)
    print('RESULTS:', results)
    # check that the seat exists
    if len(results) <= 0:
        return False

    user_id = 33
    payment_method = results[0][1]
    data = dict()  #dictionary being returned

    #handle case where the user id is None
    if results[0][0] is None:
        user_id = None
        data['email'] = 'N/A'
    else:
        user_id = int(results[0][0])

        # grab the email of the user who bought it
        # first, check if it is the default user
        if user_id == 33:
            data['email'] = "*purchased at front desk*"
        else:
            r = Constants.query(f"""SELECT email FROM User WHERE user_id={user_id}""")
            print('ONE r:', r)
            data['email'] = r[0][0]





    #handle price not being set. Just set it to 5
    if results[0][2] is None:
        data['price'] = 5
    else:
        data['price'] = results[0][2]



    #status can ONLY be 'paid', 'reserved', or 'available'
    if user_id is None: #available
        data['status'] = 'available'
    elif payment_method is None:
        data['status'] = 'reserved'
    else:
        data['status'] = 'paid'

    #return data
    return data









######################################
# Load all the seats for a show
# params:
#   performance_id - id of the performance to show
# returns a list of tuples where each tuple is a seat.
#   This is the same format the data is returned
#   in from the database.
######################################
def load_seats(performance_id):
    pass


def test1():
    data = upcoming_performances("tom.bombadillo@arnornet.me")
    print(data)


def test2():
    results = handle_payment(performance_id=26, number=3, row='A', section='main_orch', payment_method=Constants.Payment.cash)
    print(results)


def test3():
    results = get_seat_info(performance_id=26, number=3, row='A', section='main_orch')
    print(results)




if __name__ == "__main__":
    test3()











