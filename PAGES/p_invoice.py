from tkinter import BOTH, RAISED
from tkinter.ttk import *

from PIL import ImageTk, Image

from FUNC.f_userd import f_userd
from PAGES.p_multiple_invoices import p_multiple_invoices


class p_invoice(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        # basic imports
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result
        from FUNC.f_products import f_products

        # basic properties
        self.controller = controller
        self.tool = f_products()
        Frame.__init__(self, parent)
        self.controller = controller

        # inserting of elements of gui
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_multiple_invoices)).pack(pady=10, padx=10)
        self.invocename = Label(self, text="Invoce 23:", font=f_userd.LARGE_FONT)
        self.invocename.pack(pady=10, padx=10)

        Label(self, text="Payment List:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        self.photos = Label(self, text="Photos:", font=f_userd.LARGE_FONT)
        self.photos.pack()
        self.photolistframe = Frame(self, relief=RAISED, borderwidth=1)
        self.photolistframe.pack(fill=BOTH, expand=True)
        Label(self, text="Price", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.price = Label(self, text="Price", font=f_userd.LARGE_FONT)
        self.price.pack(pady=10, padx=10)

    # basic actions before show frame
    def run(self):
        from FUNC.f_invoice import f_invoice
        self.photos.config(text="")
        invoices = f_invoice()
        invoice = ""
        #claer payment list
        for child in self.frame.winfo_children():
            child.destroy()
        #clear photo list
        for child in self.photolistframe.winfo_children():
            child.destroy()
        #check if display owner or rental invoice
        if (self.controller.selectedinvoiceid != 0):
            invoice = invoices.get_invoce(self.controller.selectedinvoiceid)
            print(invoice)
            pass
        elif (self.controller.selectedrelinvoiceid != 0):
            self.photos.config(text="Photos:")
            invoice = invoices.get_invoce(self.controller.selectedrelinvoiceid)
            print(invoice)
            #insert photos to owner invoice
            for photo in invoice["photos"]:
                avatar_file = ImageTk.PhotoImage(Image.open((photo)).resize((100, 50), Image.ANTIALIAS))
                avatar = Label(self.photolistframe, image=avatar_file)
                avatar.image = avatar_file
                avatar.config(image=avatar_file)
                avatar.pack()
        print(invoice["itemlist"])
        #insert payment list items
        for item in invoice["itemlist"]:
            Label(self.frame, text=item,
                  font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        print(invoice)
        #show invoice name
        self.invocename.config(text=self.controller.selectedinvoice)
        self.price.config(text=str(invoice["summaryprice"]))
