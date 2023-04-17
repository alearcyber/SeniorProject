from flask import Flask, request, url_for, flash, redirect, get_flashed_messages, jsonify
from flask import render_template, send_from_directory
from flask_cors import CORS, cross_origin
import json
import Queries
import Constants
from database.user.sign_up import sign_up_user
from database.user.login import login_user
from Scheduling import create_new_production
from CreateSeason import get_future_list_of_productions, get_org_name

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
    # out = jsonify(Queries.get_shows())
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

    # TODO write login stuff here
    return json.dumps(result, indent=4)


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


@app.route("/is_volunteer", methods=['GET', 'POST'])
def is_volunteer():
    # Query to run:
    query_text = "SELECT Volunteer.org_id FROM User JOIN Volunteer ON User.user_id=Volunteer.user_id WHERE email=?"
    data = request.get_json()
    email = data['email']
    result = Constants.query(query_text, (email,))

    if len(result) > 0:
        org_id = result[0][0]
    else:
        org_id = ""

    return json.dumps({'org_id': org_id})

@app.route("/create_production", methods=['GET', 'POST'])
def create_production():
    data = request.get_json()
    print(data)
    result = create_new_production(data['title'], data['venue_id'], 
                                   data['org_id'], data['image'], data['description'], 
                                   data['duration'], data['times'])
    return json.dumps(result)

@app.route('/get_productions/<email>:<org_id>')
def get_productions(email, org_id):
    result = get_future_list_of_productions(email, org_id)
    org_name = get_org_name(org_id)

    return json.dumps({'production_list': result, 'org_name': org_name})

# @app.route('/create_season')
# def get_productions(email, org_id):
#     pass

if __name__ == '__main__':
    app.run()
