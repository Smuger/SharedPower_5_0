# import database
from tinydb import *

# import time handler
import time

class f_db:
    # data storage
    userdb = ""
    toolsdb = ""
    rentalsdb = ""
    invoicesdb = ""
    def __init__(self):
        # define database files
        self.userdb = TinyDB("DB/db_users.json")
        self.toolsdb = TinyDB("DB/db_products.json")
        self.rentalsdb = TinyDB("DB/db_rentals.json")
        self.invoicesdb = TinyDB("DB/db_invoices.json")

    # add new user record handler
    def createuser(self, username, email, postcode, address, card_owner, card_number, card_security, card_expiration, password, avatar):
        self.userdb.insert(
            {"id": str(time.time()), 'name': username, 'email': email, 'postcode': postcode, 'address': address, 'card_owner': card_owner, 'card_number': card_number, 'card_security': card_security, 'card_expiration': card_expiration, 'password': password, "avatar": avatar, "balance": 0})

    # is this login available handler
    def checkavaibilityoflogin(self, username):
        User = Query()
        return self.userdb.search((User.name == username))

    # add new product record handler
    def createtool(self, userid, name, price, type, photolist, condition, description, deliveryprices):
        self.toolsdb.insert(
            {"id": str(time.time()), 'userid': userid, 'name': name, 'price': price, 'typeof': type,
             "photos": photolist,
             "condition": condition, "description": description, "delivery": deliveryprices})

    # add rent record handler
    def addrental(self, userid, toolid, startdate, enddate, deliverytype, deliveryprice):
        self.rentalsdb.insert(
            {"id": str(time.time()), 'userid': userid, 'toolid': toolid, 'startdate': startdate, 'enddate': enddate,
             'status': 0, "deliverytype": deliverytype, "deliveryprice": deliveryprice})

    # pass user details handler
    def getuser(self, action, username, password):
        User = Query()
        if (action == "login"):
            # if credentials correct return user name
            return self.userdb.search((User.name == username) & (User.password == password))

    # update balance handler
    def updatebalance(self, userid, price):
        User = Query()
        tempusers = self.userdb.search((User.id == userid))
        tempuser = tempusers[0]
        self.userdb.update({'balance': tempuser["balance"] - price}, User.id == userid)

    # return user details handler
    def getuserdetails(self, userid):
        User = Query()
        return self.userdb.search(User.id == userid)

    # return product handler
    def gettool(self, searchby, query):
        Tool = Query()
        if (searchby == "typeof"):
            return self.toolsdb.search(Tool.typeof == query)
        elif (searchby == "name"):
            return self.toolsdb.search(Tool.name == query)
        elif (searchby == "userid"):
            return self.toolsdb.search(Tool.userid == query)
        elif (searchby == "id"):
            return self.toolsdb.search(Tool.id == query)
        elif (searchby == "condition"):
            return self.toolsdb.search(Tool.condition == query)

    # is product available handler
    def checkavaiblity(self, toolid, startdate, enddate):
        Rental = Query()

        return self.rentalsdb.search(
            Rental.toolid == toolid and (
                    Rental.startdate >= startdate or Rental.startdate <= enddate or Rental.enddate >= enddate or Rental.enddate >= startdate))

    # user rental handler
    def getrentalofuser(self, userid):
        Rental = Query()
        return self.rentalsdb.search((Rental.userid == userid) & (Rental.status == 0))

    # rentals handler
    def getrental(self, rentalid):
        Rental = Query()
        return self.rentalsdb.search(Rental.id == rentalid)

    # invoices handler
    def getinvoices(self, userid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.userid == userid)

    # invoice handler
    def getinvoice(self, invoiceid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.id == invoiceid)[0]

    # specific invoices handler
    def getrelatedinvoces(self, userid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.ownerid == userid)

    # end rental handler
    def finishrental(self, rentalid):
        Rental = Query()
        self.rentalsdb.update({'status': 1}, Rental.id == rentalid)

    # add invoice handler
    def addinvoice(self, userid, itemlist, summaryprice, ownerid, photolist):
        now = time.time()
        self.invoicesdb.insert(
            {"id": str(now), 'userid': userid, 'itemlist': itemlist, 'summaryprice': summaryprice,
             'created': now, "ownerid": ownerid, "photos": photolist})
        return now
