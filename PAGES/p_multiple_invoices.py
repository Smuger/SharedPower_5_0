from tkinter import *
from tkinter.ttk import *

from Controllers.Invoices import InvoicesController
from Controllers.Setting import SettingsController
from Frames.search import SearchPage


class InvoicesPage(Frame):
    invoceslist = []
    relinvoicelist = []

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #basic imports
        from Frames.main import MainPage
        from Frames.result import ResultPage
        from Controllers.Tools import ToolController
        #basic properties
        self.controller = controller
        self.tool = ToolController()
        self.invoices = InvoicesController()

        #basic gui
        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: self.controller.show_frame(SearchPage)).pack(pady=10, padx=10)

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.invoicesbox = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            self.invoicesbox.insert(END, "Invoice number" + str(line))
        self.invoicesbox.pack(fill=BOTH)
        scrollbar.config(command=self.invoicesbox.yview())
        Label(self, text="Invoiced from my rentings:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.relinvoces = Listbox(self, yscrollcommand=scrollbar.set)
        for line in range(100):
            self.relinvoces.insert(END, "Invoice number" + str(line))
        self.relinvoces.pack(fill=BOTH)
        scrollbar.config(command=self.relinvoces.yview())
    #basic action
    def run(self):
        # reset basic data
        self.controller.selectedinvoice = ""
        self.controller.selectedinvoiceid = 0
        self.controller.selectedrelinvoiceid = 0
        if self.controller.session.session:
            invoces = self.invoices.get_invoices(self.controller.session.userdetails["id"])
            self.invoicesbox.delete(0, END)
            for index, invoice in enumerate(invoces):
                self.invoicesbox.insert(END, "invoice" + invoice["id"])
                self.invoicesbox.bind('<<ListboxSelect>>', self.onselect)
                self.invoceslist.append(invoice)
            invoices = self.invoices.get_retlated_invoices(self.controller.session.userdetails["id"])
            self.relinvoces.delete(0, END)
            for index, invoice in enumerate(invoices):
                self.relinvoces.insert(END, "invoice" + invoice["id"])
                self.relinvoces.bind('<<ListboxSelect>>', self.onselectrelatedinvoice)
                self.relinvoicelist.append(invoice)

    def onselect(self, evt):
        from Frames.invoice import InvoicePage
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(InvoicePage)

    def onselectrelatedinvoice(self, evt):
        from Frames.invoice import InvoicePage
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedrelinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(InvoicePage)