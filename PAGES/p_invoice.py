from tkinter import BOTH, RAISED
from tkinter.ttk import *

from PIL import ImageTk, Image

from Controllers.Setting import SettingsController
from Frames.invoices import InvoicesPage


class InvoicePage(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        # basic imports
        from Frames.main import MainPage
        from Frames.result import ResultPage
        from Controllers.Tools import ToolController

        # basic properties
        self.controller = controller
        self.tool = ToolController()
        Frame.__init__(self, parent)
        self.controller = controller

        # inserting of elements of gui
        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()
        Button(self, text="Back", command=lambda: self.controller.show_frame(InvoicesPage)).pack(pady=10, padx=10)
        self.invocename = Label(self, text="Invoce 23:", font=SettingsController.LARGE_FONT)
        self.invocename.pack(pady=10, padx=10)

        Label(self, text="Payment List:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        self.photos = Label(self, text="Photos:", font=SettingsController.LARGE_FONT)
        self.photos.pack()
        self.photolistframe = Frame(self, relief=RAISED, borderwidth=1)
        self.photolistframe.pack(fill=BOTH, expand=True)
        Label(self, text="Price", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        self.price = Label(self, text="Price", font=SettingsController.LARGE_FONT)
        self.price.pack(pady=10, padx=10)

    # basic actions before show frame
    def run(self):
        from Controllers.Invoices import InvoicesController
        self.photos.config(text="")
        invoices = InvoicesController()
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
                  font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        print(invoice)
        #show invoice name
        self.invocename.config(text=self.controller.selectedinvoice)
        self.price.config(text=str(invoice["summaryprice"]))
