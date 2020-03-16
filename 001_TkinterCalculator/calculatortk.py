from tkinter import *
from math import *
from fractions import Fraction

window = Tk()
window.geometry("400x600+80+80")
window.configure(bg="black")
window.title("Basic Calculator")

expression = ""
answer = 0
localanswer = 0  # saved answer
length = 0


def press(key):
    global expression
    global length
    expression += str(key)
    if length == 20:
        expression = ""
        length = 0
    main_label.configure(text=expression)
    length += 1


def equal():
    global answer
    global localanswer
    global expression
    answer = str(eval(expression))
    localanswer = answer
    if len(answer) > 18:
        answer = answer[:4]
    elif expression.find("/") >= 1:
        answer = str(eval(expression))
        answer = str(Fraction(answer))
    main_label.configure(text=answer)
    expression = str(answer)


def clear():
    global answer
    global expression
    answer = 0
    expression = ""
    main_label.configure(text="")


def answer_button():
    global localanswer
    global expression
    expression += str(localanswer)
    main_label.configure(text=str(localanswer))


def decimal():
    global expression
    global answer
    global localanswer
    answer = str(eval(expression))
    localanswer = answer
    main_label.configure(text=str(answer))
    expression = answer


def fraction():
    global expression
    global answer
    global localanswer
    answer = str(Fraction(expression))
    localanswer = answer
    main_label.configure(text=str(answer))
    expression = answer


def delete():
    global expression
    expression = expression[:-1]
    main_label.configure(text=expression)


num0 = Button(window, bg="#1E2A2E", fg="black", text="0",
              font=("Courier", 40), command=lambda: press(0))
num0.place(x=0, y=500, height=100, width=100)

num1 = Button(window, bg="#1E2A2E", fg="black", text="1",
              font=("Courier", 40), command=lambda: press(1))
num1.place(x=0, y=400, height=100, width=100)
num2 = Button(window, bg="#1E2A2E", fg="black", text="2",
              font=("Courier", 40), command=lambda: press(2))
num2.place(x=100, y=400, height=100, width=100)

num3 = Button(window, bg="#1E2A2E", fg="black", text="3",
              font=("Courier", 40), command=lambda: press(3))
num3.place(x=200, y=400, height=100, width=100)

num4 = Button(window, bg="#1E2A2E", fg="black", text="4",
              font=("Courier", 40), command=lambda: press(4))
num4.place(x=0, y=300, height=100, width=100)

num5 = Button(window, bg="#1E2A2E", fg="black", text="5",
              font=("Courier", 40), command=lambda: press(5))
num5.place(x=100, y=300, height=100, width=100)

num6 = Button(window, bg="#1E2A2E", fg="black", text="6",
              font=("Courier", 40), command=lambda: press(6))
num6.place(x=200, y=300, height=100, width=100)

num7 = Button(window, bg="#1E2A2E", fg="black", text="7",
              font=("Courier", 40), command=lambda: press(7))
num7.place(x=0, y=200, height=100, width=100)

num8 = Button(window, bg="#1E2A2E", fg="black", text="8",
              font=("Courier", 40), command=lambda: press(8))
num8.place(x=100, y=200, height=100, width=100)

num9 = Button(window, bg="#1E2A2E", fg="black", text="9",
              font=("Courier", 40), command=lambda: press(9))
num9.place(x=200, y=200, height=100, width=100)
dot = Button(window, bg="#1E2A2E", fg="black", text=".",
             font=("Courier", 40), command=lambda: press("."))
dot.place(x=100, y=500, height=100, width=100)

C = Button(window, bg="#1E2A2E", fg="black", text="C",
           font=("Courier", 40), command=delete)
C.place(x=50, y=100, height=100, width=50)

CE = Button(window, bg="#1E2A2E", fg="black", text="CE",
            font=("Courier", 30), command=clear)
CE.place(x=0, y=100, height=100, width=50)

ANS = Button(window, bg="#1E2A2E", fg="black", text="ANS",
             font=("Courier", 30), command=answer_button)
ANS.place(x=200, y=100, height=100, width=100)

F = Button(window, bg="#1E2A2E", fg="black", text="F",
           font=("Courier", 35), command=fraction)
F.place(x=150, y=100, height=100, width=50)

D = Button(window, bg="#1E2A2E", fg="black", text="D",
           font=("Courier", 35), command=decimal)
D.place(x=100, y=100, height=100, width=50)

add_button = Button(window, bg="#1E2A2E", fg="black", text="+",
                    font=("Times", 40), command=lambda: press("+"))
add_button.place(x=300, y=400, height=100, width=100)

min_button = Button(window, bg="#1E2A2E", fg="black", text="-",
                    font=("Courier", 40), command=lambda: press("-"))
min_button.place(x=300, y=300, height=100, width=100)

mul_button = Button(window, bg="#1E2A2E", fg="black", text="x",
                    font=("Courier", 40), command=lambda: press("*"))
mul_button.place(x=300, y=200, height=100, width=100)

div_button = Button(window, bg="#1E2A2E", fg="black", text="÷",
                    font=("Courier", 40), command=lambda: press("/"))
div_button.place(x=300, y=100, height=100, width=100)

equals = Button(window, bg="#1E2A2E", fg="black", text="=",
                font=("Times", 40), command=equal)
equals.place(x=300, y=500, height=100, width=100)

bracket1 = Button(window, bg="#1E2A2E", fg="black", text="(",
                  font=("Times", 40), command=lambda: press("("))
bracket1.place(x=200, y=500, height=100, width=50)

bracket2 = Button(window, bg="#1E2A2E", fg="black", text=")",
                  font=("Times", 40), command=lambda: press(")"))
bracket2.place(x=250, y=500, height=100, width=50)

main_label = Label(window, bg="#6c7175", fg="black",
                   font=("Courier", 40), text="0")
main_label.place(x=0, y=0, height=100, width=500)

window.mainloop()
