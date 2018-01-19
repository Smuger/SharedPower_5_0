from tkinter import *
from tkinter.ttk import *


class ResultPage(Frame):
    def __init__(self, parent, controller):
        from Frames.main import MainPage
        from Frames.search import SearchPage
        from Controllers.Setting import SettingsController
        from Controllers.Tools import ToolController
        from Controllers.Rental import RentalController
        self.controller = controller
        self.tool = ToolController()
        self.rental = RentalController()
        from Controllers.Setting import SettingsController
        Frame.__init__(self, parent)

        # logout
        logout = Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()

        # back
        back = Button(self, text="Back", command=lambda: controller.show_frame(SearchPage)).pack()

        # search
        self.search_entry = Entry(self, textvariable=SettingsController.SEARCH_RESULT)
        self.search_entry.pack(pady=10, padx=10)
        search = Button(self, text="Search", command=self.search).pack()

        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.record = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            self.record.insert(END, "Tool number")
        self.record.pack(fill=BOTH)
        scrollbar.config(command=self.record.yview())
        # scrollbar

    def run(self):

        tools = self.tool.search_by_name(self.controller.searchkeyword)
        self.record.delete(0, END)
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, self.controller.searchkeyword)

        if tools:
            for index, toolitem in enumerate(tools):
                self.record.insert(END, toolitem["name"])
                self.record.bind('<<ListboxSelect>>', self.onselect)
        else:
            toolsbytype = self.tool.search_by_type(self.controller.searchkeyword)
            for index, toolitem in enumerate(toolsbytype):
                self.record.insert(END, toolitem["name"])
                self.record.bind('<<ListboxSelect>>', self.onselect)

    def search(self):
        self.controller.searchkeyword = self.search_entry.get()
        self.controller.show_frame(ResultPage)

    def onselect(self, evt):
        from Frames.tool import ToolPage

        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedtool = value
        self.controller.show_frame(ToolPage)