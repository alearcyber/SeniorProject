"""
   Login Function.
   0 = success, 1 = failure
"""
def login_user(username, password):
  username = username.strip()
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM account WHERE username=? AND password=?", (username, password))
  if (res.fetchall() == [(1,)]):
    con.close()
    return 0
  else:
    con.close()
    return 1
