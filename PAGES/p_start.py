from tkinter import *
from tkinter.ttk import *


class MainPage(Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        from Controllers.Setting import SettingsController
        from Frames.signup import SignUpPage

        Frame.__init__(self, parent)

        # logo
        logo = PhotoImage(file="res/settings.png")
        label = Label(self, image=logo)
        label.image = logo
        label.pack()

        # topic
        Label(self, text="Welcome to SharedPower", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # sign up
        Button(self, text="Sing up", command=lambda: controller.show_frame(SignUpPage)).pack(pady=10, padx=10)
        Label(self, text="Login:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # SettingsController.LOGIN
        self.LOGIN = Entry(self, textvariable=SettingsController.LOGIN)
        self.LOGIN.pack()
        Label(self, text="Password:", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # password
        self.password = Entry(self, show="*", textvariable=SettingsController.PASSWORD)
        self.password.pack()
        self.errors = Label(self, text="", font=SettingsController.SMALL_FONT)
        self.errors.pack()
        # sign in
        Button(self, text="Sign in", command=self.login).pack(pady=10, padx=10)

    # login front action
    def login(self):

        from Frames.search import SearchPage
        #check if user is login if is -> logout
        if (self.controller.session.session):
            self.controller.session.logout()
        #try login of user
        self.controller.session.login(self.LOGIN.get(), self.password.get())
        #check login status
        if (self.controller.session.session):
            self.controller.show_frame(SearchPage)
        else:
            self.errors['text'] = "Password and Login doesn't match to any user."
    #basic action before show frame
    def run(self):
        #basic clear of frame
        self.errors['text'] = ""
        if self.controller.session.session:
            self.controller.session.logout()
