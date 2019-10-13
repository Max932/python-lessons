import tkinter 
import random
window = tkinter.Tk()
window.title("Твоё окно")
window.geometry("1920x1080")

label = tkinter.Label(text="0", bg="purple" , font = "gabriola 19")
label.place(x=10, y=10)

def random_color () :
    colors = ["red" , "gray" , "pink" , "violet" , "blue" , "black" , ""]
    label ["bg"] = random.choice (colors)

def count() :
    random_color()
    num = int (label["text"])
    num = num + 1
    label ["text"] = str (num)


button = tkinter.Button (text="click to change color",  bg="white" , font = "calibri 20" , command = count)
button.place (x=50, y=50)




window.mainloop()