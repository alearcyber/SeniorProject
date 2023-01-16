import sqlite3


################################
# add a new venue
################################
def add_venue(id, name, n_rows, n_columns):
    #TODO - ensure proper arguments are passed thru

    #connect to the database
    # NOTE: will stall if someone else is connected when using sqlite, does not happen with postegres
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()


    #construct the query
    query = f'INSERT INTO venue VALUES ({id}, \"{name}\", {n_rows}, {n_columns});'
    print("Sending query:", query)

    #execute the query
    cursor.execute(query)

    #commit the changes and close the connection
    connection.commit()
    connection.close()
    return True #TODO - check to see if the query acutally went thru, return false if it fails


################################
# add a seat to the database
################################
def add_seat(row, column, venue):
    """
    :param row: positive integer
    :param column: positive integer
    :param venue: a string, non-null
    :return: True if it goes thru, false if otherwise
    """
    #TODO - ensure proper arguments are passed thru

    #connect to the database
    # NOTE: will stall if someone else is connected when using sqlite, does not happen with postegres
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()


    #construct the query
    query = f'INSERT INTO ticket VALUES ({row}, {column}, \"{venue}\");'
    print(query)

    #executre the query
    cursor.execute(query)

    #commit the changes and close the connection
    connection.commit()
    connection.close()












if __name__ == '__main__':
    add_seat(1, 1, "Theater")




