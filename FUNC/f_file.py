from shutil import copy2
from tkinter import filedialog

from FUNC.f_userd import f_userd


class f_file:
    def uploadfile(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        print(path)
        print(f_userd.UPLOADPATH)
        return copy2(path, f_userd.UPLOADPATH).replace("\\", "/")
    #upload mutiple files
    def uploadphotos(self):
        #list of path to photos
        photolist = []
        #open file dialog
        filez = filedialog.askopenfilenames(initialdir="/", title="Select photos",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        #change path to correct for tkinter
        for file in filez:
            photo = copy2(file, f_userd.UPLOADPATH).replace("\\", "/")
            photolist.append(photo)
            #return corrected list of photos
        return photolist