from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class p_start(Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        from FUNC.f_userd import f_userd
        from PAGES.p_signup import p_signup

        Frame.__init__(self, parent)

        # logo with antialiasing
        self.logo = PhotoImage(file="RES/logo/logo.png")
        self.label = Label(self, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, columnspan=2)


        # sign up
        Button(self, text="Sing up", command=lambda: controller.show_frame(p_signup)).grid(row=4, column=0, sticky=EW)
        Label(self, text="Login:", font=f_userd.LARGE_FONT).grid(row=1, column=0)

        # SettingsController.LOGIN
        self.LOGIN = Entry(self, textvariable=f_userd.LOGIN)
        self.LOGIN.grid(row=1, column=1)
        Label(self, text="Password:", font=f_userd.LARGE_FONT).grid(row=2, column=0)

        # password
        self.password = Entry(self, show="*", textvariable=f_userd.PASSWORD)
        self.password.grid(row=2, column=1)
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.grid(row=3, column=0, columnspan=2)
        # sign in
        Button(self, text="Sign in", command=self.login).grid(row=4, column=1)

    # login front action
    def login(self):

        from PAGES.p_search import p_search
        #check if user is login if is -> logout
        if (self.controller.session.session):
            self.controller.session.logout()
        #try login of user
        self.controller.session.login(self.LOGIN.get(), self.password.get())
        #check login status
        if (self.controller.session.session):
            self.controller.show_frame(p_search)
        else:
            self.errors['text'] = "This credentials are not correct"
    #basic action before show frame
    def run(self):
        #basic clear of frame
        self.errors['text'] = ""
        if self.controller.session.session:
            self.controller.session.logout()
