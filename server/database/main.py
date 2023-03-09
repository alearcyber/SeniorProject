import sqlite3
import re

# CONSTANTS DO NOT CHANGE!!!
TABLES = 5

def main():
  init_database()

'''
   ### RETURNS: 0 = 'database is good', 1 = 'database error occured' ###
   
   First establishes connection to database and queries for how many database exists.
   Next looks at three conditons
      -> Database exists with the numbers expected.
      -> Database is empty. Create the database.
      -> Database is missing a table.
'''
def init_database():
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT COUNT(1) FROM sqlite_master WHERE type='table' AND (name='user' OR name='organization' OR name='venue' OR name='volunteer' OR name='performance')")
  
  res = res.fetchall()
  #print(res[0][0])
  if (res[0][0] == TABLES):
    print("LOG: database is already setup")
    con.close()
    return 0
  elif (res[0][0] == 0):
    print("LOG: database has not been setup")
    print("LOG: creating and setting database")
    cur.execute("CREATE TABLE user (user_id INTEGER PRIMARY KEY AUTOINCREMENT, email, firstName, lastName, password, level)")
    cur.execute("CREATE TABLE organization (org_id INTEGER PRIMARY KEY AUTOINCREMENT, name, org_code)")
    cur.execute("CREATE TABLE venue (venue_id INTEGER PRIMARY KEY AUTOINCREMENT, name)")
    cur.execute("CREATE TABLE volunteer (user_id, org_id)")
    cur.execute("CREATE TABLE performance (performance_id INTEGER PRIMARY KEY AUTOINCREMENT, title, venue_id, org_id, image, desc, time)")
    cur.execute("INSERT INTO venue (name) VALUES ('playhouse')")
    cur.execute("INSERT INTO venue (name) VALUES ('concerthall')")
    cur.execute("INSERT INTO user (email, firstName, lastName, password, level) VALUES ('admin@admin.com', 'root', 'admin', 'password', 3)")
    con.commit()
    con.close()
    return 0
  else: 
    print("ERROR LOG: unexpected behavior with database init_database function")
    print("LOG: database shutting down")
    con.close()
    return 1

"""
   ### RETURNS: True = 'string has correct syntax/format', False = 'string does not meet length requirements or accepted character formatting' ###
   
   Checks to see if it meets requirements for input data.
"""
def isValid(string, minLen, maxLen, regex):
  if (len(string) >= minLen and len(string) <= maxLen and string != "" and bool(re.match(regex, string))):
    return True
  else:
    return False
  
if __name__ == "__main__":
  main()
