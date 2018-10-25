from gamePieces import *

def main():

    cardDeck=Deck()
    print(cardDeck)
    for i in range(26):
        stephCard=cardDeck.deal()
        evanCard=cardDeck.deal()
        print("steph holding " +str(stephCard))
        print("evan holding " +str(evanCard))
        print()
    junkCard=cardDeck.deal()
    print(junkCard)

    print("shuffled deck")
    cardDeck.shuffle()
    print(cardDeck)


    print()
    cardDeck.sort()
    print(cardDeck)
    
    
##    spencerCard=Card("Spades",13)
##    print(spencerCard)
##    spencerCard=Card("hearts",1)
##    print(spencerCard)
##    spencerCard=Card("Bananas",14)
##    print(spencerCard)
    
##    kenDie=Die(6)
##    cerDie=Die(8)
##    
##    print("carter's die val"+str(cerDie.getFaceValue()))
##    print("kensley's die val:" +str(kenDie.getFaceValue()))
##
##    print(str(kenDie))
##    print(str(cerDie))
##
##    
##
##    for i in range(10):
##        kenDie.roll()
##        cerDie.roll()
##        print("die value"+str(cerDie.getNumSides()))
##    
##    cerDie.setNumSides(3.5)
##    print("carter num of sides: " +str(cerDie.getNumSides()))
##
##    cerDie.setFaceValue(0)
##    print("carter's num of sides: " +str(cerDie.getFaceValue()))
main()
