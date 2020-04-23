from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

chatbot = ChatBot("Humanoid")

conversation = [
    'Hello',
    'Hi There !',
    'what is your name ?',
    'My name is Humanoid , i am created by Atif !',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Chhindwara',
    'In which language you talk?',
    ' I mostly talk in English'
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

main = Tk()
main.title("ChatBot")
main.geometry("450x600")
img = PhotoImage(file="bot.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "BOT : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=90, height=15, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Bot", font=("Verdana", 15), command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)
main.mainloop()
