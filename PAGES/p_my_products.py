# import tkinter
from tkinter import *
from tkinter.ttk import *

# import pages
from PAGES.p_end_rental import p_end_rental

class p_my_products(Frame):
    # data storage
    selectedtool = "";
    toollist = []
    renttoollist =[]
    def __init__(self, parent, controller):

        # import pages
        from PAGES.p_multiple_invoices import p_multiple_invoices
        from PAGES.p_start import p_start
        from PAGES.p_search import p_search

        # import functionality
        from FUNC.f_userd import f_userd
        from FUNC.f_products import f_products
        from FUNC.f_rental import f_rental

        # define controller, tool and rental
        self.controller = controller
        self.tool = f_products()
        self.rental = f_rental()

        Frame.__init__(self, parent)

        # logout
        Button(self, text="Logout", command=lambda: self.controller.show_frame(p_start)).pack()

        # my invoices
        Button(self, text="My invoices", command=lambda: controller.show_frame(p_multiple_invoices)).pack()

        # back
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_search)).pack(pady=10, padx=10)

        # balance
        self.topic = Label(self, text="Your balance is: £" + str(f_userd.WALLET), font=f_userd.LARGE_FONT)
        self.topic.pack(pady=10, padx=10)

        # leased products
        Label(self, text="Leased:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar
        self.record = Listbox(self)
        tools = self.tool.list_all(1514206410.671336)
        for index, toolitem in enumerate(tools):
            self.record.insert(END, toolitem["name"] + str(index))
        self.record.pack(fill=BOTH)

        # rented
        Label(self, text="Rented:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar
        self.rentedrecord = Listbox(self)
        for line in range(100):
            self.rentedrecord.insert(END, "Tool number" + str(line))
        self.rentedrecord.pack(fill=BOTH)

    # cleanup
    def run(self):
        self.selectedtool = ""

        if self.controller.session.session:
            tools = self.tool.list_all(self.controller.session.userdetails["id"])

            # populate scrollbar
            self.record.delete(0, END)
            self.topic.config(text="Your balance is: £" + str(self.controller.session.userdetails["balance"]))
            for index, toolitem in enumerate(tools):
                self.record.insert(END, toolitem["name"])
                self.record.bind('<<ListboxSelect>>', self.onselect)
                self.toollist.append(toolitem)
            rentals = self.rental.my_rented_tools(self.controller.session.userdetails["id"])
            self.rentedrecord.delete(0, END)
            for index, rental in enumerate(rentals):
                toolitem = self.tool.gettoolbyid(rental["toolid"])
                self.rentedrecord.insert(END, toolitem["name"])
                self.rentedrecord.bind('<<ListboxSelect>>', self.onselectrental)
                self.renttoollist.append(rental)

    # select handler leased
    def onselect(self, evt):

        # import page
        from PAGES.p_my_product import p_my_product

        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedtool = value
        self.controller.selectedtoolid = self.toollist[index]["id"]
        self.controller.show_frame(p_my_product)

    # select handler rented
    def onselectrental(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectrental = self.renttoollist[index]["id"]
        self.controller.show_frame(p_end_rental)
