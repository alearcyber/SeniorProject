import sqlite3
import json


def get_shows():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    query = f'SELECT performance_id, title, image FROM Performance;'
    #print("Sending query:", query)

    cursor.execute(query)

    rows = cursor.fetchall()


    #make the dummy descriptions

    new_rows = []
    for i in range(len(rows)):
        new_row = []
        for element in rows[i]:
            new_row.append(element)
        new_row.append('INSERT DESCRIPTION HERE')
        new_rows.append(new_row)

    rows = new_rows

    for row in rows:
        pass
        #print(row)

    #connection.commit()
    connection.close()

    #CONSTURCT THE JSON
    #output = {}
    output = []
    for i in range(len(rows)):
        row = rows[i]
        show_dictionary = {
            'id': row[0],
            'name': row[1],
            'imgurl': row[2],
            'description':row[3]
        }

        #output[str(i)] = show_dictionary
        output.append(show_dictionary)

    json_object = json.dumps(output, indent=4) #convert dictionary to JSON
    #print(json_object) # print out the JSON for testing if it worked








    #RETURN THE JSON
    #id, name, imgurl, description are the json thingies
    #return str(json_object)
    return output


def test():
    print(get_shows())



if __name__ == "__main__":
    test()