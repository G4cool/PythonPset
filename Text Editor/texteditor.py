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

def donothing():
	print "donothing"

def file_save():
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.

menubar=Menu(root)
frame = Frame(root, width=1000, height=500)
var = StringVar()
label = Label(root, anchor=NW, justify=LEFT, padx=0, pady=0, textvariable=var)
label.pack()
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)

root.mainloop()