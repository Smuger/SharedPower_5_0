# import tkinter
from tkinter import *
from tkinter.ttk import *

# import image handler
from PIL import ImageTk, Image

# import page
from PAGES.p_result import p_result

class p_search(Frame):

    # storage
    userdetails = ""
    username = ""
    searchvalue = ""

    def __init__(self, parent, controller):

        # import pages
        from PAGES.p_my_products import p_my_products
        from PAGES.p_new_product import p_new_product
        from PAGES.p_start import p_start

        # import functionality
        from FUNC.f_userd import f_userd
        from FUNC.f_users import f_users
        from FUNC.f_logon import f_logon

        Frame.__init__(self, parent)
        # define controller
        self.controller = controller

        # load avatar
        avatar_file = PhotoImage(file="RES/users/no_avatar.png")
        self.avatar = Label(self, image=avatar_file)
        self.avatar.image = avatar_file
        self.avatar.pack()

        # load login
        self.username = Label(self, text="Luke Logan", font=f_userd.SMALL_FONT)
        self.username.pack()

        # logout
        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # my tools
        Button(self, text="My tools", command=lambda: controller.show_frame(p_my_products)).pack()

        # add a new tool
        Button(self, text="Add tool", command=lambda: controller.show_frame(p_new_product)).pack()

        # search
        self.search_entry = Entry(self, textvariable=f_userd.SEARCH)
        self.search_entry.pack(pady=10, padx=10)
        Button(self, text="Search", command=self.search).pack()

    # cleanup
    def run(self):
        self.search_entry.config(textvariable="")
        self.search_entry.delete(0, END)
        print("test")
        if self.controller.session.session:
            details = self.controller.session.userdetails

            self.username["text"] = details["name"]
            photo = Image.open((details["avatar"]))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            avatar_file = ImageTk.PhotoImage(photo)

            self.avatar.image = avatar_file
            self.avatar.config(image=avatar_file)

    # pass search phrase
    def search(self):
        self.controller.searchkeyword = self.search_entry.get()
        self.controller.show_frame(p_result)
