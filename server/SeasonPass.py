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
from Constants import Query



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
# returns a list of tuples where each tuple is a season.
#   This is the same format the data is returned as from the database query
#######################################
def upcoming_seasons():
    pass



#######################################
# grab all the Performances in a Season
# params:
#   season_id - The id for the season the performances are being grabbed from.
# returns a dictionary where the keys are all the names of the different productions
#   and the the value for each productions is the list of performances in that
#   production. The list of performances is a list of tuples.
#######################################
def get_all_season_performances(season_id):
    pass



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


