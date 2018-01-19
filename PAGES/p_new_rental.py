from datetime import timedelta, datetime
from tkinter import *
from tkinter.ttk import *

from Controllers.Rental import RentalController
from Controllers.Setting import SettingsController
from Frames.result import ResultPage

from Libs.ttkcalendar import *


class RentalPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        from Frames.main import MainPage
        from Controllers.Tools import ToolController
        self.controller = controller
        self.rental = RentalController()
        self.tool = ToolController()
        self.delivery={}
        Frame.__init__(self, parent)
        self.controller = controller
        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: self.controller.show_frame(ResultPage)).pack(pady=10, padx=10)
        Label(self, text="Check Avaiblity", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        Label(self, text="Start Date", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        self.stardate = Calendar(self, firstweekday=calendar.SUNDAY)
        self.stardate.pack()
        Label(self, text="End Date", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        self.enddate = Calendar(self, firstweekday=calendar.SUNDAY)
        self.enddate.pack()
        Button(self, text="Check Avaiblity", command=self.checkavaiblity).pack()
        self.errors = Label(self, text="", font=SettingsController.SMALL_FONT)
        self.errors.pack()
        Label(self, text="Delivery Method:", font=SettingsController.LARGE_FONT).pack()
        self.Combobox = Combobox(self,
                                  state=DISABLED)
        self.Combobox.pack()
        self.rent = Button(self, text="Rent",
                           state=DISABLED, command=self.rent)
        self.rent.pack()
        if 'win' not in sys.platform:
            style = ttk.Style()
            style.theme_use('clam')

    def rent(self):
        from Frames.success import SuccessPage
        if (self.stardate.selection > self.enddate.selection):
            self.errors['text'] = "StartDate has to be before enddate"
            return
        if (self.rental.check_availability(self.controller.selectedtoolid, self.stardate.selection,
                                           self.enddate.selection)):
            self.controller.deliverytype=str(self.Combobox.get())
            self.controller.deliveryprice = self.delivery[str(self.Combobox.get())]
            self.rental.add_rental(self.controller.session.userid, self.controller.selectedtoolid,
                                   self.stardate.selection, self.enddate.selection,  self.controller.deliverytype, self.controller.deliveryprice)
            self.controller.show_frame(SuccessPage)
        else:
            self.errors['text'] = "Sorry Tool is unavailable in that time"

    def checkavaiblity(self):
        print(self.controller.price)
        self.errors['text'] = ""
        print(self.enddate.selection - self.stardate.selection )
        print(timedelta(days=3))
        if (self.stardate.selection > self.enddate.selection):
            self.errors['text'] = "StartDate has to be before enddate"
            return
        elif self.enddate.selection - self.stardate.selection > timedelta(days=3):
            print("test")
            if int(self.controller.price) <= 0:
                self.errors['text'] = "Renting couldn't be longer than 3 days"
                return
        elif (self.stardate.selection <= datetime.now()):
            self.errors['text'] = "Start Date has to be in future"
            return
        if self.rental.check_availability(self.controller.selectedtoolid, self.stardate.selection,
                                          self.enddate.selection):
            tool = self.tool.gettoolbyid(self.controller.selectedtoolid)
            print(tool)

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
            self.errors['text'] = "Sorry Tool is unavailable in that time"

    def run(self):
        self.controller.deliverytype = ""
        self.controller.deliveryprice = 0
