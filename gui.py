import tkinter

window = tkinter. Tk()
window.title('My GUI')
lab1 = tkinter.Label(window, text = "Visitors log", fg = "black").pack()
lab2 = tkinter.Label(text = "Hello Everybody!!!", bg = "White").pack() 

bt = tkinter.Button(text = "click here!!!", bg = "blue").pack()

txt = tkinter.Entry(width = 30).pack()
txt2 = tkinter.Text().pack()



window.mainloop()









