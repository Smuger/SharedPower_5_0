from tkinter import *
from tkinter.ttk import *


from PIL import ImageTk, Image

from FUNC.f_userd import f_userd
from PAGES.p_new_rental import p_new_rental


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
        Button(self, text="Back", command=lambda: controller.show_frame(p_result)).pack(pady=10, padx=10)
        Label(self, text="Tool Details", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)
        Label(self, text="Name:", font=f_userd.SMALL_FONT).pack()
        self.name = Label(self, text="Name:", font=f_userd.SMALL_FONT)
        self.name.pack()
        Label(self, text="Description:", font=f_userd.SMALL_FONT).pack()
        self.description = Label(self, text="Name:", font=f_userd.SMALL_FONT)
        self.description.pack()
        Label(self, text="photos:", font=f_userd.SMALL_FONT).pack()
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)


        Label(self, text="Price:", font=f_userd.SMALL_FONT).pack()
        self.price = Label(self, text="Name:", font=f_userd.SMALL_FONT)
        self.price.pack()

    def run(self):
        tools = self.tool.search_by_name(self.controller.selectedtool)
        tool=tools[0]
        self.name["text"] = tool["name"]
        self.price["text"]= tool["price"]
        self.description["text"] = tool["description"]

        for photo in tool["photos"]:
            avatar_file = ImageTk.PhotoImage(Image.open((photo)).resize((100, 50), Image.ANTIALIAS))
            avatar = Label(self.frame, image=avatar_file)
            avatar.image = avatar_file
            avatar.config(image=avatar_file)
            avatar.pack()
