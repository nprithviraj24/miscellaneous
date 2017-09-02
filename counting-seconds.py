import tkinter as tk #Comes out of the box with python 3.x intrepreter

#Using GUI methods in Tkinter library
counter = 0
count2 = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
    # count2 = 0
    # def countingTwoSeconds():
    #     global count2
    #     count2 +=1
    #     label.config(text=str(count2))
    #     label.after(2000, count2)
    # countingTwoSeconds()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark blue")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command = root.destroy)
button.pack()
root.mainloop() #running the main loop.



