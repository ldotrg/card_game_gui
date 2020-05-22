# import tkinter for GUI and random for gambling
from tkinter import Tk, Button, Label, Entry, PhotoImage, NORMAL, END, DISABLED, CENTER
import random
import time
import threading


class CardGame:
    def __init__(self, master):
        self.master = master
        master.title("Card Game")
        master.configure(background='white', padx=70, pady=70)

        self.cardBackImg = PhotoImage(file="cards/card_back.png")

        self.cardRedImg = [
            PhotoImage(file="cards/ace_of_hearts.png"),
            PhotoImage(file="cards/ace_of_diamonds.png"),
            PhotoImage(file="cards/2_of_hearts.png"),
            PhotoImage(file="cards/2_of_diamonds.png"),
            PhotoImage(file="cards/3_of_hearts.png"),
            PhotoImage(file="cards/3_of_diamonds.png"),
            PhotoImage(file="cards/4_of_hearts.png"),
            PhotoImage(file="cards/4_of_diamonds.png"),
            PhotoImage(file="cards/5_of_hearts.png"),
            PhotoImage(file="cards/5_of_diamonds.png"),
            PhotoImage(file="cards/6_of_hearts.png"),
            PhotoImage(file="cards/6_of_diamonds.png"),
            PhotoImage(file="cards/7_of_hearts.png"),
            PhotoImage(file="cards/7_of_diamonds.png"),
            PhotoImage(file="cards/8_of_hearts.png"),
            PhotoImage(file="cards/8_of_diamonds.png"),
            PhotoImage(file="cards/9_of_hearts.png"),
            PhotoImage(file="cards/9_of_diamonds.png"),
            PhotoImage(file="cards/10_of_hearts.png"),
            PhotoImage(file="cards/10_of_diamonds.png"),
            PhotoImage(file="cards/jack_of_hearts.png"),
            PhotoImage(file="cards/jack_of_diamonds.png"),
            PhotoImage(file="cards/queen_of_hearts.png"),
            PhotoImage(file="cards/queen_of_diamonds.png"),
            PhotoImage(file="cards/king_of_hearts.png"),
            PhotoImage(file="cards/king_of_diamonds.png")
        ]

        self.cardBlackImg = [
            PhotoImage(file="cards/ace_of_spades.png"),
            PhotoImage(file="cards/ace_of_clubs.png"),
            PhotoImage(file="cards/2_of_spades.png"),
            PhotoImage(file="cards/2_of_clubs.png"),
            PhotoImage(file="cards/3_of_spades.png"),
            PhotoImage(file="cards/3_of_clubs.png"),
            PhotoImage(file="cards/4_of_spades.png"),
            PhotoImage(file="cards/4_of_clubs.png"),
            PhotoImage(file="cards/5_of_spades.png"),
            PhotoImage(file="cards/5_of_clubs.png"),
            PhotoImage(file="cards/6_of_spades.png"),
            PhotoImage(file="cards/6_of_clubs.png"),
            PhotoImage(file="cards/7_of_spades.png"),
            PhotoImage(file="cards/7_of_clubs.png"),
            PhotoImage(file="cards/8_of_spades.png"),
            PhotoImage(file="cards/8_of_clubs.png"),
            PhotoImage(file="cards/9_of_spades.png"),
            PhotoImage(file="cards/9_of_clubs.png"),
            PhotoImage(file="cards/10_of_spades.png"),
            PhotoImage(file="cards/10_of_clubs.png"),
            PhotoImage(file="cards/jack_of_spades.png"),
            PhotoImage(file="cards/jack_of_clubs.png"),
            PhotoImage(file="cards/queen_of_spades.png"),
            PhotoImage(file="cards/queen_of_clubs.png"),
            PhotoImage(file="cards/king_of_spades.png"),
            PhotoImage(file="cards/king_of_clubs.png")
        ]

        # create card window
        self.cardWindow = Label(
            master,
            image=self.cardBackImg,
            width=222,
            height=323,
            bg="white",
            borderwidth=1,
            relief="solid"
        )
        # we need to keep a reference to the image in order to display it http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.cardWindow.image = self.cardBackImg
        self.cardWindow.grid(ipadx=5, ipady=5)

        # create RED button
        redButtonImg = PhotoImage(file="buttons/redButton.png")
        self.redButton = Button(
            master,
            image=redButtonImg,
            bg="white",
            activebackground="red",
            cursor="hand1",
            borderwidth=0,
            text = "Choose Group",
            command=lambda: self.click("red"),  # call click() function
            compound="top" # Let image on top of text.
        )
        self.redButton.image = redButtonImg
        self.redButton.grid()

        # create BLACK button
        blackButtonImg = PhotoImage(file="buttons/blackButton.png")
        self.blackButton = Button(
            master,
            image=blackButtonImg,
            bg="white",
            activebackground="black",
            activeforeground="white",
            borderwidth=0,
            cursor="hand1",
            text = "Choose Card & \nStart stopwatch",
            justify = CENTER,
            compound="top", # Let image on top of text.
            command=lambda: self.click("black")
        )
        self.blackButton.image = blackButtonImg
        self.blackButton.grid()

        # create blackcard window
        self.blackcardWindow = Label(
            master,
            image=self.cardBackImg,
            width=222,
            height=323,
            bg="white",
            borderwidth=1,
            relief="solid"
        )
        # we need to keep a reference to the image in order to display it http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.blackcardWindow.image = self.cardBackImg
        self.blackcardWindow.grid(ipadx=5, ipady=5)

        # create CREDIT text
        self.credit = Entry(master, justify=CENTER)
        # self.credit.grid()
        self.credit.insert(0, "CREDIT")

        # create CASH OUT button
        self.cashOut = Button(
            master,
            text="CASH OUT",
            command=lambda: self.cashOutTrigger()  # call cashOutTrigger() function
        )
        # self.cashOut.grid(pady=20, ipady=10)

        # create BET entry
        self.bet = Entry(master, justify=CENTER)
        # self.bet.grid()
        self.bet.insert(0, "BET")

        # create INFO
        self.info = Entry(
            master,
            justify=CENTER,
            state=DISABLED,
            disabledbackground="orange",
            disabledforeground="white"
        )
        # self.info.grid(column=1, ipadx=20)

        # Countdown window
        self.countdown_window = Label(
            master,
            text= "Time",
            width=40,
            height=5,
            bg="white",
            borderwidth=1,
            font=("Helvetica", 20)
        )
        # make grid system/component position
        count = 0
        # components = [
        #     self.redButton, self.cardWindow, self.blackButton,
        #     self.credit, self.cashOut, self.bet
        # ]
        components = [
            self.redButton,
            self.cardWindow,
            self.blackButton,
            self.blackcardWindow,
            self.countdown_window
        ]
        # for row in range(0, 1):
        #     for column in range(0, 3):
        #         components[count].grid(row=row, column=column)
        #         count += 1
        components[0].grid(row=0, column=0)
        components[1].grid(row=0, column=1)
        components[2].grid(row=1, column=0)
        components[3].grid(row=1, column=1)
        components[4].grid(row=2, columnspan=2)

        self.trigger = False  # it helps us leading the player and resolve some bugs
        self.credit.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(event, self.credit,)
        )  # when a player focus the text box, the text will disappear
        self.credit.bind(
            "<FocusOut>",
            lambda event: self.add_placeholder(event, self.credit,  "CREDIT")
        )  # when a player focus outside the text box, the text will appear if the string is 0 or empty

        self.bet.bind(
            "<FocusIn>",
            lambda event: self.clear_placeholder(event, self.bet)
        )  # when a player focus the text box, the text will disappear
        self.bet.bind(
            "<FocusOut>",
            lambda event: self.add_placeholder(event, self.bet, "BET")
        )  # when a player focus outside the text box, the text will appear if the string is 0 or empty

    def click(self, color):  # what happen when you click a color

        # # first checks if you insert CREDIT
        # if len(self.credit.get()) == 0 or self.credit.get() == "CREDIT":
        #     print("Please insert coins first!")
        #     self.infoDisplay("Please insert coins first!", "orange")

        # # second checks if you insert BET
        # elif len(self.bet.get()) == 0 or self.bet.get() == "BET":
        #     print("Please bet first!")
        #     self.infoDisplay("Please bet first!", "orange")

        # # third checks if BET is bigger than CREDIT and IF the trigger is OFF
        # # ex.: IF the trigger is ON and you win more hands in a row,
        # # when the BET get bigger than your CREDIT you can't play anymore and you are forced to CASH OUT
        # elif int(self.bet.get()) > int(self.credit.get()) and self.trigger is False:
        #     print("You don't have enough credit!")
        #     self.infoDisplay("You don't have enough credit!", "orange")
        # else:
            # chance = random.choice([True, False])
            # self.takeCredit()
            self.flipCard(color)
            # self.checkWin(color, chance)
            # self.disableBet()

    def takeCredit(self):  # take coins from CREDIT when you BET your first hand
        if self.trigger is False:  # without trigger condition you would be charged every time you bet even if you win
            aux = int(self.credit.get())
            self.credit.delete(0, END)
            self.credit.insert(0, aux-int(self.bet.get()))

    timer_id = ""

    def countdown2(self, timeremaining):
        #global timer_id
        if self.timer_id:
            self.master.after_cancel(self.timer_id) # cancel any already running timers
        mins, secs = divmod(timeremaining, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        self.countdown_window.config(text = timeformat)
        if timeremaining == 0:
            print('Finished!!! timer_id: ' + self.timer_id)
        else:
            self.timer_id = self.master.after(1000, self.countdown2, timeremaining-1) # schedule the next iteration
    def countdown(self,t):
        lt = t
        while lt > -1:
            mins, secs = divmod(lt, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            self.countdown_window.configure(text=timeformat)
            self.master.update() #This way your program will display the numbers.
            time.sleep(1)
            lt -= 1

    def flipCard(self, color):  # change card according to the color
        index = random.randint(0, 25)
        if color is "red":
            self.cardWindow.configure(image=self.cardRedImg[index])
            self.cardWindow.image = self.cardRedImg[index]
        elif color is "black":
            self.blackcardWindow.configure(image=self.cardBlackImg[index])
            self.blackcardWindow.image = self.cardBlackImg[index]
            self.countdown2(10)
            # t = threading.Thread(target=self.countdown(10))
            # t.start()

    def checkWin(self, color, chance):  # verify if you win or lose
        if color == "red" and chance is True:
            print("You win!")
            self.infoDisplay("You win!", "green")
            self.bet.configure(state=NORMAL)
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
            self.bet.configure(state=DISABLED)
        elif color == "black" and chance is False:
            print("You win!")
            self.infoDisplay("You win!", "green")
            self.bet.configure(state=NORMAL)
            self.trigger = True
            aux = int(self.bet.get())
            self.bet.delete(0, END)
            self.bet.insert(0, aux*2)
            self.bet.configure(state=DISABLED)
        else:
            print("You lose!")
            self.infoDisplay("You lose!", "tomato")
            self.bet.configure(state=NORMAL)
            self.bet.delete(0, END)
            self.trigger = False

    # disabled input so you can't increase your bet(winnings) before you CASH OUT
    def disableBet(self):
        if self.trigger is False:
            print("false output")
            self.bet.configure(state=NORMAL)
        else:
            print("true output")
            self.bet.configure(state=DISABLED)

    def cashOutTrigger(self):  # take coins out
        if len(self.credit.get()) == 0 or len(self.bet.get()) == 0:
            print("Please insert coins first!")
            self.infoDisplay("Please insert coins first!", "orange")
        elif self.trigger is False:
            print("Pick a color first!")
            self.infoDisplay("Pick a color first!", "orange")
        elif int(self.bet.get()) > 0:
            print("DONE!")
            self.infoDisplay("DONE!", "yellow")
            self.bet.configure(state=NORMAL)
            aux = int(self.credit.get())
            self.credit.delete(0, END)
            self.credit.insert(0, aux+int(self.bet.get()))
            self.bet.delete(0, END)
            self.trigger = False
        else:
            print("Try to win first!")
            self.infoDisplay("Try to win first!", "orange")

    def infoDisplay(self, outputText, color):  # display some usefull informations
        self.info.configure(state=NORMAL)  # so we can modify it
        self.info.delete(0, END)
        self.info.insert(0, outputText)
        self.info.configure(
            disabledbackground=color,
            state=DISABLED  # return to the first state
        )

    # adds placeholder to the both entries (CREDIT and BET)
    def add_placeholder(self, event, whatEntry, placeholder):
        if not whatEntry.get() or whatEntry.get() == "0":
            whatEntry.delete(0, END)
            whatEntry.insert(0, placeholder)

    # clean placeholder to the both entries (CREDIT and BET)
    def clear_placeholder(self, event, whatEntry):
        if whatEntry.get() == "CREDIT" or whatEntry.get() == "BET":
            whatEntry.delete(0, END)

def main():
    root = Tk()
    CardGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()