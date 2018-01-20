from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from PAGES.p_result import p_result



class p_search(Frame):
    userdetails = ""
    username = ""
    searchvalue = ""


    def __init__(self, parent, controller):
        from PAGES.p_my_products import p_my_products
        from PAGES.p_new_product import p_new_product
        from PAGES.p_multiple_invoices import p_multiple_invoices
        from PAGES.p_start import p_start

        from FUNC.f_userd import f_userd
        from FUNC.f_users import f_users
        from FUNC.f_logon import f_logon

        Frame.__init__(self, parent)
        user = f_users
        session = f_logon
        self.controller = controller
        # user avatar
        avatar_file = PhotoImage(file="RES/users/no_avatar.png")
        self.avatar = Label(self, image=avatar_file)
        self.avatar.image = avatar_file
        self.avatar.pack()

        # user name
        self.username = Label(self, text="Luke Logan", font=f_userd.SMALL_FONT)
        self.username.pack()



        Button(self, text="Logout", command=lambda: controller.show_frame(p_start)).pack()

        # mytools
        Button(self, text="My tools", command=lambda: controller.show_frame(p_my_products)).pack()
        Button(self, text="My invoices", command=lambda: controller.show_frame(p_multiple_invoices)).pack()

        # addtool
        Button(self, text="Add tool", command=lambda: controller.show_frame(p_new_product)).pack()

        # Search part
        self.search_entry = Entry(self, textvariable=f_userd.SEARCH)
        self.search_entry.pack(pady=10, padx=10)
        #search button
        Button(self, text="Search", command=self.search).pack()

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

    def search(self):
        self.controller.searchkeyword = self.search_entry.get()
        self.controller.show_frame(p_result)
