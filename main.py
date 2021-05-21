# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import ANCHOR, END, Tk, BOTH, W, E
from tkinter.ttk import Frame, Button, Label, Entry
from typing import List

from rasp_pi_connection import Picframe


def get_list_of_directories():
    # process = subprocess.run(
    #     ["ssh", "pi@picframe", "ls /media/microserver/images"], stdout=subprocess.PIPE
    # )
    # folders = process.stdout.decode("utf-8")
    #
    # folder_list = folders.split("\n")

    folder_list = ["one", "two", "three"]
    return folder_list


def generate_command() -> List[str]:
    command = [
        "ssh",
        "pi@picframe",
        "poetry run python PySpace/photo_frame/start_slideshow.py",
    ]

    return command


class Gui(Frame):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.slideshow_delay_btn = None
        self.left_listbox = None
        self.right_listbox = None
        self.picframe = Picframe()

        self.initUI()

    def initUI(self):

        self.master.title("Photo Frame Gui")
        self.pack(fill=BOTH, expand=True)

        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Photo Frame")
        lbl.grid(sticky=W, pady=0, padx=5)

        self.left_listbox = tk.Listbox(self)
        self.left_listbox.grid(
            row=1, column=0, columnspan=1, rowspan=4, padx=0, sticky=W
        )
        for i, v in enumerate(self.picframe.get_directory_contents()):
            self.left_listbox.insert(i, v)

        self.right_listbox = tk.Listbox(self)
        self.right_listbox.grid(
            row=1, column=2, columnspan=1, rowspan=4, padx=0, sticky=W
        )

        right_btn = Button(self, text="-->", command=self.on_shift_right_click)
        right_btn.grid(row=2, column=1)

        left_btn = Button(self, text="Remove Item", command=self.on_shift_left_click)
        left_btn.grid(row=3, column=1, pady=2)

        load_btn = Button(
            self, text="Show on Photo Frame", command=self.on_load_btn_click
        )
        load_btn.grid(row=1, column=5)

        self.slideshow_delay_btn = Entry(self)
        self.slideshow_delay_btn.grid(row=2, column=5, sticky=E, padx=5)

    def on_load_btn_click(self):
        print("hello world")

        print(self.slideshow_delay_btn.get())

    def on_slideshow_delay_entry(self):
        print("slideshow delay entry")

    def on_shift_right_click(self):
        self.right_listbox.insert(END, self.left_listbox.get(ANCHOR))

    def on_shift_left_click(self):
        self.right_listbox.delete(ANCHOR)

    # noinspection PyUnusedLocal
    def close(self, event=None):
        self.picframe.close()
        self.root.destroy()
        print("window closed")


def main():

    root = Tk()
    root.geometry("500x500+700+300")
    g = Gui(root)
    root.protocol("WM_DELETE_WINDOW", g.close)
    root.bind("<Escape>", g.close)
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
