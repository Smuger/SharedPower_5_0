from tkinter import *
from tkinter.ttk import *


from PIL import ImageTk, Image

from FUNC.f_userd import f_userd
from PAGES.p_new_rental import p_new_rental
from PAGES.p_my_products import p_my_products

class p_my_product(Frame):

    def __init__(self, parent, controller):
        from PAGES.p_start import p_start
        from PAGES.p_result import p_result
        from FUNC.f_products import f_products
        self.controller = controller
        self.tool = f_products()
        Frame.__init__(self, parent)
        self.controller = controller
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()
        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_my_products)).pack(pady=10, padx=10)

        self.name = Label(self, text="Name:", font=f_userd.LARGE_FONT_BOLD)
        self.name.pack()
        product_file = PhotoImage(file="RES/users/no_avatar.png")
        self.avatar = Label(self, image=product_file)
        self.avatar.image = product_file
        self.avatar.pack()
        Label(self, text="Description:", font=f_userd.LARGE_FONT).pack()
        self.description = Label(self, text="Name:", font=f_userd.LARGE_FONT, wraplength=350, justify=CENTER)
        self.description.pack()

        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)



        Label(self, text="Price: £", font=f_userd.LARGE_FONT).pack()
        self.price = Label(self, text="Name:", font=f_userd.SMALL_FONT)
        self.price.pack()

    def run(self):
        tools = self.tool.search_by_name(self.controller.selectedtool)
        tool=tools[0]
        self.name["text"] = tool["name"]
        self.price["text"]= tool["price"]
        self.description["text"] = tool["description"]

        for photo in tool["photos"]:
            photo = Image.open((photo))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            product_file = ImageTk.PhotoImage(photo)

            self.avatar.image = product_file
            self.avatar.config(image=product_file)
