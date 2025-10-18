import tkinter
screen = tkinter.Tk()
screen.title("REGISTRATION FORM")
screen.geometry("500x300")
screen.config(bg = "beige")

name = tkinter.Label(screen, text = "Name").place(x = 30, y = 50)

email = tkinter.Label(screen, text = "Email").place(x = 30, y = 70)

phone_number = tkinter.Label(screen, text = "Phone_number").place(x = 30, y = 90)

comment = tkinter.Label(screen, text = "comment").place(x = 30, y = 150)

ent1 = tkinter.Entry(screen).place(x =150, y =50)
ent2 = tkinter.Entry(screen).place(x =150, y =80)
ent3 = tkinter.Entry(screen).place(x =150, y =110)
ent4 = tkinter.Text(screen, height= 4, width= 20).place(x=150, y=150)

bt = tkinter.Button(text = "click here!!!", bg = "black", fg="white").place(x = 150, y = 250)

bt = tkinter.Button(text = "exit", bg ="black", fg ="white").place(x = 260, y= 250)



screen.mainloop()









