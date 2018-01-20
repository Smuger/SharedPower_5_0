from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

import time

import datetime

from FUNC.f_userd import f_userd
from FUNC.f_users import f_users
from PAGES.p_invoice import p_invoice


class p_end_rental(Frame):
    #basic variables
    rentalitem = ""
    rentsum = 0
    dayfee = 0
    insurance = 5
    pricetotal = 0
    itemlist = []
    ownerid = 0
    photolist = []
    #init FinishRentalPage frame
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #Basic imports
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result
        from FUNC.f_userd import f_userd
        from FUNC.f_products import f_products
        from FUNC.f_rental import f_rental
        #Setting basisc properties with controllers
        self.controller = controller
        self.tool = f_products()
        self.rental = f_rental()
        self.controller = controller
        #inserting gui elements
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()
        topic = Label(self, text="Return Tool", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        back = Button(self, text="Back", command=lambda: self.controller.show_frame(p_result)).pack(pady=10, padx=10)
        Label(self, text="Payment List:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)
        Label(self, text="Additional Info:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.addinfo = Label(self, text="", font=f_userd.LARGE_FONT)
        self.addinfo.pack(pady=10, padx=10)
        Label(self, text="Photos:", font=f_userd.LARGE_FONT).pack()

        Button(self, text='Browse', command=self.addphototools).pack()
        Label(self, text="Price", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.price = Label(self, text="", font=f_userd.LARGE_FONT)
        self.price.pack(pady=10, padx=10)
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()
        self.confirm =Button(self, text="Confirm", command=self.finishrental,state=DISABLED)
        self.confirm.pack()
    #connecting with logic and checking data
    def finishrental(self):
        #check if added photo
        if (self.photolist):
            #finishing rental
            self.rental.finish_rental(self.controller.selectrental, self.pricetotal, self.controller.session.userid,
                                      self.ownerid)
            id = self.invoices.add_invoce(self.controller.session.userid, self.itemlist, self.pricetotal,
                                          self.ownerid, self.photolist)
            #inserting nr of invoice
            self.controller.selectedinvoice = "invoice" + id
            self.controller.selectedinvoiceid = id
            self.controller.show_frame(p_invoice)
        else:
            self.errors['text'] = "Add photos is required"
    #uploading photo of tools
    def addphototools(self):
        from FUNC.f_file import f_file
        file = f_file()
        self.photolist = file.uploadphotos()
        print(self.photolist)
    #basic configuration of frame before display
    def run(self):
        from FUNC.f_invoice import f_invoice
        self.invoices = f_invoice()
        self.rentalitem = self.rental.get_rental(self.controller.selectrental)
        tool = self.tool.gettoolbyid(self.rentalitem["toolid"])
        self.ownerid = tool["userid"]
        dayfee = int(tool["price"])
        #get now time
        now = time.time()
        #validation of dates
        if datetime.datetime.utcfromtimestamp(now) - datetime.datetime.utcfromtimestamp( self.rentalitem["startdate"]) < datetime.timedelta(days=0):
            print(now)
            self.addinfo.config(
                text="You cannot finish rental before end date")
        else:
            self.confirm.config(state=NORMAL)
        #checking if we finish rental after enddate

        if now -  self.rentalitem["enddate"] >0:
            self.addinfo.config(
                text="Your payment is multiply 2 times, because you should finish renting before end date")
            dayfee = int(dayfee) * 2
        Label(self.frame, text=tool["name"]).pack(pady=10, padx=10)
        days = datetime.datetime.utcfromtimestamp(now) - datetime.datetime.utcfromtimestamp(
            self.rentalitem["startdate"])
        productprice = dayfee * int(days.days)
        self.itemlist = [tool["name"] + " Price:" + str(productprice), "Insurance Price:" + str(self.insurance),
                         self.rentalitem["deliverytype"] + " Price: " + str(self.rentalitem["deliveryprice"])]

        Label(self.frame, text='      Price:' + str(productprice),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        Label(self.frame, text=self.rentalitem["deliverytype"],
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        Label(self.frame, text= "Price :" + str(self.rentalitem["deliveryprice"]),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        Label(self.frame, text="Insurance").pack(pady=10, padx=10)
        Label(self.frame, text="              Price:" + str(self.insurance),
              font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        price = int(productprice) + self.insurance + int(self.rentalitem["deliveryprice"])

        self.price.config(
            text="Total:" + str(price))
        self.pricetotal = price
