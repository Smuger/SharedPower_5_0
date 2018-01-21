# import tkinter
from tkinter import *
from tkinter.ttk import *

class p_start(Frame):
    def __init__(self, parent, controller):
        # define controller
        self.controller = controller

        #import page
        from PAGES.p_signup import p_signup
        # import functionality
        from FUNC.f_userd import f_userd

        Frame.__init__(self, parent)

        # choose image file and load it
        self.logo = PhotoImage(file="RES/logo/logo.png")
        self.label = Label(self, image=self.logo)
        self.label.image = self.logo
        self.label.grid(row=0, column=0, columnspan=2)


        # signup
        Button(self, text="Sing up", command=lambda: controller.show_frame(p_signup)).grid(row=4, column=0, sticky=EW)

        # signin
        Label(self, text="Login:", font=f_userd.LARGE_FONT).grid(row=1, column=0)
        self.LOGIN = Entry(self, textvariable=f_userd.LOGIN)
        self.LOGIN.grid(row=1, column=1)
        Label(self, text="Password:", font=f_userd.LARGE_FONT).grid(row=2, column=0)
        self.password = Entry(self, show="*", textvariable=f_userd.PASSWORD)
        self.password.grid(row=2, column=1)
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.grid(row=3, column=0, columnspan=2)
        Button(self, text="Sign in", command=self.login).grid(row=4, column=1)


    def login(self):
        # import page
        from PAGES.p_search import p_search

        # login validation
        if (self.controller.session.session):
            self.controller.session.logout()
        self.controller.session.login(self.LOGIN.get(), self.password.get())

        # wrong credentials
        if (self.controller.session.session):
            self.controller.show_frame(p_search)
        else:
            self.errors['text'] = "This credentials are not correct"
    # cleanup
    def run(self):
        self.errors['text'] = ""
        if self.controller.session.session:
            self.controller.session.logout()
