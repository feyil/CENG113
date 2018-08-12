#230201057
import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        self.tip_memory=[] #to keep tracking tips but it is not working well I have no time to complete how I want.
        self.count_memory=[]#to keep tracking changes on the count_deck
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self,tip):
        tip=str.split(tip,",")
        if tip[-1]=="b" or tip[-1]=="w":
            location=[]
            control=set([1,2,3])
            if len(self.hand)==2:
                control=set([1,2])
            if len(self.hand)==1:
                control=set([1])
            for i in tip[:(len(tip)-1)]:
                a=int(i)
                location.append(a)
                self.hand[a-1][0]=tip[-1]
            result=control-set(location)
            if tip[-1]=="b" and len(list(result))!=0:
                for i in list(result):
                    a=int(i)
                    self.hand[a-1][0]="w"
            elif tip[-1]=="w" and len(list(result))!=0:
                for i in list(result):
                    a=int(i)
                    self.hand[a-1][0]="b"
                    
        else:
            for i in tip[:(len(tip)-1)]:
                a=int(i)
                self.hand[a-1][1]=int(tip[-1])
            # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
            # where * indicates optionality and tip is either a value or a color.
            # e.g. "1,2,w" or "2,3" or "1,2,3,2"
            # output: none
            # The tip is processed and the information about the bot's hand is updated.
    def get_tip_logic(self):
        black_inform={"b1":0,"b2":0,"b3":0,"b4":0}
        white_inform={"w1":0,"w2":0,"w3":0,"w4":0}
        for i in self.count_deck:
            if i[0]=="b":
                for n in range(1,5):
                    if i[1]==n:
                        black_inform["b"+str(n)]=black_inform["b"+str(n)]+1
            elif i[0]=="w":
                for n in range(1,5):
                    if i[1]==n:
                        white_inform["w"+str(n)]=white_inform["w"+str(n)]+1
        black_number=0
        white_number=0
        for i in black_inform.values():
            black_number=black_number+i
        for i in white_inform.values():
            white_number=white_number+i
        if len(count_deck)!=0:
            if black_number==0:
                for i in self.hand:
                    if i[0]=='!':
                        i[0]='w'
            elif white_number==0:
                for i in self.hand:
                    if i[0]=='!':
                        i[0]='b'
        for i in range(1,5):
            if black_inform["b"+str(i)]==0:
                for n in self.hand:
                    if n[1]==i:
                        n[0]='w'
        for i in range(1,5):
            if white_inform["w"+str(i)]==0:
                for n in self.hand:
                    if n[1]==i:
                        n[0]='b'
    def update_count_deck(self,card):
        if card in self.count_deck:
            self.count_deck.remove(card)
            return self.count_deck
        else:
            return "No exist"
        # input: none
        # output: none
        # card is removed from the count_deck of the bot.
        pass

    def update_hand(self,num):
        self.hand.pop(num-1)
        if len(deck)!=0:
            self.hand.append(['!',-1])
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.
        
    def give_tip(self):
        self.count_memory.append(len(self.count_deck))
        if len(self.count_memory)>1 and ((self.count_memory[-1]-self.count_memory[-2])!=0):
            d=self.tip_memory[:]
            for c in d:
                self.tip_memory.remove(c)
        if len(self.stack[0])==len(self.stack[1]) and len(self.stack[0])!=4 and len(self.stack[0])!=4:
            replica=self.play_hand[:]
            loc=1
            hint=[]
            location=[]
            while loc<5:
                need=[["b",loc],["w",loc]]
                if len(self.stack[0])==loc-1 and len(self.stack[1])==loc-1:
                    for i in need:
                        if i in replica:
                            number=replica.count(i)
                            for a in range(number):
                                index=replica.index(i)+1
                                hint=i[1]
                                location.append(index)
                                replica[index-1]=0
                loc=loc+1
            location.sort()
            result="Tip:"
            if hint!=[]:
                for i in location:
                    result=result+(str(i)+",")
                result=result+str(hint)
                if (result in self.tip_memory)!=True:
                    self.tip_memory.append(result)
                    return result
        if len(self.stack[0])==0:
            replica=self.play_hand[:]
            location=[]
            need_num=1
            need=['b',1]
            for i in replica:
                if need==i:
                    index=replica.index(i)
                    location.append(index+1)
                    replica[index]=0
            if len(location)!=0:
                location.sort()
                result="Tip:"
                for i in location:
                    result=result+(str(i)+",")
                result=result+str(need_num)
                if (result in self.tip_memory)!=True:
                    self.tip_memory.append(result)
                    return result
        if len(self.stack[1])==0:
            replica=self.play_hand[:]
            location=[]
            need_num=1
            need=['w',1]
            for i in replica:
                if need==i:
                    index=replica.index(i)
                    location.append(index+1)
                    replica[index]=0
            if len(location)!=0:
                location.sort()
                result="Tip:"
                for i in location:
                    result=result+(str(i)+",")
                result=result+str(need_num)
                if (result in self.tip_memory)!=True:
                    self.tip_memory.append(result)
                    return result
            
        if len(self.stack[0])!=0:
            x=self.stack[0][-1][1]
            replica=self.play_hand[:]
            counter=[]
            for i in replica:
                if i[1]==x+1:
                    index=replica.index(i)
                    counter.append(index+1)
                    replica[index]=0
            if len(counter)!=0:
                counter.sort()
                result="Tip:"
                for i in counter:
                    result=result+(str(i)+",")
                result=result+str(x+1)
                if (result in self.tip_memory)!=True:
                    self.tip_memory.append(result)
                    return result
        if len(self.stack[1])!=0:
            replica=self.play_hand[:]
            y=self.stack[1][-1][1]
            replica=self.play_hand[:]
            counter=[]
            for i in replica:
                if i[1]==y+1:
                    index=replica.index(i)
                    counter.append(index+1)
                    replica[index]=0
            if len(counter)!=0:
                counter.sort()
                result="Tip:"
                for i in counter:
                    result=result+(str(i)+",")
                result=result+str(y+1)
                if (result in self.tip_memory)!=True:
                    self.tip_memory.append(result)
                    return result
        if True:
            color=random.choice(["w","b"])
            result_black=""
            if color=="b":
                replica=self.play_hand[:]
                counter=[]
                for i in replica:
                    if i[0]=="b":
                        index=replica.index(i)
                        counter.append(index+1)
                        replica[index]=0
                counter.sort()
                result="Tip:"
                for i in counter:
                    result=result+(str(i)+",")
                result=result+"b"
                result_black=result
                if (result in self.tip_memory)!=True and result!="Tip:b":
                    self.tip_memory.append(result)
                    return result
            else:
                
                replica=self.play_hand[:]
                counter=[]
                for i in replica:
                    if i[0]=="w":
                        index=replica.index(i)
                        counter.append(index+1)
                        replica[index]=0
                counter.sort()
                result="Tip:"
                for i in counter:
                    result=result+(str(i)+",")
                result=result+"w"
                if (result in self.tip_memory)!=True and result!="Tip:w":
                    self.tip_memory.append(result)
                    return result
            return result_black
        # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.

    def pick_stack(self):
        if len(self.stack[0])==len(self.stack[1]) and len(self.stack[0])!=4:
            if len(self.stack[0])!=0:    
                need=self.stack[0][-1][1]+1
            else:
                need=1
            if ['!',need] in self.hand:
                loc=self.hand.index(['!',need])
                if comp_hand[loc][0]=="b":
                    self.stack[0].append(comp_hand[loc])
                else:
                    self.stack[1].append(comp_hand[loc])
                return loc+1        
        if len(self.stack[0])==0 and (['b',1] in self.hand):
            loc=self.hand.index(['b',1])
            self.stack[0].append(['b',1])
            return loc+1
        if len(self.stack[1])==0 and (['w',1] in self.hand):
            loc=self.hand.index(['w',1])
            self.stack[1].append(['w',1])
            return loc+1
        if len(self.stack[0])!=0 and (['b',(self.stack[0][-1][1]+1)] in self.hand):
            loc=self.hand.index(['b',(self.stack[0][-1][1]+1)])
            self.stack[0].append(['b',(self.stack[0][-1][1]+1)])
            return loc+1
        if len(self.stack[1])!=0 and (['w',(self.stack[1][-1][1]+1)] in self.hand):
            loc=self.hand.index(['w',(self.stack[1][-1][1]+1)])
            self.stack[1].append(['w',(self.stack[1][-1][1]+1)])
            return loc+1
        if True:
            return -1
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
    def pick_discard(self):
        for i in self.hand:
            if (i in self.stack[0]) or (i in self.stack[1]):
                loc=self.hand.index(i)
                return loc+1 
        if len(self.stack[0])==4:
            for loc in range(len(self.hand)):
                if self.hand[loc][0]=='b':
                    return loc+1
        if len(self.stack[1])==4:
            for loc in range(len(self.hand)):
                if self.hand[loc][0]=='w':
                    return loc+1
        if len(self.stack[0])>=1 and len(self.stack[0])>=1:
            for loc in range(len(self.hand)):
                if self.hand[loc][1]==1:
                    return loc+1
        if len(self.stack[0])>=2 and len(self.stack[0])>=2:
            for loc in range(len(self.hand)):
                if self.hand[loc][1]==2:
                    return loc+1
        if len(self.stack[0])>=3 and len(self.stack[0])>=3:
            for loc in range(len(self.hand)):
                if self.hand[loc][1]==3:
                    return loc+1
        if ['!',-1] in self.hand:
            loc=self.hand.index(['!',-1])
            return loc+1
        if True:
            loc=random.randint(0,2)
            if len(self.hand)==2:
                loc=random.randint(0,1)
            elif len(self.hand)==1:
                loc=0
            return loc+1
        if True:
            return -1
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case, 
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.


