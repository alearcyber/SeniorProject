"""
This file has to do with every that goes on with operating the front desk for a performance.
"""
import Constants

####################################################################
########################## EXCEPTIONS ##############################
####################################################################

#occurs when their is an attempt to accept payment for a seat that has already been payed for
class SeatAlreadyPaid(Exception):
    pass

#occurs when trying to accept payment and the payment type is invalid
class InvalidPayment(Exception):
    pass



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




######################################
# Load all the seats for a show
# params:
#   performance_id - id of the permormance to show
# returns a list of tuples where each tuple is a seat.
#   This is the same format the data is returned
#   in from the database.
######################################
def load_seats(performance_id):
    pass



def test1():
    data = upcoming_performances("tom.bombadillo@arnornet.me")
    print(data)



if __name__ == "__main__":
    test1()











