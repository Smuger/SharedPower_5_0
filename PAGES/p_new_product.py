from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from Controllers.Tools import ToolController
from shutil import copy2

from Controllers.Setting import SettingsController


# Add toll Page frame
class AddPage(Frame):
    # basic properties
    photolist = []
    deliverymethod = []
    deliveryprices = {}

    # init of frame
    def __init__(self, parent, controller):
        # basic import for frame
        from Frames.main import MainPage
        from Frames.search import SearchPage
        from Frames.success import SuccessPage
        from Controllers.Setting import SettingsController

        Frame.__init__(self, parent)
        self.controller = controller
        # logout

        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack(pady=10, padx=10)

        # topic
        Label(self, text="Add tool", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # DATA
        Label(self, text="Name:", font=SettingsController.SMALL_FONT).pack()
        self.name = Entry(self, textvariable=SettingsController.NAME)
        self.name.pack()
        Label(self, text="Type:", font=SettingsController.SMALL_FONT).pack()
        self.type = Entry(self, textvariable=SettingsController.TYPE)
        self.type.pack()

        Label(self, text="Condition:", font=SettingsController.LARGE_FONT).pack()
        self.condition = Combobox(self)
        self.condition.pack()
        # add pic
        Label(self, text="Photo:", font=SettingsController.LARGE_FONT).pack()

        Button(self, text='Browse', command=self.addphototools).pack()
        # add PIC

        Label(self, text="Describe product:", font=SettingsController.LARGE_FONT).pack()
        self.description = Entry(self, textvariable=SettingsController.DESCRIPTION)
        self.description.pack()

        Label(self, text="Price in £", font=SettingsController.LARGE_FONT).pack()

        Label(self, text="Per day:", font=SettingsController.SMALL_FONT).pack()
        self.priceperday = Entry(self, textvariable=SettingsController.PRICE_DAY)
        self.priceperday.pack()
        Label(self, text="Delivery method:", font=SettingsController.SMALL_FONT).pack()

        self.pick = Checkbutton(self, text="Delivery with return", variable="Delivery with return",
                                command=self.delivery)
        self.pick.pack()
        Label(self, text="Delivery price:", font=SettingsController.SMALL_FONT).pack()

        self.pickprice = Entry(self, textvariable=SettingsController.DESCRIPTION)
        self.pickprice.pack()
        self.delivery = Checkbutton(self, text="One way delivery", variable="delivery", command=self.deliverywithreturn)
        self.delivery.pack()
        Label(self, text="Delivery price:", font=SettingsController.SMALL_FONT).pack()

        self.deliveryprice = Entry(self, textvariable=SettingsController.DESCRIPTION)
        self.deliveryprice.pack()

        # DATA
        Button(self, text="Add tool", command=self.savetool).pack(pady=10, padx=10)
        self.delivery.setvar()
    # delivery methods
    def delivery(self):
        if ("One way Delivery" in self.deliverymethod):
            self.deliverymethod.remove("One way Delivery")
            del self.deliveryprices["One way Delivery"]
        else:
            self.deliverymethod.append("One way Delivery")
            self.deliveryprices["One way Delivery"] = self.pickprice.get()

    # delivery methods
    def deliverywithreturn(self):
        if ("Delivery with return" in self.deliverymethod):

            self.deliverymethod.remove("Delivery with return")
            del self.deliveryprices["Delivery with return"]
        else:
            self.deliverymethod.append("Delivery with return")
            self.deliveryprices["Delivery with return"] = self.deliveryprice.get()

    # run photo upload
    def addphototools(self):
        from Controllers.File import FileController
        file = FileController()
        self.photolist = file.uploadphotos()

    # save tool
    def savetool(self):
        from Frames.success import SuccessPage
        tools = ToolController()
        tools.add_tool(self.controller.session.userid, self.name.get(), self.priceperday.get(), self.type.get(),
                       self.photolist, self.condition.get(), self.description.get(), self.deliveryprices)
        self.controller.show_frame(SuccessPage)

    # basic action before show frame
    def run(self):
        pass
