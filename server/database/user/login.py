import sqlite3
"""
   ### RETURNS: 0 = 'login success' 1 = 'login failure' ###
   
   First remove white space before and after the email.
   Connect to database and check to see if there is an entry for that user in the database.
   Return the login operation status and close the connection.
"""
def login_user(email, password):
  email = email.strip()
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  res = cursor.execute("SELECT first_name FROM user WHERE email=? AND password=?", (email, password))
  name = res.fetchone()
  if (name != None):
    print("Success: " + name[0])
    connection.close()
    return name[0]
  else:
    print("Failed")
    connection.close()
    return "fail"
