"""
   ### RETURNS: 0 = 'organization successfully created', 1 = 'email is invalid', 2 = 'email is not registered to an account'  ###
   ###          3 = 'organization name is not valid', 4 = 'organization code is not valid', 5 = 'organization already exists' ###
   
   First checks to see if email is valid. Next check to see if the email has been registered in the database and see if account level has the privileges.
   Next see if name and organization code of organization is valid. Finally see if the organization aleady exists. If insert the organization into the database.
   Then change user level to 2 and they are inserted into the volunteer table.
   
   NOTE: This function is under the assumption that any user may create an organization. This function may be subjected to change. 
"""
def add_organization(user, name, org_code):
  # Checks to see if user is valid before searching database for user.
  if (not isValid(user, 1, 32, "^[A-Za-z0-9]+@[a-z]+\.(edu|com|net|org)$")):
    return 1
  
  """
     Checks for if the user exists and their level corresponds to a regular user.
  """
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT 1 FROM user WHERE email=? AND level=1", (user,))
  if (not res.fetchall() == [(1,)]):
    con.close()
    return 2
  
  if (not isValid(name, 1, 32, "^[A-Z][A-Za-z ]+$")):
    con.close()
    return 3
  if (not isValid(org_code, 8, 32, "^[A-Za-z0-9]+$")):
    con.close()
    return 4
    
  res = cur.execute("SELECT 1 FROM organization WHERE name=?",  (name,))
  if (res.fetchall() == []):
    cur.execute("INSERT INTO organization (name, org_code) VALUES (?, ?)", (name, org_code))
    cur.execute("UPDATE user SET level=2 WHERE email=?", (user,))
    cur.execute("INSERT INTO volunteer (user_id, org_id) VALUES ((SELECT user_id FROM USER WHERE email=?), (SELECT org_id FROM organization WHERE name=?))", (user, name))
    con.commit()
    con.close()
    return 0
  else:
    con.close()
    return 5
