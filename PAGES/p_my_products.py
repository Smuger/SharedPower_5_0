from tkinter import *
from tkinter.ttk import *

from Frames.finishrental import FinishRentalPage
from Frames.rental import RentalPage
from Frames.tool import ToolPage

class MyToolsPage(Frame):
    selectedtool = "";
    toollist = []
    renttoollist =[]
    def __init__(self, parent, controller):
        from Frames.main import MainPage
        from Frames.search import SearchPage
        from Controllers.Setting import SettingsController
        from Controllers.Tools import ToolController
        from Controllers.Rental import RentalController
        self.controller = controller
        self.tool = ToolController()
        self.rental = RentalController()
        Frame.__init__(self, parent)
        # logout
        Button(self, text="Logout", command=lambda: self.controller.show_frame(MainPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: self.controller.show_frame(SearchPage)).pack(pady=10, padx=10)

        # topic
        self.topic = Label(self, text="Your balance is: £" + str(SettingsController.WALLET),
                      font=SettingsController.LARGE_FONT)
        self.topic.pack(pady=10, padx=10)

        # what tools you leased
        Label(self, text="Leased:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK

        self.record = Listbox(self)
        tools = self.tool.list_all(1514206410.671336)
        for index, toolitem in enumerate(tools):
            self.record.insert(END, toolitem["name"] + str(index))
        self.record.pack(fill=BOTH)
        # scrollbar

        # what tools you rented
        Label(self, text="Rented:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

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

        from Frames.mytool import MyToolPage
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedtool = value
        self.controller.selectedtoolid = self.toollist[index]["id"]

        self.controller.show_frame(MyToolPage)

    def onselectrental(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectrental = self.renttoollist[index]["id"]
        self.controller.show_frame(FinishRentalPage)
