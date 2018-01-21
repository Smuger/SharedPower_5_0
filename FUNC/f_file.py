# import file handler lib
from shutil import copy2
from tkinter import filedialog

# import functionality
from FUNC.f_userd import f_userd

class f_file:

    # change dir of a file
    def uploadfile(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        return copy2(path, f_userd.UPLOADPATH).replace("\\", "/")
    # add photo to array
    def uploadphotos(self):
        photolist = []
        filez = filedialog.askopenfilenames(initialdir="/", title="Select photos",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        # move
        for file in filez:
            photo = copy2(file, f_userd.UPLOADPATH).replace("\\", "/")
            photolist.append(photo)
        return photolist