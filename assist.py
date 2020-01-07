from time import sleep
from subprocess import Popen
from datetime import datetime
from googletrans import Translator
from random import randrange
from os import remove

jokes = ["Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.", "What is the difference between a well-dressed man on a unicycle and a poorly dressed man on a bicycle? Attire."]
rjokes = ["- Запомни, умный человек всегда во всём сомневается.\nТолько дурак может быть полностью уверенным в чём-то.\n- Ты уверен в этом?\n- Абсолютно.", "— Скажите, какова ваша методика написания диплома?\n— Crtl C, Ctrl V!", "Утром мать спрашивает дочь:\n- Что ночью упало с таким грохотом?\n- Одежда\n- А почему так громко?\n- Я не успела из нее вылезти...", "На чемпионате мира по плаванию тройку лидеров замкнул электрик Петров."]
hello = ["Hello to you to!", "Hi!", "Hi, how can I help you?", "Hello, how can I help you?", "Hi! How are you?", "How can I help you?", "How can I help?"]
goodbye = ["Goodbye to you to!", "See you later!", "Hope, I'll see you again!", "Waiting for help!"]
sorry = ["Sorry, I can't do that yet!", "Sorry, but I don't understand that!", "Sorry, I can't do that yet! Please, try another command."]
feeling = ["I'm fine, thank you!", "Very well, thanks!", "Very good, tank you! And you?"]
bad = [f"Why are you so {feeling}?", "What's wrong?", "What can I do for you?", "If you want to, I can make you laugh. Just say: \"Make me laugh.\""]
thanks = ["Glad you like it.", "You are welcome."]

lang = "en"

def show_text(text):
    return f"<div class='assistant'>{text}</div>"

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language=lang)
            if lang == "ru":
                print(f"Вы: {said}")
            else:
                print(f"You: {said}")
        except:
            if lang == "ru":
                print("Извините, но я вас не слышу.")
            else:
                print("Sorry, but I can't hear you.")

    return said

def note(text):
        date = datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        Popen(["notepad.exe", file_name])
        with open(file_name, "w") as f:
            f.write(text)

if lang == "ru":
    return show_text("Чем я могу вам помочь?")

else:
    return show_text("How can I help you?")

