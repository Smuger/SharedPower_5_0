from Controllers.DataBase import DataBaseController


class UserController:
    def __init__(self):
        return

    def create_account(self, username, password, avatar):
        db = DataBaseController()
        db.createuser(username, password, avatar)

    def get_user_details(self, userid):
        db = DataBaseController()
        db.getuserdetails(userid)

    def checklogin(self, username):
        db = DataBaseController()
        if (db.checkavaibilityoflogin(username)):
            return False
        return True

    def updatebalance(self, userid, price):
        db = DataBaseController()
        db.updatebalance(userid, price)