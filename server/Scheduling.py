"""
@Author Aidan Lear, Jainum Patel

This File will have all the backend logic for Scheduling Productions.
This includes all of the performances that go along with that production,
and it includes the seats for the performances of the production
"""

import Constants
from Constants import query
import sqlite3

"""
QUESTIONS: where does venue id belong?
           How to represent duration?
           Production id returned from add production?
"""

#####################################################################################
################################ EXCEPTIONS #########################################
#####################################################################################


class InvalidFormat(Exception):
    pass


class ProductionExists(Exception):
    pass


class InvalidID(Exception):
    pass


class InvalidTime(Exception):
    pass


class InvalidPermission(Exception):
    pass


####################################################################
# This will initialize the empty seats/tickets for a performance
#   that takes place in the playhouse venue
# Params:
#   performance_id - What performance takes place in the
#
# NOTE: The information for the seats is stored in
#   binary files. This would include the x, y, row, number, and
#   section.
#
# Playhouse is venue id 2
####################################################################
def initialize_playhouse_seats(performance_id):
    # Read playhouse seating data into memory
    seating_data = Constants.load_playhouse_data()

    # parse seating data
    for section in seating_data:  # loop through each sections
        # grab the list of seat data for each section
        seats = seating_data[section]
        # This loop iterates over all the seats in the playhouse
        for seat in seats:
            # debug print
            # print(f"x:{seat['x']}, y:{seat['y']}, section:{seat['sec']}, row:{seat['row']}, number:{seat['number']}")

            # construct the query
            query_text = "INSERT INTO Seat " \
                "(row, number, x, y, user_id, venue_id, performance_id, section, payment_method) " \
                "VALUES " \
                "(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            params = (seat['row'], seat['number'], seat['x'],
                      seat['y'], None, 2, performance_id, seat['sec'], None)

            # insert into the table
            Constants.query(query_text, params)
    return True


##################################################
# adds a single item to production table
##################################################
def add_production(title, venue_id, org_id, image, desc, duration):
    """
    # Test for if input matches expected pattern.
    if (not isValid(title, 1, 32, "^[A-Za-z0-9 ]+$")):
        raise InvalidFormat
    if (not isValid(str(venue_id), 1, 1, "1|2")):
        raise InvalidFormat
    if (not isValid(str(org_id), 1, 3, "^[0-9]+$")):
        raise InvalidFormat
    if (not isValid(image, 1, 32, "^[A-Za-z0-9/:]+$")):
        raise InvalidFormat
    if (not isValid(desc, 1, 1024, "^[A-Za-z0-9 .!?]+$")):
        raise InvalidFormat

    # Test for if duration matches expected pattern.
    if (not isValid(str(duration), 1, 3, "^[0-9]$")):
        raise InvalidFormat
    if (duration <= 0 or duration > 300):
        raise InvalidFormat
    """

    # insert the production
    query_text = "INSERT INTO Production " \
                 "(title, venue_id, org_id, image, description, duration) " \
                 "VALUES (?, ?, ?, ?, ?, ?)"
    parameters = (title, venue_id, org_id, image, desc, duration)
    query(query_text, params=parameters)

    # grab and return the id of the recently inserted production
    results = Constants.query(
        f"SELECT id FROM Production where title='{title}'")
    id = int(results[0][0])
    return id


