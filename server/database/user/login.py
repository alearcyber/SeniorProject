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
  res = cursor.execute("SELECT first_name,level FROM user WHERE email=? AND password=?", (email, password))
  user_info = res.fetchone()
  print(user_info)

  # Case where the db returned a name
  if (user_info != None):
    print("Success: " + user_info[0])
    connection.close()
    return user_info
  else:
  # Case where the db returned None
    print("Failed")
    connection.close()
    return "fail"
