from tkinter import *
import wave


def write(filename, data, rate, channels, width):
    # Create a new wave file
    wf = wave.open(filename, "w")
    # Set the number of channels
    wf.setnchannels(int(channels))
    # Set the sample width
    wf.setsampwidth(int(width))
    # Set the frame rate
    wf.setframerate(int(rate))
    # Write the data to the file
    wf.writeframes(b"")
    # Close the file
    wf.close()

class GUI:
    def generate(o):
        print("Generating...")
        write(o.filename.get(), o.data.get(), o.rate.get(), o.channels.get(), o.width.get())
        print("Done!")

    def __init__(o):
        o.root = Tk()
        o.root.title("Waver")
        o.root.geometry("400x400")
        o.root.resizable(0, 0)
        o.filename_label = Label(o.root, text="Filename:")
        o.filename_label.grid(row=0, column=0)
        o.filename = Entry(o.root)
        o.filename.grid(row=0, column=1)
        o.rate_label = Label(o.root, text="Rate:")
        o.rate_label.grid(row=1, column=0)
        o.rate = Entry(o.root)
        o.rate.grid(row=1, column=1)
        o.channels_label = Label(o.root, text="Channels:")
        o.channels_label.grid(row=2, column=0)
        o.channels = Entry(o.root)
        o.channels.grid(row=2, column=1)
        o.width_label = Label(o.root, text="Width:")
        o.width_label.grid(row=3, column=0)
        o.width = Entry(o.root)
        o.width.grid(row=3, column=1)
        o.data_label = Label(o.root, text="Data:")
        o.data_label.grid(row=4, column=0)
        o.data = Entry(o.root)
        o.data.grid(row=4, column=1)
        o.generate = Button(o.root, text="Generate", command=o.generate)
        o.generate.grid(row=5, column=0) 
        o.root.mainloop()

o=GUI()