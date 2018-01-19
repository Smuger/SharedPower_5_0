from Controllers.DataBase import DataBaseController


class LoginController:
    # login status
    session = False
    # id of user after login
    userid = 0
    # details of user after login
    userdetails = ""

    # user login
    def login(self, username, password):
        db = DataBaseController()
        # search user by combination of username and password
        login = db.getuser("login", username, password)
        # check status
        if (login):
            # set login status to true
            self.session = True
            # insert userid
            self.userid = login[0]["id"]
            # insert user details
            self.userdetails = login[0]

    # user logout
    def logout(self):
        # set login status to false
        self.session = False