def shuffle(deck):
    for i in range(100):
        ind1 = random.randint(0,len(deck)-1)
        ind2 = random.randint(0,len(deck)-1)
        deck[ind1], deck[ind2] = deck[ind2], deck[ind1]

def print_menu():
    
    print "Hit 'v' to view the status of the game."
    print "Hit 't' to spend a tip."
    print "Hit 's' to try and stack your card."
    print "Hit 'd' to discard your card and earn a tip."
    print "Hit 'h' to view this menu."
    print "Hit 'q' to quit."
    
def update_hand(hand,deck,num):
    if len(deck)!=0:#assumption num is between 1 and 3
        removed_card=hand[num-1]
        del hand[num-1]
        hand.append(deck[0])
        del deck[0]
        return removed_card #warning
    else:
        removed_card=hand[num-1]
        del hand[num-1]#dont forget
        return removed_card 
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.

def try_stack(card,stack,trash,lives):
    if card[0]=='b':
       if card[1]==1 and ((card in stack[0])!=True):
           stack[0].append(card)
           return lives
       elif (len(stack[0])!=0 and len(stack[0])!=4) and (card[1]-stack[0][-1][1])==1:#and order is important
           stack[0].append(card)
           return lives
       else:
           lives=lives-1
           trash.append(card)
           trash.sort
           if lives>=0:
               print "Number of lives left:",lives
           return lives
    elif card[0]=='w':
        if card[1]==1 and ((card in stack[1])!=True):
            stack[1].append(card)
            return lives
        elif (len(stack[1])!=0 and len(stack[1])!=4) and (card[1]-stack[1][-1][1])==1:#and order is important
           stack[1].append(card)
           return lives
        else:
           lives=lives-1
           trash.append(card)
           trash.sort()
           if lives>=0:
               print "Number of lives left:",lives
           return lives
    # input: the card to be stacked, current stack, current trash, number of lives
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.
def discard(card,trash,tips):
    trash.append(card)
    trash.sort()
    tips=tips+1
    print "Trash:",trash
    print "Updated tips:",tips
    return tips
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.

