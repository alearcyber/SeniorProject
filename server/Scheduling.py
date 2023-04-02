"""
@Author Aidan Lear, Jainum Patel

This File will have all the backend logic for Scheduling Productions.
This includes all of the performances that go along with that production,
and it includes the seats for the performances of the production
"""

import Constants
from Constants import query

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


#######################################################
# Check if a Production already exists in the database
# uses the title as input
#######################################################





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
# PLayhouse is venue id 2
####################################################################
def initialize_playhouse_seats(performance_id):
    #Read playhouse seating data into memory
    seating_data = Constants.load_playhouse_data()

    #parse seating data
    for section in seating_data: # loop through each sections
        seats = seating_data[section] # grab the list of seat data for each section
        # This loop iterates over all the seats in the playhouse
        for seat in seats:
            # debug print
            # print(f"x:{seat['x']}, y:{seat['y']}, section:{seat['sec']}, row:{seat['row']}, number:{seat['number']}")

            #construct the query
            query_text = "INSERT INTO Seat " \
                    "(row, number, x, y, user_id, venue_id, performance_id, section, payment_method) " \
                    "VALUES " \
                    "(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            params = (seat['row'], seat['number'], seat['x'], seat['y'], None, 2, performance_id, seat['sec'], None)

            #insert into the table
            Constants.query(query_text, params)
    return True




##################################################
# adds a single production entry to the database
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

    #insert the production
    query("INSERT INTO Production (title, venue_id, org_id, image, description, duration) VALUES (?, ?, ?, ?, ?, ?)", params=(title, venue_id, org_id, image, desc, duration))
    return True



def add_performance(production_id, org_id, startTime):
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
    query("INSERT INTO Performance (production_id, time) VALUES (?, ?)", (production_id, startTime))
    return True


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


    #Query for performances in the venue within a given time frame
    result = query("SELECT 1 FROM performance WHERE venue_id=? AND (startTime AND endTime BETWEEN ? AND ?)",
                      (venue_id, startTime, endTime))

    #return true if no performances were there in the given time frame, false otherwise
    if len(result) <= 0:
        return True
    else:
        return False



def get_production_id_from_title(title):
    con = sqlite3.connect(Constants.DB_PATH)
    cur = con.cursor()
    res = cur.execute("SELECT production_id FROM Production WHERE title=?", title)
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





#######################################################
# Tests for this file
#######################################################
def tests():
    initialize_playhouse_seats(1)



#######################################################
# For running tests
#######################################################
if __name__ == '__main__':
    tests()
