import sqlite3
import json
import Constants


class InvalidListItem(Exception):
  pass

def addressList(email, items):
  res = Constants.query("SELECT User.first_name, User.last_name, SeasonTicket.phone_number, SeasonTicket.address FROM User JOIN SeasonTicket ON User.user_id=SeasonTicket.user_id WHERE email=?", params=(email,))
  
  data = []
  data.append(items)
  for info in range(len(res)):
    lis = list(res[info])  
    temp = []
    for item in items:
      if item == "first_name":
        temp.append(lis[0])
      elif item == "last_name":
        temp.append(lis[1])
      elif item == "phone":
        temp.append(lis[2])
      elif item == "address":
        temp.append(lis[3])
      else:
        raise InvalidListItem()
    data.append(temp)
  return data
    
def exportAddressList(email, items, fmt):
  if (fmt == "csv"):
    return json.dumps(addressList(email, items))





def ticketList(email, items):
  res = Constants.query("SELECT Seat.row, Seat.number, Seat.section, Performance.title FROM Seat JOIN Performance JOIN User ON Seat.performance_id=Performance.performance_id AND Seat.user_id=User.user_id WHERE User.email=?", params=(email,))
  
  """
    First loop has a list of tuples that contain tickets.
    The first loops job is to get each individual ticket.
    The inner loop is for iterating throught the provided order and then swaps the orders.
    Then after append the ticket to a temp variable.
  """
  tickets = []
  tickets.append(items)
  for ticket in range(len(res)):
    temp = []
    lis = list(res[ticket])  
    for item in items:
      if item == "row":
        temp.append(lis[0])
      elif item == "number":
        temp.append(lis[1])
      elif item == "section":
        temp.append(lis[2])
      elif item == "title":
        temp.append(lis[3])
      else:
        raise InvalidListItem()
    tickets.append(tuple(temp))
      
  return tickets

def exportTicketList(email, items, fmt):
  if (fmt == "csv"): 
    return json.dumps(ticketList(email, items))





def importAddressList(email, data, fmt):
  items = list(data[0])
  key = [-1, -1, -1, -1]
  if (fmt == "csv"):
    for item in range(len(items)):
      if items[item] == "first_name":
        key[0] = item
      elif items[item] == "last_name":
        key[1] = item
      elif items[item] == "phone":
        key[2] = item
      elif items[item] == "address":
        key[3] = item
      else:
        raise InvalidListItem()
    
    if key[0] != -1:
      Constants.query("UPDATE User SET first_name=? WHERE email=?", params=(data[len(data) - 1][key[0]], email))
    if key[1] != -1:
      Constants.query("UPDATE User SET last_name=? WHERE email=?", params=(data[len(data) - 1][key[1]], email))
    if key[2] != -1:
      Constants.query("UPDATE User SET phone=? WHERE email=?", params=(data[len(data) - 1][key[2]], email))
    if key[3] != -1:
      Constants.query("UPDATE User SET address=? WHERE email=?", params=(data[len(data) - 1][key[3]], email))
    
        
def importTicketList(email, data, fmt):
  items = list(data[0])
  key = [-1, -1, -1, -1]
  if (fmt == "csv"):
    for item in range(len(items)):
      if items[item] == "row":
        key[0] = item
      elif items[item] == "number":
        key[1] = item
      elif items[item] == "section":
        key[2] = item
      elif items[item] == "title":
        key[3] = item
      else:
        raise InvalidListItem()
    
    user_id = Constants.query("SELECT user_id FROM User WHERE email=?", params=(email,))
    for item in data[1:]:
      row = ''
      number = ''
      section = ''
      title = ''
      
      if key[0] != -1:
        row = item[key[0]]
      if key[1] != -1:
        number = item[key[1]]
      if key[2] != -1:
        section = item[key[2]]
      if key[3] != -1:
        title = item[key[3]]
      Constants.query("INSERT INTO Seat (row, number, section, user_id) VALUES (NULL, NULL, NULL, NULL)", params=())
      seat_id = Constants.query("SELECT id FROM Seat WHERE row IS NULL AND number IS NULL AND section IS NULL AND user_id IS NULL", params=())
      Constants.query("UPDATE Seat SET row=?, number=?, section=?, user_id=? WHERE id=?", (row, number, section, str(user_id[0][0]), str(seat_id[0][0])))
      Constants.query("INSERT INTO SeasonTicket (user_id, seat_id, address, phone_number) VALUES (?, ?, (SELECT address FROM User WHERE email=?), (SELECT phone FROM User WHERE email=?))", params=(str(user_id[0][0]), str(seat_id[0][0]), email, email))

    
#########################
# TEST
#########################
'''
print(addressList("email.com", ['first_name', 'last_name', 'phone', 'address']))
print(addressList("email.com", ['address', 'phone', 'first_name', 'last_name']))
print(exportAddressList("brenda@gmail.com", ['address', 'phone', 'first_name', 'last_name'], "csv"))
print(ticketList("brenda@gmail.com", ['row', 'number', 'section', 'title']))
'''

    
print(importTicketList("brenda@gmail.com", [['row', 'number', 'section', 'title'], ['a', '1', 'ss', 'se']], "csv"))
#print(importAddressList("brenda@gmail.com", [['address', 'last_name'], ['123st', 'Joan'], ['12st', 'Joan']], "csv"))
