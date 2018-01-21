# import tkinter
from tkinter import *
from tkinter.ttk import *

# import functionality
from FUNC.f_products import f_products

class p_new_product(Frame):
    # storage
    photolist = []
    deliverymethod = []
    deliveryprices = {}
    def __init__(self, parent, controller):

        # import pages
        from PAGES.p_start import p_start
        from PAGES.p_search import p_search

        # import functionality
        from FUNC.f_userd import f_userd
        Frame.__init__(self, parent)

        # define controller
        self.controller = controller

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_search)).pack(pady=10, padx=10)

        Label(self, text="Add tool", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # product name
        Label(self, text="Name:", font=f_userd.SMALL_FONT).pack()
        self.name = Entry(self, textvariable=f_userd.NAME)
        self.name.pack()

        # product type
        Label(self, text="Type:", font=f_userd.SMALL_FONT).pack()
        self.type = Entry(self, textvariable=f_userd.TYPE)
        self.type.pack()

        # product condition
        Label(self, text="Condition:", font=f_userd.LARGE_FONT).pack()
        self.condition = Combobox(self, values=f_userd.CONDITION_LIST, textvariable=f_userd.CONDITION)
        self.condition.pack()

        # product picture
        Label(self, text="Photo:", font=f_userd.LARGE_FONT).pack()
        Button(self, text='Browse', command=self.addphototools).pack()
        self.path = Label(self, text="", font=f_userd.SMALL_FONT)
        self.path.pack()

        # product description
        Label(self, text="Describe product:", font=f_userd.LARGE_FONT).pack()
        self.description = Entry(self, textvariable=f_userd.DESCRIPTION)
        self.description.pack()

        # prices
        Label(self, text="Price in £", font=f_userd.LARGE_FONT).pack()

        # price per day
        Label(self, text="Per day:", font=f_userd.SMALL_FONT).pack()
        self.priceperday = Entry(self, textvariable=f_userd.PRICE_DAY)
        self.priceperday.pack()

        # prices per hour
        Label(self, text="Per hour:", font=f_userd.SMALL_FONT).pack()
        self.priceperhour = Entry(self, textvariable=f_userd.PRICE_HOUR)
        self.priceperhour.pack()

        # choose delivery
        Label(self, text="Delivery method:", font=f_userd.LARGE_FONT).pack()
        self.pick = Checkbutton(self, text="Delivery with return", variable="Delivery with return", command=self.delivery)
        self.pick.pack()

        # prices for delivery
        Label(self, text="Delivery price:", font=f_userd.SMALL_FONT).pack()
        self.pickprice = Entry(self, textvariable=f_userd.DESCRIPTION)
        self.pickprice.pack()

        # do you want this delivery
        self.delivery = Checkbutton(self, text="One way delivery", variable="delivery", command=self.deliverywithreturn)
        self.delivery.pack()

        # delivery prices
        Label(self, text="Delivery price:", font=f_userd.SMALL_FONT).pack()
        self.deliveryprice = Entry(self, textvariable=f_userd.DESCRIPTION)
        self.deliveryprice.pack()

        # add tool
        Button(self, text="Add tool", command=self.savetool).pack(pady=10, padx=10)
        self.delivery.setvar()

    # choose delivery
    def delivery(self):
        if ("One way Delivery" in self.deliverymethod):
            self.deliverymethod.remove("One way Delivery")
            del self.deliveryprices["One way Delivery"]
        else:
            self.deliverymethod.append("One way Delivery")
            self.deliveryprices["One way Delivery"] = self.pickprice.get()

    # choose delivery
    def deliverywithreturn(self):
        if ("Delivery with return" in self.deliverymethod):

            self.deliverymethod.remove("Delivery with return")
            del self.deliveryprices["Delivery with return"]
        else:
            self.deliverymethod.append("Delivery with return")
            self.deliveryprices["Delivery with return"] = self.deliveryprice.get()
            self.deliveryprices["Delivery with return"] = self.deliveryprice.get()

    # show path of a photo
    def show_path(self):
        self.path["text"] = self.photolist

    # add photo
    def addphototools(self):
        from FUNC.f_file import f_file
        file = f_file()
        self.photolist = file.uploadphotos()
        self.show_path()

    # add data to db
    def savetool(self):
        from PAGES.p_my_products import p_my_products
        products = f_products()
        products.add_tool(self.controller.session.userid, self.name.get(), self.priceperday.get(), self.type.get(),
                       self.photolist, self.condition.get(), self.description.get(), self.deliveryprices)
        self.controller.show_frame(p_my_products)

    # cleanup
    def run(self):
        pass
