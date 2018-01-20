from tkinter import *
from tkinter.ttk import *

from PAGES.p_end_rental import p_end_rental
from PAGES.p_new_rental import p_new_rental
from PAGES.p_product import p_product

class p_my_products(Frame):
    selectedtool = "";
    toollist = []
    renttoollist =[]
    def __init__(self, parent, controller):
        from PAGES.p_start import p_start
        from PAGES.p_search import p_search
        from FUNC.f_userd import f_userd
        from FUNC.f_products import f_products
        from FUNC.f_rental import f_rental
        self.controller = controller
        self.tool = f_products()
        self.rental = f_rental()
        Frame.__init__(self, parent)
        # logout
        Button(self, text="Logout", command=lambda: self.controller.show_frame(p_start)).pack()

        # back
        back = Button(self, text="Back", command=lambda: self.controller.show_frame(p_search)).pack(pady=10, padx=10)

        # topic
        self.topic = Label(self, text="Your balance is: £" + str(f_userd.WALLET),
                      font=f_userd.LARGE_FONT)
        self.topic.pack(pady=10, padx=10)

        # what tools you leased
        Label(self, text="Leased:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK

        self.record = Listbox(self)
        tools = self.tool.list_all(1514206410.671336)
        for index, toolitem in enumerate(tools):
            self.record.insert(END, toolitem["name"] + str(index))
        self.record.pack(fill=BOTH)
        # scrollbar

        # what tools you rented
        Label(self, text="Rented:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK

        self.rentedrecord = Listbox(self)
        for line in range(100):
            self.rentedrecord.insert(END, "Tool number" + str(line))
        self.rentedrecord.pack(fill=BOTH)

        # scrollbar

    def run(self):
        self.selectedtool = ""
        if self.controller.session.session:
            tools = self.tool.list_all(self.controller.session.userdetails["id"])
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

    def onselect(self, evt):

        from PAGES.p_my_product import p_my_product
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedtool = value
        self.controller.selectedtoolid = self.toollist[index]["id"]

        self.controller.show_frame(p_my_product)

    def onselectrental(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectrental = self.renttoollist[index]["id"]
        self.controller.show_frame(p_end_rental)
