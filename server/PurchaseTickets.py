"""
@Author Aidan lear

This file deals with the backend stuff for purchasing tickets
"""
import json
import pickle

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
side_orc_rows = [6,7,7,6,6,6,6,5,5,5,5,5,5,4]
main_orc_rows = [8,9,10,11,11,12,12,12,12,12,12,12,12,10,9,7]
balc_rows = [24,23,22,23,22,23]



###########################################################################
# read in the json info for seat locations of the playhouse
###########################################################################
def construct_playhouse_info():
    file = open('PlayhouseInfo.json')  # open the file
    data = json.load(file) # read the JSON text into a dictionary
    file.close() # close the file. The contents have already been read into memory.
    seats = data['seats']
    new_data = dict() # place to store the new data


    #construct the main_orch seats
    new_data['main_orch'] = []
    row = 0
    number = 0
    for seat in seats['main_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'main_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= main_orc_rows[row]:
            row += 1
            number = 0
        new_data['main_orch'].append(new_seat)


    #construct the left_orch seats
    new_data['left_orch'] = []
    row = 0
    number = 0
    for seat in seats['left_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'left_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= side_orc_rows[row]:
            row += 1
            number = 0
        new_data['left_orch'].append(new_seat)



    #construct the right_orch seats
    new_data['right_orch'] = []
    row = 0
    number = 0
    for seat in seats['right_orch']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'right_orch'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= side_orc_rows[row]:
            row += 1
            number = 0
        new_data['right_orch'].append(new_seat)


    #construct the balc seats
    new_data['balc'] = []
    row = 0
    number = 0
    for seat in seats['balc']:
        number += 1
        new_seat = dict()
        new_seat['x'] = seat['x']
        new_seat['y'] = seat['y']
        new_seat['sec'] = 'balc'
        new_seat['number'] = number
        new_seat['row'] = alphabet[row]
        #This is for creating the correct row
        if number >= balc_rows[row]:
            row += 1
            number = 0
        new_data['balc'].append(new_seat)




    #construct single row seats
    section_names = ['right_box', 'right_loge', 'left_box', 'left_loge']
    for sec_name in section_names:
        # construct the foyer seats
        new_data[sec_name] = []
        number = 0
        for seat in seats[sec_name]:
            number += 1
            new_seat = dict()
            new_seat['x'] = seat['x']
            new_seat['y'] = seat['y']
            new_seat['sec'] = sec_name
            new_seat['number'] = number
            new_seat['row'] = 'A'
            new_data[sec_name].append(new_seat)
            print(new_seat)



    #write it to a file
    f = open("PlayhouseInfo.pkl", "wb")
    pickle.dump(new_data, f)
    f.close()


def load_playhouse_data():
    file = open('PlayhouseInfo.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    return data












################################
# tests for this file
################################
if __name__ == "__main__":
    some_data = load_playhouse_data()
    for key in some_data:
        print('---' + key + '---')
        for seat in some_data[key]:
            print(seat)
