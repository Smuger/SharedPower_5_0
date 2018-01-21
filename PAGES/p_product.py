from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image

from FUNC.f_userd import f_userd
from PAGES.p_new_rental import p_new_rental


class p_product(Frame):
    dayfee = 0

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
        Button(self, text="Back", command=lambda: controller.show_frame(p_result)).pack(pady=10, padx=10)

        self.name = Label(self, text="Name: ", font=f_userd.LARGE_FONT_BOLD)
        self.name.pack()

        product_file = PhotoImage(file="RES/users/no_avatar.png")
        self.avatar = Label(self, image=product_file)
        self.avatar.image = product_file
        self.avatar.pack()

        Label(self, text="Condition:", font=f_userd.LARGE_FONT).pack()
        self.condition = Label(self, text="Condition:", font=f_userd.LARGE_FONT, wraplength=350, justify=CENTER)
        self.condition.pack()

        Label(self, text="Description:", font=f_userd.LARGE_FONT).pack()
        self.description = Label(self, text="Name:", font=f_userd.SMALL_FONT, wraplength=350, justify=CENTER)
        self.description.pack()



        Label(self, text="Price: ", font=f_userd.LARGE_FONT).pack()
        self.price = Label(self, text="", font=f_userd.SMALL_FONT)
        self.price.pack()
        Button(self, text="Rent", command=self.rental).pack(pady=10, padx=10)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(expand=True)

    def run(self):
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


        for photo in tool["photos"]:
            photo = Image.open((photo))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            product_file = ImageTk.PhotoImage(photo)
            self.avatar.image = product_file
            self.avatar.config(image=product_file)

    def rental(self):
        self.controller.price = self.dayfee

        self.controller.show_frame(p_new_rental)
