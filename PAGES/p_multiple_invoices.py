# import tkinter
from tkinter import *
from tkinter.ttk import *

# import functionality
from FUNC.f_invoice import f_invoice
from FUNC.f_userd import f_userd

class p_multiple_invoices(Frame):
    # storage
    invoceslist = []
    relinvoicelist = []

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # import pages
        from PAGES.p_start import p_start
        from PAGES.p_my_products import p_my_products

        # import functionality
        from FUNC.f_products import f_products

        # define controller, tool and invoices
        self.controller = controller
        self.tool = f_products()
        self.invoices = f_invoice()

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_my_products)).pack(pady=10, padx=10)

        # invoice
        self.invoicesbox = Listbox(self)
        for line in range(100):
            self.invoicesbox.insert(END, "Invoice number" + str(line))
        self.invoicesbox.pack(fill=BOTH)

        Label(self, text="Invoiced from my rentings:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # scrollbar
        self.relinvoces = Listbox(self)
        for line in range(100):
            self.relinvoces.insert(END, "Invoice number" + str(line))
        self.relinvoces.pack(fill=BOTH)

    #cleanup
    def run(self):
        # populate data
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

    # select handler leased
    def onselect(self, evt):
        from PAGES.p_invoice import p_invoice
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(p_invoice)

    # select handler rent
    def onselectrelatedinvoice(self, evt):
        from PAGES.p_invoice import p_invoice
        w = evt.widget
        print(w.curselection())
        index = int(w.curselection()[0])
        value = w.get(index)
        self.controller.selectedinvoice = value
        self.controller.selectedrelinvoiceid = self.invoceslist[index]["id"]
        self.controller.show_frame(p_invoice)