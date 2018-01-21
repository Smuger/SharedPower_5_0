# import tkinter
from tkinter import *
from tkinter.ttk import *

class p_result(Frame):
    def __init__(self, parent, controller):

        # import pages
        from PAGES.p_start import p_start
        from PAGES.p_search import p_search
        # import functionality
        from FUNC.f_products import f_products
        from FUNC.f_rental import f_rental
        from FUNC.f_userd import f_userd

        # define controller, tool and rental
        self.controller = controller
        self.tool = f_products()
        self.rental = f_rental()

        Frame.__init__(self, parent)

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_search)).pack()

        # search
        self.search_entry = Entry(self, textvariable=f_userd.SEARCH_RESULT)
        self.search_entry.pack(pady=10, padx=10)
        Button(self, text="Search", command=self.search).pack()

        # scrollbar
        self.record = Listbox(self)
        for line in range(100):
            self.record.insert(END, "Tool number")
        self.record.pack(fill=BOTH)

    # cleanup
    def run(self):

        # prepare scrollbar
        tools = self.tool.search_by_name(self.controller.searchkeyword)
        self.record.delete(0, END)
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, self.controller.searchkeyword)

        # populate
        if tools:
            for index, toolitem in enumerate(tools):
                self.record.insert(END, toolitem["name"])
                self.record.bind('<<ListboxSelect>>', self.onselect)
        else:
            toolsbytype = self.tool.search_by_type(self.controller.searchkeyword)
            for index, toolitem in enumerate(toolsbytype):
                self.record.insert(END, toolitem["name"])
                self.record.bind('<<ListboxSelect>>', self.onselect)

    # pass search phrase and load page
    def search(self):
        self.controller.searchkeyword = self.search_entry.get()
        self.controller.show_frame(p_result)

    # selecting functionality
    def onselect(self, evt):

        # import page
        from PAGES.p_product import p_product

        # get selected
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedtool = value
        self.controller.show_frame(p_product)