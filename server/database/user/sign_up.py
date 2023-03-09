"""
   ### RETURNS: 0 = 'user created sucessfully', 1 = 'invalid email', 2 = 'invalid first name'          ###
   ###          3 = 'invalid last name',  4 = 'invalid password', 5 = 'account has already been taken' ###
   
   First checks for if the email, first name, last name, and password are correctly formatted input.
   Next checks to see if email has already been taken.
   If it has not then create account with standard permissions.
   Else abort account creation.
"""
def sign_up_user(email, firstName, lastName, password):
  if (not isValid(email, 1, 32, "^[A-Za-z0-9@.]+$")):
    return 1
  if (not isValid(firstName, 1, 32, "^[A-Za-z0-9]+$")):
    return 2
  if (not isValid(lastName, 1, 32, "^[A-Za-z0-9]+$")):
    return 3
  if (not isValid(password, 1, 32, "^[A-Za-z0-9]+$")):
    return 4
  
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM user WHERE email=?",  (email,))
  if (res.fetchall() == []):
    cur.execute("INSERT INTO user (email, firstName, lastName, password, level) VALUES (?, ?, ?, ?, 1)", (email, firstName, lastName, password))
    con.commit()
    con.close()
    return 0
  else:
    con.close()
    return 5
