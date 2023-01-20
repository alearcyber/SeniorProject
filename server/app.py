import DataConnector
from flask import Flask, request, url_for, flash, redirect, get_flashed_messages
from flask import render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='templates')
app.secret_key = 'test'

###########################################
# this is for viewing the test venue
###########################################
@app.route("/testvenue")
def test_venue():
    return render_template("SeatsGrid.html")



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

if __name__ == '__main__':
    app.run()
