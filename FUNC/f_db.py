from tinydb import *
import time


class f_db:
    userdb = ""
    toolsdb = ""
    rentalsdb = ""
    invoicesdb = ""

    # init DataBaseController and attach basic databases
    def __init__(self):
        # user database
        self.userdb = TinyDB("DB/db_users.json")
        # tool database
        self.toolsdb = TinyDB("DB/db_products.json")
        # rental database
        self.rentalsdb = TinyDB("DB/db_rentals.json")
        # invoice database
        self.invoicesdb = TinyDB("DB/db_invoices.json")

    # create user with username, password, avatar, balance =0 and save to database
    def createuser(self, username, password, avatar):
        self.userdb.insert(
            {"id": str(time.time()), 'name': username, 'password': password, "avatar": avatar, "balance": 0})

    # check if exists any user with username
    def checkavaibilityoflogin(self, username):
        # basic tinydbquery
        User = Query()
        return self.userdb.search((User.name == username))

    # create tool with userid of owner, name, price, type, photolist, condition, description
    def createtool(self, userid, name, price, type, photolist, condition, description, deliveryprices):
        self.toolsdb.insert(
            {"id": str(time.time()), 'userid': userid, 'name': name, 'price': price, 'typeof': type,
             "photos": photolist,
             "condition": condition, "description": description, "delivery": deliveryprices})

    # add rental using userid, toolid, start date, end date
    def addrental(self, userid, toolid, startdate, enddate, deliverytype, deliveryprice):
        self.rentalsdb.insert(
            {"id": str(time.time()), 'userid': userid, 'toolid': toolid, 'startdate': startdate, 'enddate': enddate,
             'status': 0, "deliverytype": deliverytype, "deliveryprice": deliveryprice})

    # get user by action from database
    def getuser(self, action, username, password):
        # basic tinydbquery
        User = Query()
        # Login action
        if (action == "login"):
            # return user if password and login are corrected
            return self.userdb.search((User.name == username) & (User.password == password))

    # update balance of user who rent and owner of tool
    def updatebalance(self, userid, price):
        User = Query()
        tempusers = self.userdb.search((User.id == userid))
        tempuser = tempusers[0]
        self.userdb.update({'balance': tempuser["balance"] - price}, User.id == userid)

    # get user details by userid
    def getuserdetails(self, userid):
        # basic tinydbquery
        User = Query()
        # return user object
        return self.userdb.search(User.id == userid)

    # get tool by searchby
    def gettool(self, searchby, query):
        # basic tinydbquery
        Tool = Query()
        # check type of search and return toollist
        if (searchby == "typeof"):

            return self.toolsdb.search(Tool.typeof == query)
        elif (searchby == "name"):
            return self.toolsdb.search(Tool.name == query)
        elif (searchby == "userid"):
            return self.toolsdb.search(Tool.userid == query)
        elif (searchby == "id"):
            return self.toolsdb.search(Tool.id == query)

    # check if exist any rent in period of time
    def checkavaiblity(self, toolid, startdate, enddate):
        # basic tinydbquery
        Rental = Query()
        # return all rentals in that time

        return self.rentalsdb.search(
            Rental.toolid == toolid and (
                    Rental.startdate >= startdate or Rental.startdate <= enddate or Rental.enddate >= enddate or Rental.enddate >= startdate))

    # get all user rentals by id
    def getrentalofuser(self, userid):
        # basic tinydbquery
        Rental = Query()
        # return all user rentals
        return self.rentalsdb.search((Rental.userid == userid) & (Rental.status == 0))

    # get rental details
    def getrental(self, rentalid):
        # basic tinydbquery
        Rental = Query()
        # return rental object
        return self.rentalsdb.search(Rental.id == rentalid)

    # list all invoices of user
    def getinvoices(self, userid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.userid == userid)

    # get invoice details
    def getinvoice(self, invoiceid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.id == invoiceid)[0]

    # list all invoices of owner of tool
    def getrelatedinvoces(self, userid):
        Invoices = Query()
        return self.invoicesdb.search(Invoices.ownerid == userid)

    # update status of rental
    def finishrental(self, rentalid):
        Rental = Query()

        self.rentalsdb.update({'status': 1}, Rental.id == rentalid)

    # add invoice to db
    def addinvoice(self, userid, itemlist, summaryprice, ownerid, photolist):
        now = time.time()
        self.invoicesdb.insert(
            {"id": str(now), 'userid': userid, 'itemlist': itemlist, 'summaryprice': summaryprice,
             'created': now, "ownerid": ownerid, "photos": photolist})
        return now
