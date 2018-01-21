# import tkinter
from tkinter import *
from tkinter.ttk import *

# import time handler
import time
import datetime

# import page
from PAGES.p_invoice import p_invoice

# import functionality
from FUNC.f_userd import f_userd

class p_end_rental(Frame):
    # data storage
    rentalitem = ""
    rentsum = 0
    dayfee = 0
    insurance = 5
    pricetotal = 0
    itemlist = []
    ownerid = 0
    photolist = []

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # import pages
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result

        # import functionality
        from FUNC.f_userd import f_userd
        from FUNC.f_products import f_products
        from FUNC.f_rental import f_rental

        # define controller, tool, rental
        self.controller = controller
        self.tool = f_products()
        self.rental = f_rental()

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # return tool
        Label(self, text="Return Tool", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # back
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_result)).pack(pady=10, padx=10)

        # payment list
        Label(self, text="Payment List:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # target frame
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        # details
        Label(self, text="Additional Info:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.addinfo = Label(self, text="", font=f_userd.LARGE_FONT)
        self.addinfo.pack(pady=10, padx=10)

        # photos
        Label(self, text="Photos:", font=f_userd.LARGE_FONT).pack()
        Button(self, text='Browse', command=self.addphototools).pack()

        # price
        Label(self, text="Price", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.price = Label(self, text="", font=f_userd.LARGE_FONT)
        self.price.pack(pady=10, padx=10)

        # error place
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()

        # confirm data
        self.confirm = Button(self, text="Confirm", command=self.finishrental,state=DISABLED)
        self.confirm.pack()

    def finishrental(self):
        # photo validation
        if (self.photolist):
            self.rental.finish_rental(self.controller.selectrental, self.pricetotal, self.controller.session.userid,
                                      self.ownerid)
            id = self.invoices.add_invoce(self.controller.session.userid, self.itemlist, self.pricetotal,
                                          self.ownerid, self.photolist)
            # populate
            self.controller.selectedinvoice = "invoice" + id
            self.controller.selectedinvoiceid = id
            self.controller.show_frame(p_invoice)
        else:
            self.errors['text'] = "Add photos is required"

    def addphototools(self):
        # import functionality
        from FUNC.f_file import f_file

        file = f_file()
        self.photolist = file.uploadphotos()

    def run(self):
        # import functionality
        from FUNC.f_invoice import f_invoice

        self.invoices = f_invoice()
        self.rentalitem = self.rental.get_rental(self.controller.selectrental)
        tool = self.tool.gettoolbyid(self.rentalitem["toolid"])
        self.ownerid = tool["userid"]
        dayfee = int(tool["price"])
        now = time.time()

        # is date before end date
        if datetime.datetime.utcfromtimestamp(now) - datetime.datetime.utcfromtimestamp( self.rentalitem["startdate"]) < datetime.timedelta(days=0):
            print(now)
            self.addinfo.config(
                text="You can not return tool early")
        else:
            self.confirm.config(state=NORMAL)

        # is date after finish date
        if now -  self.rentalitem["enddate"] >0:
            self.addinfo.config(
                text="You action is late, payment will be multiply two times")
            dayfee = int(dayfee) * 2

        # name of product
        Label(self.frame, text=tool["name"]).pack(pady=10, padx=10)

        # start date
        days = datetime.datetime.utcfromtimestamp(now) - datetime.datetime.utcfromtimestamp(
            self.rentalitem["startdate"])

        # finish price
        productprice = dayfee * int(days.days)

        # item data
        self.itemlist = [tool["name"] + " Price:" + str(productprice), "Insurance Price:" + str(self.insurance),
                         self.rentalitem["deliverytype"] + " Price: " + str(self.rentalitem["deliveryprice"])]

        # price
        Label(self.frame, text='      Price:' + str(productprice),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        # delivery
        Label(self.frame, text=self.rentalitem["deliverytype"],
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        Label(self.frame, text= "Price :" + str(self.rentalitem["deliveryprice"]),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # insurance
        Label(self.frame, text="Insurance").pack(pady=10, padx=10)
        Label(self.frame, text="              Price:" + str(self.insurance),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        price = int(productprice) + self.insurance + int(self.rentalitem["deliveryprice"])

        # send
        self.price.config(
            text="Total:" + str(price))
        self.pricetotal = price
