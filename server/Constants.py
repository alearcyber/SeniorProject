"""
@Author Aidan Lear
This file contains constants to be used for the backend
"""


#Path to the database
DB_PATH = 'database.db'






############################################
# Enum for the possible payment types
############################################
class Payment():
    card = 'card'
    cash = 'cash'
    check = 'check'
    none = None
    all = {'card', 'cash', 'check', None}

