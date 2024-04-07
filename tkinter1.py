import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
window.title("Add two numbers")

def add():
    num1 = int(e.get())
    num2 = int(e1.get())
    l2 = tk.Label(window,text=num1+num2,font = "Times 18 bold").place(x = 230, y = 200)


l = tk.Label(window, text = "Enter first number here: ", font = "Times 18 bold").place(x = 40, y = 40)
e = tk.Entry(window)

l1 = tk.Label(window, text="Enter second number here: ",font= "Times 18 bold").place(x = 40, y = 90)
e1 = tk.Entry(window)

b = tk.Button(window,text="+",font= "Times 18 bold",command=add).place(x = 230, y = 140)
e.place(x = 300, y = 50 )
e1.place(x = 330, y = 100 )
window.mainloop()





















# import tkinter as tk
#
# window = tk.Tk()
# window.geometry("600x300")
# window.title("notepad")
#
# def clicked():
#     data = e.get()
#     l3 = tk.Label(window,text=data).place(x = 280, y = 150)
#
#
#
#
# l = tk.Label(window,text = "this is my first tkinter class",bg = "red",fg = "blue").place(x = 30, y = 50)
#
#
# l1 = tk.Label(window,text = "hello",font="Times 20 bold").pack()
# e = tk.Entry(window)
# b = tk.Button(window,text = "click",command=clicked).pack()
# e.pack()
# window.mainloop()