import time

from Controllers.DataBase import DataBaseController
from Controllers.User import UserController


class RentalController:
    # check avaiilability of tool in date range
    def check_availability(self, toolid, startdate, enddate):
        db = DataBaseController()
        # check in database
        if db.checkavaiblity(toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple())):
            return False
        return True

    # add rental
    def add_rental(self, userid, toolid, startdate, enddate, deliverytype, deliveryprice):
        db = DataBaseController()
        db.addrental(userid, toolid, time.mktime(startdate.timetuple()), time.mktime(enddate.timetuple()), deliverytype,
                     deliveryprice)

    # list all rented tools
    def my_rented_tools(self, userid):
        db = DataBaseController()
        return db.getrentalofuser(userid)

    # show rental details
    def get_rental(self, rentalid):
        db = DataBaseController()
        return db.getrental(rentalid)[0]

    # finish rental
    def finish_rental(self, rentalid, price, userid, ownerid):
        user = UserController()
        # update balance of user
        user.updatebalance(userid, price)
        # update balance of owner of tool
        user.updatebalance(ownerid, -price)
        db = DataBaseController()
        # return of invoice id
        return db.finishrental(rentalid)