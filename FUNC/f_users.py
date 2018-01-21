from FUNC.f_db import f_db


class f_users:
    def __init__(self):
        return

    def create_account(self, username, email, postcode, address, card_owner, card_number, card_security, card_expiration, password, avatar):
        db = f_db()
        db.createuser(username, email, postcode, address, card_owner, card_number, card_security, card_expiration, password, avatar)

    def get_user_details(self, userid):
        db = f_db()
        db.getuserdetails(userid)

    def checklogin(self, username):
        db = f_db()
        if (db.checkavaibilityoflogin(username)):
            return False
        return True

    def updatebalance(self, userid, price):
        db = f_db()
        db.updatebalance(userid, price)