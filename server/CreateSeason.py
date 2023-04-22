"""
This file has all the backend logic for creating a new season.
Specifically, The productions that belong in whatever season is being made, are assumed
to already have been created. They are just being added to the season.
The shows are already schedule as well. The already existing producitons are just being added to the season
"""
import Constants
from Constants import query




"""
--The logic--
First thing, some person on their account goes to the create season menu. 

As a part of loading the create season menu
    - They will receive a list of productions that they can select from to be part of the season
        that they are creating.
    - That list of productions will ONLY be productions that are
            -in the future
            -are not already part of a season
            -AND are actually hosted by THEIR organization
            
User types the information into the box, i.e. title and description of the season.
That user then clicks on the producitons they want to be a part of the season.
Then they select some confirm button to confirm the changes.

When the confirm button is selected, some things are sent our way:
    - A list of production ids for the productions they selected
    - The informatiom about the season itself.

What we do with this information...
    - create a new entry (a new row) in the Season table
    - Add the season id for the season that was just created as the season_id column for all of the 
        productions that were sent to us.
"""




###################################
# CODE FROM JAINUM
###################################

"""
add_production_to_season = add_productions_to_season ?
work on get_future_list_of_productions. What outputs ?
"""


def add_season(org_id, title, description):
    query("INSERT INTO Season (org_id, name, description) VALUES (?, ?, ?)", params=(org_id, title, description))
    return query("SELECT id FROM Season WHERE org_id=? AND name=? AND description=?",
                 params=(org_id, title, description))


def add_productions_to_season(productions, season_id):
    for production in productions:
        query("UPDATE Production SET season_id=? WHERE id=?", params=(season_id, production))

def get_org_name(org_id):
    return query("SELECT name FROM Organization WHERE org_id=?", params=(org_id,))

def is_volunteer(email, org_id):
    return query(
        "SELECT 1 FROM volunteer INNER JOIN user ON user.user_id=volunteer.user_id WHERE user.email=? AND user.level=2 AND volunteer.org_id=?",
        params=(email, int(org_id)))


#######################################
# Available productions to select from
#######################################
def get_future_list_of_productions(email, org_id):
    if (is_volunteer(email, org_id) != [(1,)]):
        raise InvalidPermission


    query_text = "select id, title from Production where org_id=? and (select season_id from Production where org_id=?) IS NULL;"

    result = query(query_text, (org_id,org_id))
    return result


#THIS IS THE DRIVER FUNCTION FOR DOING STUFF
def main(email, org_name, productions, title, description):
    org_id = query("SELECT org_id FROM Organization WHERE name=?", params=(org_name,))
    if (org_id == []):
        raise InvalidPermission

    if (is_volunteer(email, org_id) != [(1,)]):
        raise InvalidPermission

    if (not isValid(title, 1, 32, "^[A-Za-z0-9 ]+$")):
        raise InvalidFormat
    if (not isValid(description, 1, 1024, "^[A-Za-z0-9 .!?]+$")):
        raise InvalidFormat

    season_id = add_season(org_id, title, description)
    add_productions_to_season(productions, season_id)











