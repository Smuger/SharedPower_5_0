# import tkinter
from tkinter import *
from tkinter.ttk import *

# image handler
from PIL import ImageTk, Image

# import page
from PAGES.p_my_products import p_my_products

# import functionality
from FUNC.f_userd import f_userd

class p_my_product(Frame):
    def __init__(self, parent, controller):

        # import page
        from PAGES.p_start import p_start

        # import functionality
        from FUNC.f_products import f_products

        # define controller and tool
        self.controller = controller
        self.tool = f_products()

        Frame.__init__(self, parent)

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_my_products)).pack(pady=10, padx=10)

        # product avatar
        self.name = Label(self, text="Name:", font=f_userd.LARGE_FONT_BOLD)
        self.name.pack()
        product_file = PhotoImage(file="RES/tools/no_image.png")
        self.avatar = Label(self, image=product_file)
        self.avatar.image = product_file
        self.avatar.pack()

        # description
        Label(self, text="Description:", font=f_userd.LARGE_FONT).pack()
        self.description = Label(self, text="Name:", font=f_userd.LARGE_FONT, wraplength=350, justify=CENTER)
        self.description.pack()

        # target frame
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        # price
        Label(self, text="Price: £", font=f_userd.LARGE_FONT).pack()
        self.price = Label(self, text="Name:", font=f_userd.SMALL_FONT)
        self.price.pack()

    # cleanup
    def run(self):
        tools = self.tool.search_by_name(self.controller.selectedtool)
        tool=tools[0]
        self.name["text"] = tool["name"]
        self.price["text"]= tool["price"]
        self.description["text"] = tool["description"]

        # load image only one for now
        for photo in tool["photos"]:
            photo = Image.open((photo))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            product_file = ImageTk.PhotoImage(photo)

            self.avatar.image = product_file
            self.avatar.config(image=product_file)
