from tkinter import *
from tkinter.ttk import *

from FUNC.f_invoice import f_invoice
from FUNC.f_userd import f_userd
from PAGES.p_search import p_search


class p_multiple_invoices(Frame):
    invoceslist = []
    relinvoicelist = []

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #basic imports
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result
        from FUNC.f_products import f_products
        #basic properties
        self.controller = controller
        self.tool = f_products()
        self.invoices = f_invoice()

        #basic gui
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_search)).pack(pady=10, padx=10)


        self.invoicesbox = Listbox(self)
        for line in range(100):
            self.invoicesbox.insert(END, "Invoice number" + str(line))
        self.invoicesbox.pack(fill=BOTH)

        Label(self, text="Invoiced from my rentings:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar NOT-WORK

        self.relinvoces = Listbox(self)
        for line in range(100):
            self.relinvoces.insert(END, "Invoice number" + str(line))
        self.relinvoces.pack(fill=BOTH)

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
        from PAGES.p_invoice import p_invoice
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(p_invoice)

    def onselectrelatedinvoice(self, evt):
        from PAGES.p_invoice import p_invoice
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedrelinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(p_invoice)