while True:        

    text = get_audio().lower()

    if lang == "en":
        if "remember" in text:
            return show_text("What do I need to remember?")
            global info
            info = get_audio()

        elif "you" in text and "remember" in text:
            return show_text(info)

        elif "goodbye" in text:
            return show_text(goodbye[randrange(len(goodbye))])

        elif "stop" in text:
            break

        elif "ha" in text or "thank you" in text or "thanks" in text:
            return show_text(thanks[randrange(len(thanks))])

        elif "change" in text and "language" in text:
            return show_text("Which language whould you like to use?")
            lang = input("Plaese, type the language here (en/ru): ")
            f = open("info.txt", "w")
            f.write(lang)
            return show_text("Successfully changed!")

        elif "hello" in text:
            return show_text(hello[randrange(len(hello))])

        elif "what is your name" in text:
            return show_text("My name is Assistant")
        elif "thank you" in text:
            return show_text("You are welcome!")

        elif "how are you" in text:
            return show_text(feeling[randrange(len(feeling))])

        elif "i am" in text:
            feeling = ""
            if "bad" in text or "angry" in text:
                if "bad" in text:
                    feeling = "bad"
                else:
                    feeling = "angry"
                return show_text(bad[randrange(len(bad))])

        elif "random number generator" in text:
            i = randrange(100)
            return show_text(i)

        elif "+" in text:
            text = text.split()
            return show_text(f"{text[0]} + {text[-1]} = {int(text[0]) + int(text[-1])}")

        elif "-" in text:
            text = text.split()
            return show_text(f"{text[0]} - {text[-1]} = {int(text[0]) - int(text[-1])}")

        elif "*" in text:
            text = text.split()
            return show_text(f"{text[0]} * {text[-1]} = {int(text[0]) * int(text[-1])}")
            
        elif "/" in text:
            text = text.split()
            return show_text(f"{text[0]} / {text[-1]} = {int(text[0]) / int(text[-1])}")   
            
        elif "timer" in text:
            return show_text("Please, write the number of seconds to set the timer.")
            t = int(input())
            return show_text("Started!")
            sleep(t)
            return show_text("Time over!")

        elif "what can you do" in text:
            return show_text("I am an Assistant by Bekhruz Niyazov and Peter Repiev. I can translate English to Russian, set timers, make notes and I can count!")

        elif "make a note" in text or "write this down" in text or "remember this" in text:
            return show_text("What would you like to write down?")
            note_text = get_audio()
            try:
                note(note_text)
                return show_text("I've made a note of that.")
            except:
                return show_text(sorry[randrange(len(sorry))])

        elif text == None:
            sleep(1)

        elif "joke" in text or "laugh" in text:
            return show_text(jokes[randrange(len(jokes))])

        elif "time" in text:
            return show_text(ctime())

        elif "date" in text:
            print(ctime())

        elif "say" in text or "return show_text" in text:
            words = input('Please, write what I have to say.')
            return show_text(words)

        elif "open" in text:
            try:
                Popen([f"{text.split()[-1]}.exe", ""])
            except:
                return show_text(sorry[randrange(sorry)])

        else:
            return show_text(sorry[randrange(len(sorry))])

        sleep(1)

    elif lang == "ru":
        try:
            if "кто ты" in text or "что ты умеешь" in text or "кто тебя создал" in text:
                return show_text("Я ассистент созданный Ниязовом Бехрузом и Петром Репьевым. Я могу говорить время и дату, шутить, делать заметки и многое другого")

            elif "дата" in text: 
                print(ctime())

            elif "пока" in text or "до свидания" in text or "прощай" in text:
                    return show_text("Пока! Скажите стоп, чтоб прекратить работу.")

            elif "стоп" in text:
                break

            elif "время" in text or "времени" in text:
                return show_text(ctime())

            elif "шутка" in text or "шутку" in text or "пошути" in text:
                return show_text(rjokes[randrange(len(rujokes))])

            elif "таймер" in text:
                return show_text("Пожалуйста, укажите количество секунд на которое поставить надо таймер.")
                tr = int(input())
                return show_text("Установлено!")
                sleep(tr)
                return show_text("Время истекло!")

            elif "сделай заметку" in text or "напиши это" in text or "запомни это" in text:
                return show_text("Что мне нужно запомнить?")
                note_text = get_audio()
                note(note_text)
                return show_text("Я это записал.")

            elif text == None:
                sleep(1)

            elif "запомни" in text:
                return show_text("Что я должен запомнить?")
                global info2
                info2 = get_audio()

            elif "ты" in text or "вы" in text and "запомнил" in text or "запомнила" in text:
                return show_text(info)

            elif "привет" in text:
                return show_text("Тебе привет тоже!")

            elif "как тебя зовут" in text:
                return show_text("Меня зовут ...")

            elif "спасибо" in text:
                return show_text("Не за что!")

            elif "как ты" in text:
                return show_text("Хорошо, спасибо!")

            elif "случайное число" in text:
                i2 = randrange(100)
                return show_text(i2)

            elif "произнеси" in text or "скажи" in text:
                words = input('Пожалуйста, напишите, что мне надо произнести.')
                say(words)

            elif "+" in text:
                text = text.split()
                return show_text(f"{text[0]} + {text[-1]} = {int(text[0]) + int(text[-1])}")

            elif "-" in text:
                text = text.split()
                return show_text(f"{text[0]} - {text[-1]} = {int(text[0]) - int(text[-1])}")

            elif "*" in text:
                text = text.split()
                return show_text(f"{text[0]} * {text[-1]} = {int(text[0]) * int(text[-1])}")
            
            elif "/" in text:
                text = text.split()
                return show_text(f"{text[0]} / {text[-1]} = {int(text[0]) / int(text[-1])}")

            else:
                return show_text("Извините, но я этого еще не умею!")

        except:
            return show_text("Извините, но я не могу сейчас выполнить эту команду, повторите попозже.")

    else:
        return show_text("Sorry, but I don't know that language yet! Извините, но я ещё не знаю этого языка!")
