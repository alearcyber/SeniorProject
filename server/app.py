from flask import Flask, request, url_for, flash, redirect, get_flashed_messages, jsonify
from flask import render_template, send_from_directory
from flask_cors import CORS, cross_origin
import json
import Queries
import Constants
from database.user.sign_up import sign_up_user
from database.user.login import login_user
import PurchaseTickets
from Scheduling import create_new_production
from CreateSeason import get_future_list_of_productions, get_org_name
import SeasonPass
import FrontDesk

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
    result = PurchaseTickets.seating_chart_f(performance_id)
    return result






###########################################
# list of upcoming performances
###########################################
@app.route("/upcoming_performances", methods=['GET'])
def upcoming_performances():
    print('LOG: Received request for upcoming performances')
    data = PurchaseTickets.upcoming_performances()
    out = json.dumps({'data': data}, indent=4)
    #print('THE JSON IS HERE:', out)
    return out






#for the BUY TICKETS page at the top
@app.route("/purchase_tickets", methods=['POST'])
def purchase_tickets():
    data = request.get_json()
    print("Received request for purchasing tickets")
    print("data received:", data)
    #parse out the data
    d = data
    seat_data = d['seat_data']
    email = d['email']
    performance_id = d['performance_id']
    payment_method = d['payment_method']
    #check for 'credit' instead of 'card'
    if payment_method == 'credit':
        payment_method = Constants.Payment.card

    #result = PurchaseTickets.purchase_tickets(data['seats'], data['email'], data['performance_id'], data['payment_method'])
    result = PurchaseTickets.purchase_tickets(seat_data=seat_data, email=email, performance_id=performance_id, payment_method=payment_method)
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
    #print(data)
    result = create_new_production(data['title'], data['venue_id'], 
                                   data['org_id'], data['image'], data['description'], 
                                   data['duration'], data['times'])
    
    # Add section pricing to performances
    for key in data['performances']:
        print("Section prices:", key['section_prices'])

    return json.dumps(result)

@app.route('/get_productions/<email>:<org_id>')
def get_productions(email, org_id):
    result = get_future_list_of_productions(email, org_id)
    org_name = get_org_name(org_id)

    return json.dumps({'production_list': result, 'org_name': org_name})




#used for the user to select a season when they are buying a season pass
#data is used to load the page that presents the available seasons
@app.route('/get_upcoming_seasons')
def get_upcoming_seasons():
    data = SeasonPass.upcoming_seasons()
    out = json.dumps({'seasons':data})
    print(out)
    return out



# retrieves a list of all the performances for a given season
@app.route("/get_season_performances", methods=['POST'])
def get_season_performances():
    title = request.get_json()['title']
    data = SeasonPass.get_all_season_performances(title)
    out = json.dumps({'performances': data})
    print(out)
    return out



#getting the performances for the front desk
@app.route("/frontdesk_upcoming_performances", methods=['POST'])
def frontdesk_performances():
    email = request.get_json()['email']
    data = FrontDesk.upcoming_performances(email)
    out = json.dumps({'performances': data})
    print('Received request from', email, 'for a list of upcoming perforamances for the front desk.')
    print(out)
    return out



#This is for when the front desk is handling any sort of payment
@app.route('/handle_frontdesk_payment', methods=['POST'])
def handle_frontdesk_payment():
    d = request.get_json() #data from the post
    status = FrontDesk.handle_payment(d['performance_id'], d['number'], d['row'], d['section'], d['payment_method'])
    if status:
        print('Handled Payment Successfully')
    else:
        print('somthing went wrong handling the payment')
    return json.dumps({'status': status})


#retreiving seat info foor the front desk person
@app.route('/frontdesk_seat_info', methods=['POST'])
def frontdesk_seat_info():
    d = request.get_json()
    seat_info = FrontDesk.get_seat_info(d['performance_id'], d['number'], d['row'], d['section'])
    return json.dumps({'seat_info': seat_info})



#show tickets eligible to be exchanged
@app.route('/get_my_tickets', methods=['POST'])
def get_my_tickets():
    d = request.get_json()
    email = d['email']
    seats = PurchaseTickets.get_owned_tickets(email)
    return json.dumps({'seats': seats})



#exchange these tickets in the database
@app.route('/free_tickets', methods=['POST'])
def free_tickets():
    d = request.get_json()
    seat_ids = d['seat_ids']
    print('Received request to free up tickets. The session storage variable received is:', seat_ids)
    success = PurchaseTickets.free_tickets(seat_ids)
    return json.dumps({'success': success})



@app.route('/buy_season_ticket', methods=['POST'])
def buy_season_ticket():
    d = request.get_json()
    params = (d['number'],d['row'],d['section'],d['season'],d['email'],d['name'], d['address'])
    q = f"""
    INSERT INTO SeasonTicket (number, row, section, season, email, name, address)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    Constants.query(q, params=params)
    return json.dumps({'success': True})




if __name__ == '__main__':
    app.run()
