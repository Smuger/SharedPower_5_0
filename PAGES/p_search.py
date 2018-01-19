from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

from Frames.result import ResultPage


class SearchPage(Frame):
    userdetails = ""
    username = ""
    searchvalue = ""

    def __init__(self, parent, controller):
        from Frames.mytools import MyToolsPage
        from Frames.result import ResultPage
        from Frames.addtool import AddPage
        from Controllers.Setting import SettingsController
        from Controllers.User import UserController
        from Controllers.Login import LoginController
        from Frames.invoices import InvoicesPage

        from Frames.main import MainPage
        Frame.__init__(self, parent)
        user = UserController
        session = LoginController
        self.controller = controller
        # user avatar
        avatar_file = PhotoImage(file="res/user.png")
        self.avatar = Label(self, image=avatar_file)
        self.avatar.image = avatar_file
        self.avatar.pack()

        # user name
        self.username = Label(self, text="Luke Logan", font=SettingsController.SMALL_FONT)
        self.username.pack()



        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()

        # mytools
        Button(self, text="My tools", command=lambda: controller.show_frame(MyToolsPage)).pack()
        Button(self, text="My invoices", command=lambda: controller.show_frame(InvoicesPage)).pack()

        # addtool
        Button(self, text="Add tool", command=lambda: controller.show_frame(AddPage)).pack()

        # Search part
        self.search_entry = Entry(self, textvariable=SettingsController.SEARCH)
        self.search_entry.pack(pady=10, padx=10)
        #search button
        Button(self, text="Search", command=self.search).pack()

    def run(self):
        self.search_entry.config(textvariable="")
        self.search_entry.delete(0, END)
        print("test")
        if self.controller.session.session:
            from Controllers.User import UserController
            from Controllers.Login import LoginController
            details = self.controller.session.userdetails

            self.username["text"] = details["name"]
            photo = Image.open((details["avatar"]))
            photo = photo.resize((400, 300), Image.ANTIALIAS)
            avatar_file = ImageTk.PhotoImage(photo)

            self.avatar.image = avatar_file
            self.avatar.config(image=avatar_file)

    def search(self):
        self.controller.searchkeyword = self.search_entry.get()
        self.controller.show_frame(ResultPage)
