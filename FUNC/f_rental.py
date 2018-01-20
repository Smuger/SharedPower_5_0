import time

from FUNC.f_db import f_db
from FUNC.f_users import f_users


class f_rental:
    # check avaiilability of tool in date range
    def check_availability(self, toolid, startdate, enddate):
        db = f_db()
        # check in database
        if db.checkavaiblity(toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple())):
            return False
        return True

    # add rental
    def add_rental(self, userid, toolid, startdate, enddate, deliverytype, deliveryprice):
        db = f_db()
        db.addrental(userid, toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple()), deliverytype,
                     deliveryprice)

    # list all rented tools
    def my_rented_tools(self, userid):
        db = f_db()
        return db.getrentalofuser(userid)

    # show rental details
    def get_rental(self, rentalid):
        db = f_db()
        return db.getrental(rentalid)[0]

    # finish rental
    def finish_rental(self, rentalid, price, userid, ownerid):
        user = f_users()
        # update balance of user
        user.updatebalance(userid, price)
        # update balance of owner of tool
        user.updatebalance(ownerid, -price)
        db = f_db()
        # return of invoice id
        return db.finishrental(rentalid)