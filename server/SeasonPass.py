"""
This file implements the functionality for a user to purchase a season pass.

--Here is how buying a season pass works logically--
The user chooses the season they want to buy the season pass for. After selecting the season, they
will choose what seat they want reserved for that season. The seat they choose MUST be available for all
of the performances in that season. After choosing their seat, the user will select one performance
per production for all of the productions in the season. Those seats will then be marked as reserved for that user.
The user then must provide their credit card to process the payment (I suggest for simplicity we say season passes
can only be purchased with credit cards).They are now done.

--Here is how renewing a season pass works logically--
If a user is renewing their season pass, that means they already had one in the past. The user goes to a renew
season pass screen and will be presented with upcoming seasons to choose from. Once the user selects a season,
instead of selecting their seat and processing the payment information, all of their information and seat selection
are carried over from their most recent season pass. They have now 'renewed' their season pass, in otherwords,
they now have a season pass for the new season they selected.

--updating season pass information--
Updating season pass information will just be a single query. The user will basically input the information
into a form and press an 'update' button. A single query should be sufficient to make the
modifications within the database.
"""

import Constants




#########################################################################################################
################################### EXCEPTIONS ##########################################################
#########################################################################################################

# Occurs when trying trying to buy a season ticket and the selected seat is not avaialable
class SeatUnavailable(Exception):
    pass

# Occurs when user selects more than one performance per production in the season
class DuplicatePerformancesInProduction(Exception):
    pass

# Occurs if a request is sent to buy a season pass and any of the selected
# performances are not part of the season
# NOTE: This will probably never be used because the user will only ever see
#   performances that are part of the season they selected.
class PerformanceNotInSeason(Exception):
    pass








#########################################################################################################
################################### MAIN FUNCTIONS ######################################################
#########################################################################################################

#######################################
# grab the upcoming seasons
# Note: no parameters are required.
# The output is an associave array, (aka a dictionary)
# The data will look like so:
#   {title: month, title2: month2, etc.}
#######################################
def upcoming_seasons():
    # getting season and the times for the season
    # this query returns the earliest time associated with each season
    query_text = """
    SELECT MIN(Performance.time), Season.title, Production.venue_id
    FROM Season INNER JOIN Production JOIN Performance
    ON
    Performance.production_id = Production.id AND
    Production.season_id = Season.id
    WHERE Season.id IS NOT NULL
    GROUP BY Season.title
    """
    results = Constants.query(query_text)
    seasons = []
    for time, title, venue_id in results:
        out = dict()
        #parse out the proper month
        month = Constants.months[int(time.split('-')[1])]
        out['title'] = title
        out['month'] = month
        out['location'] = 'Playhouse' if int(venue_id) == 2 else 'Concert Hall'
        seasons.append(out)
    return seasons




#######################################
# grab all the Performances in a Season
# params:
#   season_id - The id for the season the performances are being grabbed from.
# returns a dictionary where the keys are all the names of the different productions
#   and the the value for each productions is the list of performances in that
#   production. The list of performances is a list of tuples.
#
# NOTE: CHANGED FROM PREVIOUS DEXSRIPTION ABOVE
#######################################
def get_all_season_performances(season_title):
    query_text = f"""
    SELECT
    prod.title, perf.time, prod.venue_id, perf.performance_id
        FROM
    Performance perf JOIN Production prod JOIN Season s
    ON perf.production_id=prod.id AND prod.season_id=s.id
        WHERE
    perf.time > datetime() AND s.title='{season_title}'
    """

    # execute and grab the results
    results = Constants.query(query_text)
    formatted_results = []
    for r in results:
        title = r[0]
        datetime = r[1]
        venue = 'Playhouse' if r[2] == 2 else 'Concert Hall'
        performance_id = r[3]

        # make datetime into date and time
        tokens = datetime.split(' ')  # split on the space
        date = tokens[0]
        time = tokens[1]
        d_tokens = date.split('-')
        t_tokens = time.split(':')

        # date
        month = Constants.months[int(d_tokens[1])]
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

        # append new map
        # example name: "Hamilton", date: "May 7", time: "6:00 p.m.", venue: "Civic Center Concert Hall", performance_id: "2"
        #new_result = {'name': title, 'date': date, 'time': time, 'venue': venue, 'performance_id': performance_id}
        new_result = {'title': title, 'id': performance_id,
                      'content': f'On {date} @ {time}'}
        formatted_results.append(new_result)

    # return the results in the appropriate format
    return formatted_results




#######################################
# Gets the availablility for the seats within a given season
# Only parameters is the season_id
# NOTE: Only needs to return one list of seats with only two peices of information per seat
#   - Whether it is available for ALL the performances of a season
#   - The price
# Return list of tuples.
#######################################
def season_seat_availability(season_id):
    pass



#######################################
# Buy a season pass
# params:
#   email - the email of the user purchasing the season pass
#   seat_row - row of the seat to be reserved
#   seat_number - number of the seat to be reserved
#   FINISH THIS HERE
#######################################
def buy_season_pass(email, seat_row, seat_number, performances_ids, season_id, price):
    pass


#seat availability for season id
def season_seat_availability(season_id):
  return Constants.query("SELECT Seat.id, Seat.price FROM Season JOIN Production ON Season.id=Production.season_id "
               "JOIN Performance ON Production.id=Performance.production_id JOIN Seat "
               "ON Seat.performance_id=Performance.performance_id WHERE Season.id=? AND Seat.user_id IS NULL",
               params=(season_id,))










#test retreival of upcoming seasons
def test1():
    upcoming_seasons()

#getting all the performances for a specific season
def test2():
    season_title = 'Movies'
    data = get_all_season_performances(season_title)
    print(data)


if __name__ == "__main__":
    test2()