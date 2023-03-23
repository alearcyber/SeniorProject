"""
   ### RETURNS: 0 = 'volunteer successfully added', 1 = 'email is invalid', 2 = 'email is not registered to an account'  ###
   ###          3 = 'organization name is not valid', 4 = 'organization code is not valid', 5 = 'organization does not exists' ###
   
   First checks to see if email is valid. Next check to see if the email has been registered in the database and see if account level is eligible.
   Next see if name and organization code of organization is valid. Finally see if the organization does not exists. If insert the volunteer into the database.
   Then change user level to 2 and they are inserted into the volunteer table.
"""
def add_volunteer(user, name, org_code):
  # Checks to see if user is valid before searching database for user.
  if (not isValid(user, 1, 32, "^[A-Za-z0-9]+@[a-z]+\.(edu|com|net|org)$")):
    return 1
  
  # Checks for if the user exists and their level corresponds to a regular user.
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM user WHERE email=? AND (level=1 OR level=2)", (user,))
  if (not res.fetchall() == [(1,)]):
    con.close()
    return 2
  
  # Remove white space and see if the input matches the pattern expected.
  name = name.strip()
  if (not isValid(name, 1, 32, "^[A-Z][A-Za-z ]+$")):
    con.close()
    return 3
  org_code = org_code.strip()
  if (not isValid(org_code, 8, 32, "^[A-Za-z0-9]+$")):
    con.close()
    return 4
  
  # Check to see if the organization exists and if the code matches with that organization. Add user to volunteer.
  res = cur.execute("SELECT 1 FROM organization WHERE name=? AND org_code=?",  (name, org_code))
  if (res.fetchall() != []):
    cur.execute("UPDATE user SET level=2 WHERE email=?", (user,))
    cur.execute("INSERT INTO volunteer (user_id, org_id) VALUES ((SELECT user_id FROM USER WHERE email=?), (SELECT org_id FROM organization WHERE name=?))", (user, name))
    con.commit()
    con.close()
    return 0
  else:
    con.close()
    return 5
