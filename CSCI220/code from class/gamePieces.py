import random 

class Die:
    #constuctor:
    #   set intial values for all of the class properties
    #       initial values should be legit 
    def __init__(self,numSides):
        self.numSides=6
        self.setNumSides(numSides)
        self.faceValue=1
##        numSides=int(numSides)
##        if numSides>1:
##            self.numSides=numSides
##        else:
##            self.numSides=6
##        self.numSides = numSides
##        #numSides=properties of the value?
##
##        self.faceValue=1

    #getter methods aka accessor methods:
         #return the property value
    def getFaceValue(self):
        return self.faceValue
    def getNumSides(self):
        return self.numSides
        
    #self is where object is in memory


    ##setter methods aka mutator methods
    #       set the value of a property to a new (legitimate) property

    def setFaceValue(self,value):
        if type(value)==int and value>=1 and value<=self.numSides:
            self.faceValue=value
        

    #method sets the face value to be integer inclusivily bw
    #   1 and numSides
    def roll(self):
        self.faceValue=random.randint(1,self.numSides)

    #method to convert object into a string representation and
        #   return the string
    def __str__(self):
        rntStr="Face Value: " +str(self.faceValue)
        rntStr+= "\nNumber of sides: " +str(self.numSides)
        return rtnStr

class Card:
    #properties: suit and face value
    #constructor(suit,faceVal)
    def __init__(self,suit,faceValue):
        self.faceValue=1
        self.suit="Diamonds"
        self.setFaceValue(faceValue)
        self.setSuit(suit)
    #setter for both properties
    def setFaceValue(self,value):
        if type(value)==int and value>=1 and value<=13:
            self.faceValue=value

    def setSuit(self,suit):
        suits=["Spades","Clubs","Hearts","Diamonds"]
        if type(suit)==str:
            suit=suit.capitalize()
            if suit in suits:
                self.suit=suit
    #getter for both properties 
    def getFaceValue(self):
        return self.faceValue
    def getSuit(self):
        return self.getSuit

    
    #str()

    def __str__(self):
        values=["Ace"]
        for i in range(2,11):
            values.append(str(i))
        values.append("Jack")
        values.append("Queen")
        values.append("King")
        return values[self.faceValue-1]+ " of " +self.suit
    #deck of cards is next
    # properties:
    #   go to a list
    #   next- card to deal
    #methods:
    #   constructor
    #   shuffle
    #   deal
    #   sort
    #   str

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in ["Spades","Clubs","Hearts","Diamonds"]:
            for value in range(1,14):
                #append card with value and face so call card object
                self.deck.append(Card(suit,value))
        self.next=0

    #input: none
    #output: card at position next
    #purpose:
    #   if possible, return next card in deck
    #   increases next by 1
    def deal(self):
        if self.next < len(self.deck):
            card=self.deck[self.next]
            self.next+=1
        else:
            card=-1
        return card

    #input:none
    #output:none
    #Purpose:
    #   modify deck by placing Cards in random order
    #   sets next to 0 
    def shuffle(self):
        for i in range(len(self.deck)):
            randPos=random.randint(0,len(self.deck)-1)
            temp=self.deck[i]
            self.deck[i]=self.deck[randPos]
            self.deck[randPos]=temp
        self.next=0
        

    def sort(self):
        suits=["Spades","Clubs","Hearts","Diamonds"]
        n=len(self.deck)
        for front in range(n-1):
            mp=front
            suitIndex=suits.index(self.deck[mp].getSuit()) #Diamonds-->3
            cardValueMP=self.deck[mp].getFaceValue()+13* suitIndex 
            for i in range(front+1,n):
            
                suitIndex=suits.index(self.deck[mp].getSuit()) #Diamonds-->3
                cardValueI=self.deck[i].getFaceValue()+13* suitIndex
                if cardValueI < cardValueMP:
                    mp=i
                    suitIndex=suits.index(self.deck[mp].getSuit()) #Diamonds-->3
                    cardValueMP=self.deck[mp].getFaceValue()+13* suitIndex 
            temp=self.deck[mp]
            self.deck[mp]=self.deck[front]
            self.deck[front]=temp

    def __str__(self):
        returnStr=""
        for card in self.deck:
            returnStr+= str(card) + "\n"
        return returnStr
            
                
        
        
        
        
        
