# import tkinter
from tkinter import *
from tkinter.ttk import *

# import image handler
from PIL import ImageTk, Image

# import page
from PAGES.p_new_rental import p_new_rental

# import functionality
from FUNC.f_userd import f_userd

class p_product(Frame):
    # storage
    dayfee = 0

    def __init__(self, parent, controller):
        # import pages
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result

        # import functionality
        from FUNC.f_products import f_products

        self.tool = f_products()

        Frame.__init__(self, parent)

        # define controller and tool
        self.controller = controller

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_result)).pack(pady=10, padx=10)

        # name of the product
        self.name = Label(self, text="Name: ", font=f_userd.LARGE_FONT_BOLD)
        self.name.pack()

        # image of the
        product_file = PhotoImage(file="RES/tools/no_image.png")
        self.avatar = Label(self, image=product_file)
        self.avatar.image = product_file
        self.avatar.pack()

        # condition of a product
        Label(self, text="Condition:", font=f_userd.LARGE_FONT).pack()
        self.condition = Label(self, text="Condition:", font=f_userd.LARGE_FONT, wraplength=350, justify=CENTER)
        self.condition.pack()

        # description of a product
        Label(self, text="Description:", font=f_userd.LARGE_FONT).pack()
        self.description = Label(self, text="Name:", font=f_userd.SMALL_FONT, wraplength=350, justify=CENTER)
        self.description.pack()

        # price
        Label(self, text="Price: ", font=f_userd.LARGE_FONT).pack()
        self.price = Label(self, text="", font=f_userd.SMALL_FONT)
        self.price.pack()

        # rent
        Button(self, text="Rent", command=self.rental).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(expand=True)

    # cleanup
    def run(self):

        # set all the data
        tools = self.tool.search_by_name(self.controller.selectedtool)
        for child in self.frame.winfo_children():
            child.destroy()
        tool = tools[0]
        self.dayfee = tool["price"]
        self.name["text"] = tool["name"]
        self.price["text"] =  "£" + tool["price"]
        self.controller.selectedtoolid = tool["id"]
        self.description["text"] = tool["description"]
        self.condition["text"] = tool["condition"]

        # place only one photo for now
        for photo in tool["photos"]:
            photo = Image.open((photo))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            product_file = ImageTk.PhotoImage(photo)
            self.avatar.image = product_file
            self.avatar.config(image=product_file)

    # pass fee and open page
    def rental(self):
        self.controller.price = self.dayfee
        self.controller.show_frame(p_new_rental)
