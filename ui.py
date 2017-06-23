from tkinter import *
from tkinter.scrolledtext import ScrolledText

#top = Tk()
#btn = Button()
#btn['text'] = 'Click me!'
#btn.pack()

def clicked():
	print('I ws clicked!')

#btn['command'] = clicked
#btn.config(text = 'Click me!', command = clicked)

#Button(text = 'Click me!', command = clicked).pack()
#Label(text = 'I am in the first window!').pack()
#second = Toplevel()
#Label(second, text = 'I am in the second window!').pack()
#for i in range(10):
#	Button(text=i).pack()

def  callback(event):
	print(event.x, event.y)

#top.bind('<Burron-1>', callback)

def load():
	with open(filename.get()) as file:
		contents.delete('1.0', END)
		contents.insert(INSERT, file.read())

def save():
	with open(filename.get(), 'w') as file:
		file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)
Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()