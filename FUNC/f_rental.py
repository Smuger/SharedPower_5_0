# import time lib
import time

# import functionality
from FUNC.f_db import f_db
from FUNC.f_users import f_users

class f_rental:
    # product availabiliy handler
    def check_availability(self, toolid, startdate, enddate):
        db = f_db()
        # check in database
        if db.checkavaiblity(toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple())):
            return False
        return True

    # rental handler
    def add_rental(self, userid, toolid, startdate, enddate, deliverytype, deliveryprice):
        db = f_db()
        db.addrental(userid, toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple()), deliverytype,
                     deliveryprice)

    # pass rental data for user handler
    def my_rented_tools(self, userid):
        db = f_db()
        return db.getrentalofuser(userid)

    # pass rental
    def get_rental(self, rentalid):
        db = f_db()
        return db.getrental(rentalid)[0]

    # end rental
    def finish_rental(self, rentalid, price, userid, ownerid):
        user = f_users()
        user.updatebalance(userid, price)
        user.updatebalance(ownerid, -price)
        db = f_db()
        return db.finishrental(rentalid)