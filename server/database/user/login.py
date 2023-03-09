"""
   ### RETURNS: 0 = 'login success' 1 = 'login failure' ###
   
   First remove white space before and after the email.
   Connect to database and check to see if there is an entry for that user in the database.
   Return the login operation status and close the connection.
"""
def login_user(email, password):
  email = email.strip()
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM user WHERE email=? AND password=?", (email, password))
  if (res.fetchall() == [(1,)]):
    con.close()
    return 0
  else:
    con.close()
    return 1
