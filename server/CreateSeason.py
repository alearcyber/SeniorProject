"""
This file has all the backend logic for creating a new season.
Specifically, The productions that belong in whatever season is being made, are assumed
to already have been created. They are just being added to the season.
The shows are already schedule as well. The already existing producitons are just being added to the season
"""
import Constants
from Constants import query




#adds a single entry to the Season table
#returns a Season_id
def add_season(org_id, title, description):
    pass



def add_productions_to_season(productions):
    pass


#checks if a user is a volunteer of an organization
def is_volunteer(email):
    pass



#check if a production is already part of a season
#returns a boolean



#get all future productions for the employee, so that they can have a list of productions
#to choose from when creating the season.
# return the information in the same data structure the query returns it as.
#THIS IS FOR THE FIRST PART
def get_future_list_of_productions(email, org_id):
    pass


#given a production_id, add that production to the season.
def add_production_to_season(production_id, season_id):
    pass






#This is the MAIN function for adding all the information
def main(email, org_name, list_of_production_ids, title, description):
    #check that the person is even part of the org
    #throw some Exception if they are not part of the org


    org_id = #grab the org id form the named

    season_id = add_season(org_id, title, description)

    #at this point, the season has been succesfully added
    #now we want to register the selected productions as being part of the season
    for production_id in list_of_production_ids:
        add_produciton_to_season(production_id, season_id)

    #done





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







