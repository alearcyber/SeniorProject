"""
@Author Aidan Lear
This file contains constants to be used for the backend
"""


#Path to the database
DB_PATH = 'database.db'






############################################
# Enum for the possible payment types
############################################
class Payment():
    card = 'card'
    cash = 'cash'
    check = 'check'
    none = None
    all = {'card', 'cash', 'check', None}




###########################################################################
# Send any Query to the database
###########################################################################
def query(query_text, params=None):
    # establish connection with database
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    results = None # holds the results from the query


    if params is None: #handle a raw query
        # Execute the query and get the results
        result = cursor.execute(query_text).fetchall()
    else: # handle parameterized query
        result = cursor.execute(query_text, params).fetchall()

    # close the connection
    connection.close()

    # return a list of results
    return result


