from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk, Image

from Controllers.Setting import SettingsController
from Frames.rental import RentalPage


class ToolPage(Frame):
    dayfee = 0

    def __init__(self, parent, controller):
        from Frames.main import MainPage
        from Frames.result import ResultPage
        from Controllers.Tools import ToolController
        self.controller = controller
        self.tool = ToolController()
        Frame.__init__(self, parent)
        self.controller = controller
        Button(self, text="Logout", command=lambda: controller.show_frame(MainPage)).pack()
        # back
        Button(self, text="Back", command=lambda: controller.show_frame(ResultPage)).pack(pady=10, padx=10)
        Label(self, text="Tool Details", font=SettingsController.LARGE_FONT).pack(pady=10, padx=10)
        Label(self, text="Name:", font=SettingsController.SMALL_FONT).pack()
        self.name = Label(self, text="Name:", font=SettingsController.SMALL_FONT)
        self.name.pack()
        Label(self, text="Description:", font=SettingsController.SMALL_FONT).pack()
        self.description = Label(self, text="Name:", font=SettingsController.SMALL_FONT)
        self.description.pack()
        Label(self, text="photos:", font=SettingsController.SMALL_FONT).pack()
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=True)

        Label(self, text="Price:", font=SettingsController.SMALL_FONT).pack()
        self.price = Label(self, text="Name:", font=SettingsController.SMALL_FONT)
        self.price.pack()
        Button(self, text="Rent", command=self.rental).pack(pady=10, padx=10)

    def run(self):
        tools = self.tool.search_by_name(self.controller.selectedtool)
        for child in self.frame.winfo_children():
            child.destroy()
        tool = tools[0]
        self.dayfee = tool["price"]
        self.name["text"] = tool["name"]
        self.price["text"] = tool["price"]
        self.controller.selectedtoolid = tool["id"]
        self.description["text"] = tool["description"]

        for photo in tool["photos"]:
            avatar_file = ImageTk.PhotoImage(Image.open((photo)).resize((100, 50), Image.ANTIALIAS))
            avatar = Label(self.frame, image=avatar_file)
            avatar.image = avatar_file
            avatar.config(image=avatar_file)
            avatar.pack()

    def rental(self):
        self.controller.price = self.dayfee

        self.controller.show_frame(RentalPage)
