from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from FUNC.f_products import f_products
from shutil import copy2

from FUNC.f_userd import f_userd


# Add toll Page frame
class p_new_product(Frame):
    # basic properties
    photolist = []
    deliverymethod = []
    deliveryprices = {}

    # init of frame
    def __init__(self, parent, controller):
        # basic import for frame
        from PAGES.p_start import p_start
        from PAGES.p_search import p_search
        from FUNC.f_userd import f_userd

        Frame.__init__(self, parent)
        self.controller = controller
        # logout

        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_search)).pack(pady=10, padx=10)

        # topic
        Label(self, text="Add tool", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # DATA
        Label(self, text="Name:", font=f_userd.SMALL_FONT).pack()
        self.name = Entry(self, textvariable=f_userd.NAME)
        self.name.pack()
        Label(self, text="Type:", font=f_userd.SMALL_FONT).pack()
        self.type = Entry(self, textvariable=f_userd.TYPE)
        self.type.pack()

        Label(self, text="Condition:", font=f_userd.LARGE_FONT).pack()
        self.condition = Combobox(self)
        self.condition.pack()
        # add pic
        Label(self, text="Photo:", font=f_userd.LARGE_FONT).pack()

        Button(self, text='Browse', command=self.addphototools).pack()
        # add PIC

        Label(self, text="Describe product:", font=f_userd.LARGE_FONT).pack()
        self.description = Entry(self, textvariable=f_userd.DESCRIPTION)
        self.description.pack()

        Label(self, text="Price in £", font=f_userd.LARGE_FONT).pack()

        Label(self, text="Per day:", font=f_userd.SMALL_FONT).pack()
        self.priceperday = Entry(self, textvariable=f_userd.PRICE_DAY)
        self.priceperday.pack()
        Label(self, text="Delivery method:", font=f_userd.SMALL_FONT).pack()

        self.pick = Checkbutton(self, text="Delivery with return", variable="Delivery with return",
                                command=self.delivery)
        self.pick.pack()
        Label(self, text="Delivery price:", font=f_userd.SMALL_FONT).pack()

        self.pickprice = Entry(self, textvariable=f_userd.DESCRIPTION)
        self.pickprice.pack()
        self.delivery = Checkbutton(self, text="One way delivery", variable="delivery", command=self.deliverywithreturn)
        self.delivery.pack()
        Label(self, text="Delivery price:", font=f_userd.SMALL_FONT).pack()

        self.deliveryprice = Entry(self, textvariable=f_userd.DESCRIPTION)
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
            self.deliveryprices["Delivery with return"] = self.deliveryprice.get()

    # run photo upload
    def addphototools(self):
        from FUNC.f_file import f_file
        file = f_file()
        self.photolist = file.uploadphotos()
        print(self.photolist)

    # save tool
    def savetool(self):
        from PAGES.p_my_products import p_my_products
        products = f_products()
        products.add_tool(self.controller.session.userid, self.name.get(), self.priceperday.get(), self.type.get(),
                       self.photolist, self.condition.get(), self.description.get(), self.deliveryprices)
        self.controller.show_frame(p_my_products)

    # basic action before show frame
    def run(self):
        pass
