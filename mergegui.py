from tkinter import filedialog
from tkinter import *
import merge as mg
from tkinter import messagebox



files_to_merge = []

window = Tk()

def verify_output_file_not_exist(output):
    return os.path.exists(output)


class DragDropListbox(Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = SINGLE
        Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i

def add_file():
    fn = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    if not fn:
        return
    files_to_merge.append(fn)
    print(files_to_merge)
    listbox.insert(END, fn)


def merge_pdfs():
    fn = ""
    if verify_output_file_not_exist:
        messagebox.showerror("File exists", "Error. File already exists. Try again with a different filename.")
        return
    if not e.get().endswith(".pdf"):
        fn = e.get() + ".pdf"
    else:
        fn = e.get()
    mg.merge_files(listbox.get(0, END), fn)
    messagebox.showinfo("File merged","Saved output file " + fn)

window.geometry('400x300')
window.title("Adub Akrebut PDF Merger")

listbox = DragDropListbox(window, width=300)
listbox.pack()

b = Button(window, text="Add file", command=add_file)
b.pack()
b2 = Button(window, text="Merge pdf", command=merge_pdfs)
b2.pack()
e = Entry(window)
e.insert(0, "outputfile.pdf")
e.pack()





mainloop()

#btn = Button(window, text="Add file", command=add_file)
 
#btn.grid(column=1, row=0)
 
window.mainloop()


#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
#print (root.filename)
