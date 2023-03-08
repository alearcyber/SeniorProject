import sqlite3
import re

# CONSTANTS DO NOT CHANGE!!!
TABLES = 5

def main():
  init_database()

def init_database():
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  res = cur.execute("SELECT COUNT(1) FROM sqlite_master WHERE type='table'")
  
  res = res.fetchall()
  #print(res[0][0])
  if (res[0][0] == TABLES):
    print("LOG: database is already setup")
    con.close()
    return 0
  elif (res[0][0] == 0):
    print("LOG: database has not been setup")
    print("LOG: creating and setting database")
    cur.execute("CREATE TABLE user (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username, password, level)")
    cur.execute("CREATE TABLE organization (org_id INTEGER PRIMARY KEY AUTOINCREMENT, name, org_code)")
    cur.execute("CREATE TABLE venue (venue_id INTEGER PRIMARY KEY AUTOINCREMENT, name)")
    cur.execute("CREATE TABLE volunteer (user_id, org_id)")
    cur.execute("CREATE TABLE performance (performance_id INTEGER PRIMARY KEY AUTOINCREMENT, title, venue_id, org_id, image, desc, time)")
    cur.execute("INSERT INTO venue (name) VALUES ('playhouse')")
    cur.execute("INSERT INTO venue (name) VALUES ('concerthall')")
    con.commit()
    con.close()
    return 0
  else: 
    print("ERROR LOG: unexpected behavior with database init_database function")
    print("LOG: database shutting down")
    con.close()
    return 1
    exit()

if __name__ == "__main__":
  main()
