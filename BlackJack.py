from tkinter import *
import random
import tkinter as tk

#Creation of the cards,suits and its values
suit=['Heart','Diamond','Spade','Club']
cards=["1","2","3","4","5","6","7","8","9","10","K","Q","J","A"]
card_value={"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"K":10,"Q":10,"J":10}

def table():
    win = tk.Tk()
    win.title('Card Shuffle')
    win.geometry("900x600")
    win.config(background="Green")

    def shuffle():
        i,j=0,0
      
        #Create players cards in a suit and value
        global player,player_suits,dealer_suits,dealer,hand,dealer_hand
        dealer_suits=[]
        player_suits=[]
        dealer = []
        player = []
      
        #Chooses a card for player
        while i < 2:
            i += 1
            color = random.randrange(len(suit))
            face_card = random.randrange(1,len(cards))
            player_suits.append(suit[color])
            for keys in card_value:
                if cards[face_card] == keys:
                    player.append(card_value.get(cards[face_card]))
            print(suit[color], card_value.get(cards[face_card]), cards[face_card])
        print(player, sum(player))
        player_label.config(text=sum(player))
      
        #Chooses two cards for dealer
        while j < 2:
            j += 1
            color = random.randrange(len(suit))
            face_card = random.randrange(1,len(cards))
            dealer_suits.append(suit[color])
            for keys in card_value:
                if cards[face_card] == keys:
                    dealer.append(card_value.get(cards[face_card]))
            print(suit[color], card_value.get(cards[face_card]), cards[face_card])
        print(dealer, sum(dealer))
        hand = [player[0], player_suits[0], player[1], player_suits[1]]
        dealer_hand =[dealer[0],dealer_suits[0],dealer[1],dealer_suits[1]]
        dealer_label.config(text=f'{dealer_hand}')
        player_label.config(text=f'{hand}')
        dealer_value_label.config(text=f'Dealer Value:{sum(dealer)}')
        player_value_label.config(text=f'Player Value:{sum(player)}')
      
    #Player Hit function
    def hit():
        color = random.randrange(len(suit))
        face_card = random.randrange(1, len(cards))
        player_suits.append(suit[color])
        for keys in card_value:
            if cards[face_card] == keys:
                player.append(card_value.get(cards[face_card]))
            print(suit[color], card_value.get(cards[face_card]), cards[face_card])
        hand.append(card_value.get(cards[face_card]))
        hand.append(suit[color])
        print(player, sum(player))
        player_label.config(text=sum(player))
        player_label.config(text=f'{hand}')
        player_value_label.config(text=f'Player Value:{sum(player)}')
        sum_player=sum(player)
        if sum_player>21:
            dealer_hit()
    #Dealer Hit Function
    def dealer_hit():
        if sum(dealer)<17:
            while sum(dealer)<17:
                color = random.randrange(len(suit))
                face_card = random.randrange(1, len(cards))
                dealer_suits.append(suit[color])
                for keys in card_value:
                    if cards[face_card] == keys:
                        dealer.append(card_value.get(cards[face_card]))
                    print(suit[color], card_value.get(cards[face_card]), cards[face_card])
                dealer_hand.append(card_value.get(cards[face_card]))
                dealer_hand.append(suit[color])
                print(dealer, sum(dealer))
        elif sum(dealer)>=17:
            print(dealer,sum(dealer))
        else:
            print(dealer, sum(dealer))
        dealer_label.config(text=sum(dealer))
        dealer_label.config(text=f'{dealer_hand}')
        dealer_value_label.config(text=f'Dealer Value:{sum(dealer)}')
        winner()
    #Function to find out who wins
    def winner():
        if sum(player)>21 and sum(dealer)<21:
            print('Dealer wins with:',sum(dealer))
        elif sum(player)<21 and sum(dealer)<21:
            if sum(dealer)>sum(player):
                print('Dealer wins with:',sum(dealer))
            else:
                print('Player wins with:', sum(player))
        elif sum(player)<21 and sum(dealer)>21:
            print('Player wins with:', sum(player))
        elif sum(player)==sum(dealer):
            print('Push')
        elif sum(player)==21 and sum(dealer)<21:
            print('Player wins with:', sum(player))
        elif sum(player) == 21 and sum(dealer)>21:
            print('Player wins with:', sum(player))
        elif sum(player)>21 and sum(dealer)==21:
            print('Dealer wins with:', sum(dealer))
        elif sum(player)<21 and sum(dealer)==21:
            print('Dealer wins with:', sum(dealer))
        elif sum(player)>21 and sum(dealer)>21:
            print('Player Loses')
    #Stand function for once player hit stand the dealer function is called
    def stand():
        dealer_hit()
      
    frame = Frame(win, bg="green")
    frame.pack(pady=120)

    dealer_frame = LabelFrame(frame, text="Dealer", bd=0, font="Arial", bg="yellowgreen")
    dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

    dealer_label = Label(dealer_frame, text='',bd=0, bg="yellowgreen")
    dealer_label.pack(pady=20)

    player_frame = LabelFrame(frame, text="Player", bd=0, font="Arial", bg="yellowgreen")
    player_frame.grid(row=1, column=0, ipadx=20)

    player_label = Label(player_frame, text='', bg="yellowgreen")
    player_label.pack(pady=20)

    dealer_value_label = LabelFrame(frame, text="Dealer Value", bd=0, font="Arial", bg="green",fg="white")
    dealer_value_label.grid(row=0, column=4, padx=20, ipadx=20)

    dealer_value_frame = Label(dealer_value_label, text="", bd=0, font="Arial",bg="green")
    dealer_value_frame.grid(row=0, column=0, ipadx=20)

    player_value_label = LabelFrame(frame, text="Player Value", bd=0, font="Arial", bg="green",fg="white")
    player_value_label.grid(row=1, column=4, padx=20, ipadx=20)

    player_value_frame = Label(player_value_label, text="", bd=0, font="Arial",bg="green")
    player_value_frame.grid(row=0, column=0, ipadx=20)

    shuffle_button = Button(win, text="Shuffle Deck", font=("Arial", 14), command=shuffle)
    shuffle_button.pack(pady=10)

    stand_button = Button(win, text="Stand", font=("Arial", 14), command=stand)
    stand_button.pack(pady=10)

    hit_button = Button(win, text="Hit", font=("Arial", 14), command=hit)
    hit_button.pack(pady=10)
