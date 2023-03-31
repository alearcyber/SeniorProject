import sqlite3
"""
Queries the database with the given login information.
If the database returned anything, send the user's name back to the client.
If not, send a failure message.
"""
def login_user(email, password):
  email = email.strip() # Strip whitespace from the email

  #  Query the database: try to get one first_name from it with the given email and password
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  res = cursor.execute("SELECT first_name FROM user WHERE email=? AND password=?", (email, password))
  name = res.fetchone()

  # Case where the db returned a name
  if (name != None):
    print("Success: " + name[0])
    connection.close()
    return name[0]
  else:
  # Case where the db returned None
    print("Failed")
    connection.close()
    return "fail"
