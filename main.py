from tkinter import *
from farmer import skillCast, buffCast

running = True  # Global flag
idx = 0  # loop index

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

root = Tk()
root.title("My Cute Maple Farmer")
root.geometry("580x180")

app = Frame(root)
app.grid()

instruction1 = Label(app, text="Use this at your own risk.")
instruction2 = Label(app, text="If the Emulator & the program is burning your PC, STOP it!")
start = Button(app, text="Start Farming", command=start)
stop = Button(app, text="Stop Farming", command=stop)
instruction3 = Label(app, text="Memory might build up over time. Please spam click on Stop Farming continuously if the program freezed.")
instruction4 = Label(app, text="If you realise your PC is slowing down abnormally after terminating the program, kindly reboot it.")

instruction1.grid()
instruction2.grid()
start.grid()
stop.grid()
instruction3.grid()
instruction4.grid()

buffCast()
while True:
    if idx % 500 == 0:
        root.update()

    if running:
        skillCast()
