"""
@Author Aidan Lear
This file contains constants to be used for the backend
"""
import pickle
import sqlite3


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
    connection.commit()
    connection.close()

    # return a list of results
    return result




###########################################################################
# Send Multiple parameterized queries to the database
# params - a list of tuples, where each tuple is to be executed.
# query_text - The SQL statement to place the tuples into from params
# returns true on success
# NOTE: does NOT return the results of the query. Only use for inserting.
###########################################################################
def insert_many(query_text, params):
    # establish connection with database
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    #execute the query
    cursor.executemany(query_text, params)

    #commit change and close the connection
    connection.commit()
    connection.close()
    return True



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
# Mapping months the number to the approprate month text.
# For example, 1 is January, 2 is February, etc.
###########################################################################
months = ['nada', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']






#Format datetime string in a readable way, returns a 2-tuple of strings: (date, time)
def format_datetime(datetime):
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
    return date, time


#mapping section names internally to ones for user to view
section_name_map = {"main_orch": "Main Orchestra",
      "left_orch": "Left Orchestra",
      "right_orch": "Right Orchestra",
      "balc": "Balcony",
      "right_box": "Right Box",
      "left_box": "Left Box",
      "left_loge": "Left Loge",
      "right_loge": "Right Loge"}




#test formatting of datetime strings
def test1():
    date, time = format_datetime("2023-08-02 12:30:00")
    print('date:', date, ' | time:', time)



if __name__ == "__main__":
    print('--Running tests for Constants.py--')
    test1()
