import sqlite3
from database.volunteer.volunteer import add_volunteer
from database.main import isValid


############################################################
# add a volunteer
############################################################
def register_user_as_volunteer(email, org_passcode):
  # get the id of the user with the corresponding email
  # user_id = SELECT user_id FROM User where email={email};

  # org_id, we have this alreayd
  # INSERT INTO Volunteer (user_id, org_id) VALUES ({user_id},{org_id});

  pass




"""
Queries the database with the given account information.
If a user with the given email already exists, an appropriate message is sent
to the client.
If not, a new user is inserted with the given information and a success message is returned.
"""
def sign_up_user(email, firstName, lastName, password, org_code):

  # Checks to see if user is valid before searching database for user.
  if (not isValid(email, 1, 256, "^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+$")):
    return 'invalid_email'

  # Query the database for a matching email
  connection = sqlite3.connect("database.db")
  cursor = connection.cursor()
  res = cursor.execute("SELECT 1 FROM user WHERE email=?",  (email,))

  # Case where the email does NOT exist in the db: insert a new user
  if (res.fetchall() == []):
    cursor.execute("INSERT INTO user (first_name, last_name, email, password, level) VALUES (?, ?, ?, ?, ?)", (firstName, lastName, email, password, 1))
    
    connection.commit()
    connection.close()
    if (org_code != ""):
      print(add_volunteer(email, org_code))
    return 'success'
  else:
  # Case where the email already exists: inform the client and don't insert the user
    connection.close()
    return 'account_exists'
