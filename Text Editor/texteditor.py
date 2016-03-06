from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)
    if (event.char == "\x7f"):
    	var.set(var.get()[:-1])
    else:
	    var.set(var.get() + event.char)
	    label.pack()

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
var = StringVar()
label = Label(root, anchor=W, justify=LEFT, padx=0, pady=0, textvariable=var)
label.pack
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

if not self.e.get().isdigit():
     #get the length of the string in the widget, and subtract one, and delete everything up to the end
     self.e.delete(len(self.e.get)-1, tk.END)