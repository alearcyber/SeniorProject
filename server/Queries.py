import sqlite3
import json


def get_shows():

    # Setup database query
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    query = f'SELECT performance_id, title, image FROM Performance;'

    # Execute the query
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    # Make the dummy descriptions
    new_rows = []
    for r in rows:
        record = list(r)
        record.append('INSERT DESCRIPTION HERE')
        new_rows.append(record)

    rows = new_rows

    # CONSTRUCT THE JSON
    output = []
    for i in range(len(rows)):
        row = rows[i]
        production = {
            'id': str(row[0]),
            'name': row[1],
            'imgurl': row[2],
            'description':row[3]
        }
        output.append(production)

    #convert dictionary to JSON
    json_object = json.dumps(output, indent=4)

    #RETURN THE JSON
    #id, name, imgurl, description are the json thingies
    #return str(json_object)
    return output

def test():
    get_shows()

if __name__ == "__main__":
    test()