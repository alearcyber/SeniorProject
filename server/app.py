from flask import Flask, request, url_for, flash, redirect, get_flashed_messages, jsonify
from flask import render_template, send_from_directory
from flask_cors import CORS, cross_origin
import json
import Queries
from database.user.sign_up import sign_up_user
from database.user.login import login_user
import PurchaseTickets

app = Flask(__name__, template_folder='templates', static_folder='templates')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
app.secret_key = 'test'

"""
###########################################
# this is for viewing the test venue
###########################################
@app.route("/testvenue")
def test_venue():
    return render_template("SeatsGrid.html")

"""
"""
############################
# Add a new venue
############################
@app.route("/addvenue", methods=['POST', 'GET'])
def add_venue():

    # Check to see if a venue was submitted
    if request.method == 'POST':
        name = request.form['name']
        rows = request.form['rows']
        cols = request.form['cols']
        DataConnector.add_venue(1, name, rows, cols)
        flash(f'New Venue Created, name:{name}, rows:{rows}, columns:{cols}')
        print(f'New Venue Created, name:{name}, rows:{rows}, columns:{cols}')



    #render the template
    return render_template("AddVenue.html")

"""

############################
# Upcoming Performances
############################
@app.route("/upcomingperformances", methods=['GET'])
def add_venue():
    print('DEBUG: received request to see upcoming performances.')
    #out = jsonify(Queries.get_shows())
    new_stuff = {"shows": Queries.get_shows()}
    out = json.dumps(new_stuff, indent=4)
    print(out)
    return out



############################
# LOGIN
# This API receives the login information. Will send back a valid or invalid login. Will also send
# some token to keep in the session variables for that user if the login is valid.
############################
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        user_input = request.get_json()
        result = login_user(user_input["email"], user_input["password"])

    #TODO write login stuff here
    return json.dumps(result, indent=4);

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_data = request.get_json()
        result = sign_up_user(user_data['email'],
                     user_data['fname'],
                     user_data['lname'],
                     user_data['password'],
                     user_data['venue_id'])

    return json.dumps(result, indent=4)





###########################################
# Get the seating chart for a performance
# expected request body:
#   {performance_id: n}
###########################################
@app.route("/get_seating_chart", methods=['POST'])
def seating_chart():
    data = request.get_json()
    performance_id = data['performance_id']
    print("Received request for seating data for peformance of id", performance_id)
    result = PurchaseTickets.get_seating_chart(performance_id)
    return result



###########################################
# list of upcoming performances
###########################################
@app.route("/upcoming_performances", methods=['GET'])
def upcoming_performances():
    print('LOG: Received request for upcoming performances')
    data = PurchaseTickets.upcoming_performances()
    out = json.dumps({'data':data}, indent=4)
    print('THE JSON IS HERE:', out)
    return out






#for the BUY TICKETS page at the top




if __name__ == '__main__':
    app.run()
