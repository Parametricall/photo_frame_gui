# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import tkinter as tk


def get_list_of_directories():
    process = subprocess.run(
        ["ssh", "pi@picframe", "ls /media/microserver/images"], stdout=subprocess.PIPE
    )
    folders = process.stdout.decode("utf-8")

    folder_list = folders.split("\n")
    return folder_list


class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500+0+0")
        self.config(bg="skyblue")
        self.bind("<Escape>", self.destroy)

        self.file_list = tk.Listbox(self)

        directories = get_list_of_directories()
        for index, dir_name in enumerate(directories):
            self.file_list.insert(index, dir_name)

        self.file_list.pack()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
