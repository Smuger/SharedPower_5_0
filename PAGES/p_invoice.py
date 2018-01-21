# import tkinter
from tkinter import BOTH, RAISED
from tkinter.ttk import *

# import image handler
from PIL import ImageTk, Image

# import pages
from PAGES.p_multiple_invoices import p_multiple_invoices

# import functionality
from FUNC.f_userd import f_userd

class p_invoice(Frame):
    def __init__(self, parent, controller):

        # define controller
        self.controller = controller
        Frame.__init__(self, parent)

        # import pages
        from PAGES.p_start import p_start
        # import functionality
        from FUNC.f_products import f_products

        # define controller
        self.controller = controller
        self.tool = f_products()
        Frame.__init__(self, parent)

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: self.controller.show_frame(p_multiple_invoices)).pack(pady=10, padx=10)

        # name of invoice
        self.invocename = Label(self, text="Invoce 23:", font=f_userd.LARGE_FONT)
        self.invocename.pack(pady=10, padx=10)

        # payment
        Label(self, text="Payment List:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        # photo of a
        self.photos = Label(self, text="Photos:", font=f_userd.LARGE_FONT)
        self.photos.pack()
        self.photolistframe = Frame(self, relief=RAISED, borderwidth=1)
        self.photolistframe.pack(fill=BOTH, expand=True)

        # price
        Label(self, text="Price", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        self.price = Label(self, text="Price", font=f_userd.LARGE_FONT)
        self.price.pack(pady=10, padx=10)

    # cleanup
    def run(self):
        from FUNC.f_invoice import f_invoice
        self.photos.config(text="")
        invoices = f_invoice()
        invoice = ""

        # destroy frame
        for child in self.frame.winfo_children():
            child.destroy()

        # photo destory
        for child in self.photolistframe.winfo_children():
            child.destroy()

        # is invoiced empty
        if (self.controller.selectedinvoiceid != 0):
            invoice = invoices.get_invoce(self.controller.selectedinvoiceid)
            pass
        # is invoiced id empty
        elif (self.controller.selectedrelinvoiceid != 0):
            self.photos.config(text="Photos:")
            invoice = invoices.get_invoce(self.controller.selectedrelinvoiceid)

            # load images
            for photo in invoice["photos"]:
                avatar_file = ImageTk.PhotoImage(Image.open((photo)).resize((100, 50), Image.ANTIALIAS))
                avatar = Label(self.photolistframe, image=avatar_file)
                avatar.image = avatar_file
                avatar.config(image=avatar_file)
                avatar.pack()


        for item in invoice["itemlist"]:
            Label(self.frame, text=item, font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # populate
        self.invocename.config(text=self.controller.selectedinvoice)
        self.price.config(text=str(invoice["summaryprice"]))
