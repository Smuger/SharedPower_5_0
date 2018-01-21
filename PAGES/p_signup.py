# import tkinter
from tkinter import *
from tkinter.ttk import *

class p_signup(Frame):

    # storage
    file_opt = ""
    avatar = ""

    def __init__(self, parent, controller):

        # import page
        from PAGES.p_start import p_start
        # import functionality
        from FUNC.f_userd import f_userd
        from FUNC.f_file import f_file

        Frame.__init__(self, parent)

        # define controller and file
        self.controller = controller
        self.file = f_file()

        # hello
        Label(self, text="Welcome to SharedPower", font=f_userd.LARGE_FONT).pack(pady=10, padx=10)

        # back
        Button(self, text="Back", command=lambda: controller.show_frame(p_start)).pack(pady=10, padx=10)

        # login
        Label(self, text="Login:", font=f_userd.SMALL_FONT).pack()
        self.LOGIN = Entry(self, textvariable=f_userd.LOGIN_NEW)
        self.LOGIN.pack()

        # email
        Label(self, text="Email:", font=f_userd.SMALL_FONT).pack()
        self.EMAIL = Entry(self, textvariable=f_userd.EMAIL_NEW)
        self.EMAIL.pack()

        # postcode
        Label(self, text="Postcode:", font=f_userd.SMALL_FONT).pack()
        self.POSTCODE = Entry(self, textvariable=f_userd.POSTCODE_NEW)
        self.POSTCODE.pack()

        # address
        Label(self, text="Address:", font=f_userd.SMALL_FONT).pack()
        self.ADDRESS = Entry(self, textvariable=f_userd.ADDRESS_NEW)
        self.ADDRESS.pack()

        # card owner
        Label(self, text="Card owner name:", font=f_userd.SMALL_FONT).pack()
        self.CARD_OWNER = Entry(self, textvariable=f_userd.CARD_OWNER_NEW)
        self.CARD_OWNER.pack()

        # card number
        Label(self, text="Card number:", font=f_userd.SMALL_FONT).pack()
        self.CARD_NUMBER = Entry(self, textvariable=f_userd.CARD_NUMBER_NEW)
        self.CARD_NUMBER.pack()

        # card security
        Label(self, text="Card security code:", font=f_userd.SMALL_FONT).pack()
        self.CARD_SECURITY_CODE = Entry(self, textvariable=f_userd.CARD_SECURITY_CODE_NEW)
        self.CARD_SECURITY_CODE.pack()

        # card expiration
        Label(self, text="Card expiration date:", font=f_userd.SMALL_FONT).pack()
        self.CARD_EXPIRATION_DATE = Entry(self, textvariable=f_userd.CARD_EXPIRATION_DATE_NEW)
        self.CARD_EXPIRATION_DATE.pack()

        # avatar
        Label(self, text="Avatar:", font=f_userd.SMALL_FONT).pack()
        Button(self, text='Browse', command=self.askopenfile).pack()
        self.path = Label(self, text="", font=f_userd.SMALL_FONT)
        self.path.pack()

        # password
        Label(self, text="Password:", font=f_userd.SMALL_FONT).pack()
        self.password = Entry(self, show="*", textvariable=f_userd.PASSWORD_NEW)
        self.password.pack()

        # password check
        Label(self, text="Password again:", font=f_userd.SMALL_FONT).pack()
        self.repeatpassword = Entry(self, show="*", textvariable=f_userd.PASSWORD_NEW)
        self.repeatpassword.pack()
        self.errors = Label(self, text="", font=f_userd.SMALL_FONT)
        self.errors.pack()

        # sign up
        Button(self, text="Sign up", command=self.register).pack(pady=10, padx=10)

    def register(self):

        # import page
        from PAGES.p_start import p_start

        # check if both passwords are correct
        if (self.password.get() == self.repeatpassword.get()):

            # import functionality
            from FUNC.f_users import f_users

            # define user
            user = f_users()

            # check if login is available
            if (user.checklogin(self.LOGIN.get())):

                # check if avatar is empty
                if (self.avatar != ""):
                    user.create_account(self.LOGIN.get(), self.EMAIL.get(), self.POSTCODE.get(), self.ADDRESS.get(), self.CARD_OWNER.get(), self.CARD_NUMBER.get(), self.CARD_SECURITY_CODE.get(), self.CARD_EXPIRATION_DATE.get(), self.password.get(), self.avatar)
                    self.controller.show_frame(p_start)
                else:
                    self.errors['text'] = "Please choose your avatar"
            else:
                self.errors['text'] = "This login already exist"
        else:
            self.errors['text'] = "Password is not the same"

    # show path of avatar file
    def show_path(self):
        self.path["text"] = self.avatar

    # define uploaded file
    def askopenfile(self):
        self.avatar = self.file.uploadfile()
        self.show_path()

    # cleanup
    def run(self):
        pass
