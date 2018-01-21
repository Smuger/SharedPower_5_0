# import tkinter
from tkinter import *
from tkinter.ttk import *

# import time handler
from datetime import timedelta, datetime

# import page
from PAGES.p_result import p_result

# import functionality
from FUNC.f_rental import f_rental
from FUNC.f_userd import f_userd

# import modify lib
from LIBS.ttkcalendar import *

class p_new_rental(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # import page
        from PAGES.p_start import p_start

        # import functionality
        from FUNC.f_products import f_products

        # set controller, rental, tool and delivery
        self.controller = controller
        self.rental = f_rental()
        self.tool = f_products()
        self.delivery = {}

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_result)).pack(pady=10, padx=10)

        # is available
        Label(self, text="Choose date", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # calendar start
        Label(self, text="Start", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.stardate = Calendar(self, firstweekday=calendar.SUNDAY)
        self.stardate.pack()

        # calendar end
        Label(self, text="End", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.enddate = Calendar(self, firstweekday=calendar.SUNDAY)
        self.enddate.pack()

        # is available
        Button(self, text="Check Avaiblity", command=self.checkavaiblity).pack()

        # space of error
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()

        # choose delivery method
        Label(self, text="Delivery Method:", font=f_userd.LARGE_FONT).pack()

        # combobox
        self.Combobox = Combobox(self, state=DISABLED)
        self.Combobox.pack()
        self.rent = Button(self, text="Rent", state=DISABLED, command=self.rent)
        self.rent.pack()

        # choose theme clam
        if 'win' not in sys.platform:
            style = ttk.Style()
            style.theme_use('clam')

    def rent(self):

        # import page
        from PAGES.p_my_products import p_my_products

        # is start date before end date
        if (self.stardate.selection > self.enddate.selection):
            self.errors['text'] = "End day is before start day"
            return

        # is product available at this time
        if (self.rental.check_availability(self.controller.selectedtoolid, self.stardate.selection,
                                           self.enddate.selection)):
            self.controller.deliverytype=str(self.Combobox.get())
            self.controller.deliveryprice = self.delivery[str(self.Combobox.get())]
            self.rental.add_rental(self.controller.session.userid, self.controller.selectedtoolid,
                                   self.stardate.selection, self.enddate.selection,  self.controller.deliverytype, self.controller.deliveryprice)
            self.controller.show_frame(p_my_products)
        else:
            self.errors['text'] = "Product unavailable"

    # is available
    def checkavaiblity(self):

        # is start date before end date
        self.errors['text'] = ""
        if (self.stardate.selection > self.enddate.selection):
            self.errors['text'] = "End day is before start day"
            return
        elif self.enddate.selection - self.stardate.selection > timedelta(days=3):
            if int(self.controller.price) <= 0:
                self.errors['text'] = "Renting couldn't be longer than 3 days"
                return
        elif (self.stardate.selection <= datetime.now()):
            self.errors['text'] = "Start Date has to be in future"
            return

        # is product available at this time
        if self.rental.check_availability(self.controller.selectedtoolid, self.stardate.selection,
                                          self.enddate.selection):
            tool = self.tool.gettoolbyid(self.controller.selectedtoolid)

            # choose delivery
            deliverylist=["No delivery"]
            if tool["delivery"]:
                self.delivery=tool["delivery"]
                for delivery,price in tool["delivery"].items():
                    deliverylist.append(delivery)
                self.Combobox.config(state=NORMAL)
            self.Combobox['values'] = deliverylist
            self.rent.config(state=NORMAL)
            self.delivery["No delivery"] = 0
        else:
            self.errors['text'] = "Product unavailable"
    # cleanup
    def run(self):
        self.controller.deliverytype = ""
        self.controller.deliveryprice = 0
