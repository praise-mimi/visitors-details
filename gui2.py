
import tkinter 

screen = tkinter.Tk()
screen.title("TESTING!!!")
screen.geometry("500x300")
screen.config(bg = "pink")

name = tkinter.Label(screen, text = "Name").place(x = 30, y = 50)

email = tkinter.Label(screen, text = "Email").place(x = 30, y= 90)

ent1 = tkinter.Entry(screen).place(x =80, y =50)
ent2 = tkinter.Entry(screen).place(x=80, y =90)








screen.mainloop()