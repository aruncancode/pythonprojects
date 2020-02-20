import nltk
from nltk.corpus import words
from tkinter import *
import random

words_list = words.words()
new_words = []


window = Tk()
window.geometry("400x600+80+80")
window.configure(bg="light grey")
window.title("Word Generator")


def search_words(starts1, contains1, ends1):
	global new_words
	new_words = []
	starts(starts1)
	ends(ends1)
	contains(contains1)

def starts(starts):
	global new_words, words_list
	for starting in words_list:
		if starts != "":
			if starting[0] == starts:
				new_words.append(starting)
		else:
			new_words.append(words_list)
	print(len(new_words))

def ends(ends):
	global new_words
	iterwords = new_words
	for endingletter in iterwords:
		if ends != "":
			if endingletter[-1] != ends:
				new_words.remove(endingletter)
	print(len(new_words))

def contains(contains):
	global new_words
	iterwords = new_words
	for containingletter in iterwords:
		if contains != "":
			if contains not in containingletter:
				new_words.remove(containingletter)
	print(len(new_words))

		

def new_word():
	global new_words
	GeneratedWord.configure(text=random.choice(new_words))

def getparams():
	starts = StartingLetter.get()
	contains = Contains.get()
	ends = Ending.get()
	search_words(starts,contains, ends)


Title = Label(window, bg="#6c7175", fg="white", font=("Courier", 24), text="Random Word Generator")
Title.place(x=0, y=0)

StartingTitle = Label(window, text='Starting Letter')
StartingTitle.place(x=100, y=120)
StartingLetter = Entry(window)
StartingLetter.place(x=190, y=120)

ContainsTitle = Label(window, text='Contains')
ContainsTitle.place(x=100, y=150)
Contains = Entry(window)
Contains.place(x=190, y=150)

EndingTitle = Label(window, text='Ending Letter')
EndingTitle.place(x=100, y=180)
Ending = Entry(window)
Ending.place(x=190, y=180)

Generate = Button(window, bg="#6c7175", fg="white", font=("Courier", 24), text="Generate", command=getparams)
Generate.place(x=20, y=300, height=80, width=180)

NewWord = Button(window, bg="#6c7175", fg="white", font=("Courier", 24), text="New", command=new_word)
NewWord.place(x=200, y=300, height=80, width=180)

GeneratedWord = Label(window, bg="#6c7175", fg="white", font=("Courier", 24))
GeneratedWord.place(x=0, y=400, height=80, width=400)



window.mainloop()
