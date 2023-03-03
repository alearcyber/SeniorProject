"""
   If the username password and level are in correct format it will reject it.
   Next sees if the username is taken.
"""
def sign_up_account(username, password, level):
  if (not isValid(username, 8, 64, "^[A-Za-z0-9]+$")):
    return 1
  if (not isValid(password, 8, 64, "^[A-Za-z0-9]+$")):
    return 2
  if (not isValid(level, 1, 1, "^[0-2]")):
    return 3
    
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM user WHERE username=?",  (username))
  return res == cur
