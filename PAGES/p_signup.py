from tkinter import *
from tkinter.ttk import *


class SignUpPage(Frame):
    file_opt = ""
    avatar = ""

    def __init__(self, parent, controller):
        from Controllers.Setting import SettingsController
        from Frames.main import MainPage
        from Controllers.File import FileController

        Frame.__init__(self, parent)
        self.controller = controller
        self.file = FileController()
        # topic
        Label(self, text="Welcome to SharedPower", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(MainPage)).pack(pady=10, padx=10)

        # SettingsController.LOGIN
        Label(self, text="Login:", font=SettingsController.SMALL_FONT).pack()
        self.LOGIN = Entry(self, textvariable=SettingsController.LOGIN_NEW)
        self.LOGIN.pack()
        Label(self, text="Avatar:", font=SettingsController.SMALL_FONT).pack()
        Button(self, text='Browse', command=self.askopenfile).pack()
        # password
        Label(self, text="Password:", font=SettingsController.SMALL_FONT).pack()
        self.password = Entry(self, show="*", textvariable=SettingsController.PASSWORD_NEW)
        self.password.pack()
        Label(self, text="Password again:", font=SettingsController.SMALL_FONT).pack()
        self.repeatpassword = Entry(self, show="*", textvariable=SettingsController.PASSWORD_NEW)
        self.repeatpassword.pack()
        self.errors = Label(self, text="", font=SettingsController.SMALL_FONT)
        self.errors.pack()

        # Sign in
        Button(self, text="Sign up", command=self.register).pack(pady=10, padx=10)

    def register(self):
        from Frames.main import MainPage
        if (self.password.get() == self.repeatpassword.get()):
            from Controllers.User import UserController
            user = UserController()
            if (user.checklogin(self.LOGIN.get())):
                if (self.avatar != ""):

                    user.create_account(self.LOGIN.get(), self.password.get(), self.avatar)
                    self.controller.show_frame(MainPage)
                else:
                    self.errors['text'] = "Upload of avatar is required"
            else:
                self.errors['text'] = "Login already exists"

        else:
            self.errors['text'] = "Password are not the same"

    def askopenfile(self):

        self.avatar = self.file.uploadfile()

    def run(self):
        pass
