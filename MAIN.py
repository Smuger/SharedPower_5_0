# import tkinter
from tkinter import *
from tkinter.ttk import *

# import pages
from PAGES.p_end_rental import p_end_rental
from PAGES.p_invoice import p_invoice
from PAGES.p_start import p_start
from PAGES.p_my_product import p_my_product
from PAGES.p_my_products import p_my_products
from PAGES.p_new_rental import p_new_rental
from PAGES.p_result import p_result
from PAGES.p_search import p_search
from PAGES.p_product import p_product
from PAGES.p_new_product import p_new_product
from PAGES.p_signup import p_signup
from PAGES.p_multiple_invoices import p_multiple_invoices

# import logon functionality
from FUNC.f_logon import f_logon

class MAIN(Tk):

    # data storage
    session = f_logon()
    searchkeyword = ""
    selectedtool = ""
    selectedinvoice = ""
    selectedinvoiceid = 0
    selectedtoolid = 0
    selectrental = 0
    selectedrelinvoiceid = 0
    deliveryprice= 0
    deliverytype = ""
    price = 0

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # title and a name of the window
        self.title("Shared Power")
        self.iconbitmap("RES/favicon/favicon.ico")

        # general container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # page stack system
        for F in (p_product, p_search, p_result, p_new_rental, p_my_product, p_start, p_invoice, p_end_rental,
                  p_my_products, p_new_product, p_signup, p_product, p_multiple_invoices):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # show first page
        self.show_frame(p_start)

    # take page to the top of a stack
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.run()
        frame.tkraise()

# main loop
if __name__ == "__main__":
    app = MAIN()
    app.mainloop()
