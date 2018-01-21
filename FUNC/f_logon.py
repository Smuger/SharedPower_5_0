# import functionality
from FUNC.f_db import f_db

class f_logon:
    # is user loged
    session = False
    userid = 0
    userdetails = ""

    def login(self, username, password):
        db = f_db()
        login = db.getuser("login", username, password)

        # is correct?
        if (login):

            self.session = True
            self.userid = login[0]["id"]
            self.userdetails = login[0]

    def logout(self):
        # close session
        self.session = False