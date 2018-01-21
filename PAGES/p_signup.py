from tkinter import *
from tkinter.ttk import *


class p_signup(Frame):
    file_opt = ""
    avatar = ""

    def __init__(self, parent, controller):
        from FUNC.f_userd import f_userd
        from PAGES.p_start import p_start
        from FUNC.f_file import f_file

        Frame.__init__(self, parent)
        self.controller = controller
        self.file = f_file()

        # topic
        Label(self, text="Welcome to SharedPower", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_start)).pack(pady=10, padx=10)

        # SettingsController.LOGIN
        Label(self, text="Login:", font=f_userd.SMALL_FONT).pack()
        self.LOGIN = Entry(self, textvariable=f_userd.LOGIN_NEW)
        self.LOGIN.pack()

        Label(self, text="Email:", font=f_userd.SMALL_FONT).pack()
        self.EMAIL = Entry(self, textvariable=f_userd.EMAIL_NEW)
        self.EMAIL.pack()

        Label(self, text="Postcode:", font=f_userd.SMALL_FONT).pack()
        self.POSTCODE = Entry(self, textvariable=f_userd.POSTCODE_NEW)
        self.POSTCODE.pack()

        Label(self, text="Address:", font=f_userd.SMALL_FONT).pack()
        self.ADDRESS = Entry(self, textvariable=f_userd.ADDRESS_NEW)
        self.ADDRESS.pack()

        Label(self, text="Card owner name:", font=f_userd.SMALL_FONT).pack()
        self.CARD_OWNER = Entry(self, textvariable=f_userd.CARD_OWNER_NEW)
        self.CARD_OWNER.pack()

        Label(self, text="Card number:", font=f_userd.SMALL_FONT).pack()
        self.CARD_NUMBER = Entry(self, textvariable=f_userd.CARD_NUMBER_NEW)
        self.CARD_NUMBER.pack()

        Label(self, text="Card security code:", font=f_userd.SMALL_FONT).pack()
        self.CARD_SECURITY_CODE = Entry(self, textvariable=f_userd.CARD_SECURITY_CODE_NEW)
        self.CARD_SECURITY_CODE.pack()

        Label(self, text="Card expiration date:", font=f_userd.SMALL_FONT).pack()
        self.CARD_EXPIRATION_DATE = Entry(self, textvariable=f_userd.CARD_EXPIRATION_DATE_NEW)
        self.CARD_EXPIRATION_DATE.pack()

        Label(self, text="Avatar:", font=f_userd.SMALL_FONT).pack()
        Button(self, text='Browse', command=self.askopenfile).pack()
        self.path = Label(self, text="", font=f_userd.SMALL_FONT)
        self.path.pack()


        # password
        Label(self, text="Password:", font=f_userd.SMALL_FONT).pack()
        self.password = Entry(self, show="*", textvariable=f_userd.PASSWORD_NEW)
        self.password.pack()

        Label(self, text="Password again:", font=f_userd.SMALL_FONT).pack()
        self.repeatpassword = Entry(self, show="*", textvariable=f_userd.PASSWORD_NEW)
        self.repeatpassword.pack()
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()

        # Sign in
        Button(self, text="Sign up", command=self.register).pack(pady=10, padx=10)

    def register(self):
        from PAGES.p_start import p_start
        if (self.password.get() == self.repeatpassword.get()):
            from FUNC.f_users import f_users
            user = f_users()
            if (user.checklogin(self.LOGIN.get())):
                if (self.avatar != ""):

                    user.create_account(self.LOGIN.get(), self.EMAIL.get(), self.POSTCODE.get(), self.ADDRESS.get(), self.CARD_OWNER.get(), self.CARD_NUMBER.get(), self.CARD_SECURITY_CODE.get(), self.CARD_EXPIRATION_DATE.get(), self.password.get(), self.avatar)
                    self.controller.show_frame(p_start)
                else:
                    self.errors['text'] = "Upload of avatar is required"
            else:
                self.errors['text'] = "Login already exists"

        else:
            self.errors['text'] = "Password are not the same"
    def show_path(self):
        self.path["text"] = self.avatar

    def askopenfile(self):
        self.avatar = self.file.uploadfile()
        self.show_path()



    def run(self):
        pass
