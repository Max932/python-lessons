from course import get_course
import tkinter

window = tkinter.Tk()
window.geometry("1920x1080")
window.title ("course of valute")

img_logo = tkinter.PhotoImage(file="C:/Users/Максим/Desktop/Explorer/projects/python-lessons/6th lesson/logo.png")
logo = tkinter.Label(image=img_logo)
logo.place (x=0,y=0)

lab = tkinter.Label (text="course of value \n MAXIMUM банк" , fg="pink" , font = "gabriola 22")
lab.place (x=150,y=25)

usd_course = tkinter.Label(text=f"$ {get_course('R01235')}", font = "gabriola 22")
usd_course.place(x=90,y=150)

eur_course = tkinter.Label(text=f"€ {get_course ('R01239')}",font= "gabriola 22")
eur_course.place (x=90 , y=190)
window.mainloop()