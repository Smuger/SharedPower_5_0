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
        self.avatar = Label(self)
        self.avatar.pack(pady=50, padx=10)
        avatar_file = ImageTk.PhotoImage(Image.open('RES/logo/logo.png').resize((256, 256), Image.ANTIALIAS))
        self.avatar.image = avatar_file
        self.avatar.config(image=avatar_file)

        # topic
        Label(self, text="Welcome to SharedPower", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # sign up
        Button(self, text="Sing up", command=lambda: controller.show_frame(p_signup)).pack(pady=10, padx=10)
        Label(self, text="Login:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # SettingsController.LOGIN
        self.LOGIN = Entry(self, textvariable=f_userd.LOGIN)
        self.LOGIN.pack()
        Label(self, text="Password:", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # password
        self.password = Entry(self, show="*", textvariable=f_userd.PASSWORD)
        self.password.pack()
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()
        # sign in
        Button(self, text="Sign in", command=self.login).pack(pady=10, padx=10)

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
            self.errors['text'] = "Password and Login doesn't match to any user."
    #basic action before show frame
    def run(self):
        #basic clear of frame
        self.errors['text'] = ""
        if self.controller.session.session:
            self.controller.session.logout()