print "Welcome! Let's play!"
print_menu()
deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack = [[],[]] #0 means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
comp_hand = deck[0:3]           # First hands are dealt.
play_hand = deck[3:6]
del deck[0:6]
#print comp_hand
bot = Gamebot(play_hand,stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
count_deck=bot.count_deck

while True:
    if turn == 0:
        inp = raw_input("Your turn:")
        if inp == 'v':
            print "Computer's hand:", comp_hand #computer hand less than 3 is error
            print "Number of tips left:", tips
            print "Number of lives left:", lives
            print "Current stack:"
            print "Black:", stack[0]
            print "White:", stack[1]
            print "Current trash:", trash
        elif inp == "t":
            if tips > 0:
                taken_tip=raw_input("Please type your tip in the format loc1,loc2*,loc3*,tip:")
                tips=tips-1
                print "Number of tips left:",tips
                bot.get_tip(taken_tip)
                bot.get_tip_logic()
                turn = 1        # Switch turns.
                # Take a tip from the player, give it to the bot, update and print number of tips.
            else:
                print "Not possible! No tips left!"
        elif inp == "s":
            taken_location=input("Card location to be stacked:")
            lives=try_stack(play_hand[taken_location-1],stack,trash,lives)
            removed_card=update_hand(play_hand,deck,taken_location)
            if len(play_hand)!=0:
                count_deck=bot.update_count_deck(play_hand[-1])
            bot.get_tip_logic()
            turn = 1        # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
        elif inp == "d":
            taken_location=input("Card location to be discarded:")
            tips=discard(play_hand[taken_location-1],trash,tips)#empty hand forbid
            removed_card=update_hand(play_hand,deck,taken_location)
            if len(play_hand)!=0:
                count_deck=bot.update_count_deck(play_hand[-1])
            bot.get_tip_logic()
            turn = 1        # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card. 
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print "Please enter a valid choice (v,t,s,d,h,q)!"
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        loc=bot.pick_stack()
        if loc!=-1:
            bot.get_tip_logic()
            ##################Pick Stack"
            bot.update_hand(loc)
            removed_card=update_hand(comp_hand,deck,loc)
            bot.update_count_deck(removed_card)        
        else:
            bot.get_tip_logic()
            if tips > 0  and len(play_hand)>0:#I tested it work well compared to other version.If you wish you can chance tip limit
                ###############Tip"
                print bot.give_tip()
                tips=tips-1
                print "Number of tips left:",tips
                 # Take a tip from the bot. Update the number of tips. Print both
                # the given tip by the bot and the updated number of tips.
            else:
                #print loc
                bot.get_tip_logic()
                ##############Discard"
                hand=bot.hand
                loc=bot.pick_discard()
                if loc!=-1:
                    bot.update_hand(loc)
                    removed_card=update_hand(comp_hand,deck,loc)
                    tips=discard(removed_card,trash,tips)
                    bot.update_count_deck(removed_card)
                    #print bot.hand
            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck 
            # and discard the selected card.
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives<0:
        print "No lives left! Game over!"
        print "Your score is", score
        break
    if len(comp_hand+play_hand)==0:
        print "No cards left! Game over!"
        print "Your score is", score
        break
    if score == 8:
        print "Congratulations! You have reached the maximum score!"
        break
#fey