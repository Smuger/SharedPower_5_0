# import functionality
from FUNC.f_db import f_db

class f_users:
    def __init__(self):
        return

    # create account handler
    def create_account(self, username, email, postcode, address, card_owner, card_number, card_security, card_expiration, password, avatar):
        db = f_db()
        db.user_create_db(username, email, postcode, address, card_owner, card_number, card_security, card_expiration, password, avatar)

    # pass user details handler
    def get_user_details(self, userid):
        db = f_db()
        db.getuserdetails(userid)

    # is login correct handler
    def checklogin(self, username):
        db = f_db()
        if (db.login_available_db(username)):
            return False
        return True

    # update balance handler
    def updatebalance(self, userid, price):
        db = f_db()
        db.updatebalance(userid, price)