##################################################
# adds a single item to performance table
##################################################
def add_performance(production_id, startTime):
    """
    if (not isValid(str(production_id), 1, 8, "^[0-9]+$")):
        raise InvalidID
    if (not isValid(startTime, 19, 19,
                    "^20[0-9]{2}-([0][1-9]|[1][0-2])-([0-2][1-9]|[3][0-1]) ([0-1][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]$")):
        raise InvalidFormat

    con = sqlite3.connect(Constants.DB_PATH)
    cur = con.cursor()
    res = cur.execute("INSERT INTO Performance (production_id, time) VALUES (?, ?)", (production_id, startTime))
    """
    connection = sqlite3.connect(Constants.DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Performance (production_id, time) VALUES (?, ?)", (production_id, startTime))
    id = cursor.lastrowid
    connection.commit()
    connection.close()
    return id


def is_timeslot_available(startTime, endTime, venue_id):
    """
       Checks to see if end time is reasonable.
       End time cannot equal or less than to start time.
       Also cannot end time be more than 5 hours than the start time.
    """
    """
    #doesn't make sense for this to be here. This function checks to see if the timeslote is open, that is all.
    #have another function that checks for extrema in the times given
    date = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    tempDate = datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
    if (tempDate <= date):
        con.close()
        raise InvalidTime
    date += timedelta(hours=5)
    if (tempDate > date):
        con.close()
        raise InvalidTime
    # Checks for unreasonable startTime. IE Before current time or an hour after current time.
    date = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    tempDate = datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    date += timedelta(hours=5)
    if (tempDate < date):
        con.close()
        raise InvalidTime
    """

    # Query for performances in the venue within a given time frame
    result = query("SELECT 1 FROM performance WHERE venue_id=? AND (startTime AND endTime BETWEEN ? AND ?)",
                   (venue_id, startTime, endTime))

    # return true if no performances were there in the given time frame, false otherwise
    if len(result) <= 0:
        return True
    else:
        return False


def get_production_id_from_title(title):
    con = sqlite3.connect(Constants.DB_PATH)
    cur = con.cursor()
    res = cur.execute(
        "SELECT production_id FROM Production WHERE title=?", title)
    return res


def schedule_performances(user, title, venue_id, org_id, image, desc, duration, times):
    # validate the user first
    if (not isValid(user, 1, 32, "^[A-Za-z0-9]+@[a-z]+\.(edu|com|net|org)$")):
        raise InvalidPermission

    con = sqlite3.connect(Constants.DB_PATH)
    cur = con.cursor()
    res = cur.execute(
        "SELECT 1 FROM volunteer INNER JOIN user ON user.user_id=volunteer.user_id WHERE user.email=? AND user.level=2 AND volunteer.org_id=?",
        (user, int(org_id)))
    if (not res.fetchall() == [(1,)]):
        con.close()
        raise InvalidPermission

    # add single entry to the production table. If it fails it throws an exception
    try:
        add_production(title, venue_id, org_id, image, desc, duration)
    except:
        raise ProductionExists

    # grab the id of the production just entered
    production_id = get_production_id_from_title(title)

    invalidTimes = ""
    isInvalidTime = False
    # add entry to performance table for all of the showtimes
    for time in times:
        # check for conflicting timeslot
        try:
            is_timeslot_available(time, datetime.strptime(time, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=duration),
                                  venue_id)
        except:
            if (isInvalidTime == False):
                isInvalidTime = True
            invalidTimes = time + " "

        if (isInvalidTime == True):
            raise InvalidTime

    for time in times:
        add_performance(production_id, time)


##########################################################
# Create a new production
# This function does ALL the stuff for
#   creating a production, the corresponding performances
#   and seats/tickets for each performance
# Params:
#   title, venue_id, org_id, description - all self descriptive
#   image - path to where the image is as a string
#   duration - integer, how many minutes the show lasts
#   times - list of performance times, will be formatted
#       as "%Y-%m-%d %H:%M:%S", no am pm, 24 hour day cycle
#
# returns the id of the created production
##########################################################
def create_new_production(title, venue_id, org_id, image, description, duration, times):
    # first, insert item into production table
    # parameters are (title, venue_id, org_id, image, descrition, duration)
    production_id = add_production(
        title, venue_id, org_id, image, description, duration)

    # iterate over the times, add performance and initialize the seats
    for time in times:
        # add the performance
        # params: (production_id, startTime)
        performance_id = add_performance(production_id, time)

        # add seats for that performance
        if venue_id == 2:  # playhouse
            initialize_playhouse_seats(performance_id)
        else:  # conert hall, venue_id == 1
            assert False, "HEY, I HAVE NOT MADE THE SEATING THING FOR THE CONCERT HALL YET"

    # return the id of the production that was added
    return production_id

# Set all section prices for a production
def set_section_prices(production_id, section_prices):

    query_text = """UPDATE Seat
                    SET
                        price = ?
                    WHERE
                        section = ?
                    AND
                        performance_id IN (
                        SELECT Performance.performance_id
                        FROM Production JOIN Performance
                        ON Production.id = Performance.production_id
                        WHERE Production.id=?)
                    """
    for section_name in section_prices:
        price = section_prices[section_name]
        Constants.query(query_text, params=(price, section_name, production_id))

    return True


class InvalidFormat(Exception):
    pass


class ProductionExists(Exception):
    pass


class InvalidID(Exception):
    pass


class InvalidTime(Exception):
    pass


class InvalidPermission(Exception):
    pass


#####################################################################################
################################ TESTS ##############################################
#####################################################################################


##########################################################
# Test intitlizing the seats for a playhouse performance
##########################################################
def test1():
    initialize_playhouse_seats(1)


##########################################################
# Test add production
##########################################################
def test2():
    # (title, venue_id, org_id, image, desc, duration)
    production_id = add_production(
        'TESTING ADDING SECOND PRODUCTION', None, None, None, None, None)
    print('id of production added:', production_id)


##########################################################
# Test scheduling a new performance
##########################################################
def test3():
    title = 'Inception'
    description = 'It is a movie about a dream within a dream'
    times = [  # four days in a row at 12:30
        "2022-01-01 12:30:00",
        "2022-01-02 12:30:00",
        "2022-01-03 12:30:00",
        "2022-01-04 12:30:00",
    ]
    duration = 120  # 120 minutes, 2 hours

    # params for creating a new production
    # (title, venue_id, org_id, image, description, duration, times)
    create_new_production(title, 2, None, None, description, duration, times)


#######################################################
# For running tests
#######################################################
if __name__ == '__main__':
    test3()
