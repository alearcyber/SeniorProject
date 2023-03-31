import sqlite3
"""
Queries the database with the given account information.
If a user with the given email already exists, an appropriate message is sent
to the client.
If not, a new user is inserted with the given information and a success message is returned.
"""
def sign_up_user(email, firstName, lastName, password, venue_id):

  # Query the database for a matching email
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  res = cursor.execute("SELECT 1 FROM user WHERE email=?",  (email,))

  # Case where the email does NOT exist in the db: insert a new user
  if (res.fetchall() == []):
    level = 1
    if (venue_id != ""):
      level = 2
    cursor.execute("INSERT INTO user (first_name, last_name, email, password, level) VALUES (?, ?, ?, ?, ?)", (firstName, lastName, email, password, level))
    connection.commit()
    connection.close()
    return 'success'
  else:
  # Case where the email already exists: inform the client and don't insert the user
    connection.close()
    return 'account_exists'
