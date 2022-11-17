from time import sleep
from tkinter import *
from tkinter import ttk
from playsound import playsound
import simpleaudio as sa
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




class songplot:
    def play(self):
        # Play the song
        print("Playing song")
        wave_obj = sa.WaveObject.from_wave_file(self.wfdata["filename"])
        play_obj = wave_obj.play()
        while play_obj.is_playing():
            # Update the progress bar
            self.window.progress["value"] = play_obj.get_progress() * 100
            # Update the label
            self.window.label["text"] = "Song length: " + str(self.wfdata["frames"] / float(self.wfdata["rate"])) + " seconds, progress: " + str(play_obj.get_progress() * 100) + "%"
            # Update the window
            self.window.update()
            # Print the progress
            print(play_obj.get_progress())
            # Sleep for 0.1 seconds
            sleep(0.1)
            pass    

        playsound("./wav/sample.wav")
    def __init__(self, data, wfdata):
        self.data=data
        self.wfdata=wfdata
        # Create the window
        window = Tk()
        # Set the title
        window.title("Waveform")
        # Set the size
        window.geometry("800x400")
        # Create progress bar
        window.progress = ttk.Progressbar(window, orient=HORIZONTAL, length=2800, mode="determinate")
        window.progress.grid(row=1, column=0)
        # Create button to start the song
        window.button = Button(window, text="Play", command=self.play)
        window.button.grid(row=2, column=0)
        # Create label with the song length in seconds
        window.label = Label(window, text="Song length: " + str(self.wfdata["frames"] / float(self.wfdata["rate"])) + " seconds")
        window.label.grid(row=3, column=0)
        # Create the canvas
        canvas = Canvas(window, width=800, height=400)
        # Draw the waveform
        ltr=[0]*10000 
        for i in range(0, len(data), 2):
            # Get the sample
            sample = int.from_bytes(data[i:i+2], byteorder="little", signed=True)
            # Get the sample value
            samplevalue = sample / 32768
            # Get the x coordinate
            x = i / 2 / wfdata["channels"] / wfdata["width"] / wfdata["rate"] * 800
            # Draw the sample
            canvas.create_line(x, 300, x, 300 - samplevalue * 300, fill="red")
        # Draw the canvas
        #canvas.grid(column=0, row=0)
        # Start the main loop
        window.mainloop()

def read(filename):
    wf=wave.open(filename, "r")
    wfdata={
        "filename": filename,
        "channels": wf.getnchannels(),
        "width": wf.getsampwidth(),
        "rate": wf.getframerate(),
        "frames": wf.getnframes()#,
        #"comptype": wf.getcomptype(),
        #"compname": wf.getcompname()
    }
    data=wf.readframes(wfdata["frames"])
    wf.close()
    print(wfdata)
    sp=songplot(data, wfdata)
    return wfdata

class GUI:
    def generate(o):
        print("Generating...")
        write(o.filename.get(), o.data.get(), o.rate.get(), o.channels.get(), o.width.get())
        print("Done!")

    def readfile(o):
        print("Reading file...")
        file=read(o.filename.get())
        print(file)
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
        o.filename.insert(0, "./wav/sample.wav")
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
        o.readfile = Button(o.root, text="Read file", command=o.readfile)
        o.readfile.grid(row=5, column=1)
        o.root.mainloop()

o=GUI()



