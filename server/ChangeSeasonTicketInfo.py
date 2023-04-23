import Constants
import sqlite3

def getPastSeason(email):
  return Constants.query("SELECT SeasonTicket.id, SeasonTicket.user_id FROM SeasonTicket JOIN Season ON SeasonTicket.season_id=Season.id WHERE Season.org_id=(SELECT Volunteer.org_id FROM User JOIN Volunteer ON User.user_id=Volunteer.user_id WHERE User.email=?)", (email,))


def changeSeasonInfo(user_id, season_ticket_id, fname, lname, address, phone):
  Constants.query("UPDATE User SET first_name=?, last_name=?, address=?, phone=? WHERE user_id=?", (fname, lname, address, phone, user_id))
  Constants.query("UPDATE SeasonTicket SET address=?, phone_number=? WHERE season_ticket_id=?", (address, phone, season_ticket_id))
