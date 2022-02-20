from tkinter import *
from tkinter import filedialog

import captor
import resizer


video_path = ''
resize_len = ''


def openfile():
    global video_path
    video_path = filedialog.askopenfilename(filetypes=[
        ("all video format", ".mp4"),
        ("all video format", ".wmv"),
        ("text file", ".txt"),
        ("text file", ".csv")])
    if len(video_path) > 0:
        lbl_path.configure(text=video_path)
    #  print(video_path)


def capture_frames():
    img_name = cl_name.get()
    captor.main(video_path, img_name)
    lbl_status.configure(text="Process finished!")


def resize_frames():
    img_name = cl_name.get()
    resize_len = num_len.get()
    lbl_status.configure(text="PLEASE WAIT!!")
    resizer.main(video_path, resize_len, img_name)
    lbl_status.configure(text="Success!!")


if __name__ == '__main__':
    root = Tk(className=' Central')
    root.geometry("650x150")

    lbl_head = Label(root, text="Select a file and the process")
    lbl_head.grid(column=3, row=2)

    btn_visualizar = Button(root, text="Select file", command=openfile)
    btn_visualizar.grid(column=0, row=1, padx=5, pady=10, columnspan=1)

    lbl_info1 = Label(root, text="File:")
    lbl_info1.grid(column=2, row=1)

    lbl_path = Label(root, text="  Empty  ")
    lbl_path.grid(column=3, row=1)

    btn_capturar = Button(root, text="Capture", command=capture_frames)
    btn_capturar.grid(column=2, row=3)

    class_label = Label(root, text="Class name")
    class_label.grid(column=4, row=3)

    cl_name = StringVar()
    class_name = Entry(root, text='class name', textvariable=cl_name)
    class_name.grid(column=3, row=3)

    btn_resize = Button(root, text="Resize", command=resize_frames)
    btn_resize.grid(column=2, row=4)

    num_len = IntVar()
    number_len = Entry(root, text="new size", textvariable=num_len)
    number_len.grid(column=3, row=4)

    lbl_ex = Label(root, text="Ex. 40 = 80p x 80p ")
    lbl_ex.grid(column=4, row=4)

    lbl_status = Label(root, text="   ")
    lbl_status.grid(column=3, row=5)

    root.mainloop()
