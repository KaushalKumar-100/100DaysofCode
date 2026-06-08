print("WELCOME TO TREASURE ISLAND ! YOUR MISSION IS TO FIND THE TREASURE\n")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[_____]
*******************************************************************************
              ''')
choice=input("which side you want to move: left or right\n")
choice=choice.lower().strip()
if choice=="left":
    print("\n Good Job! You have completed the 1st step")
    print("\nPlease enter which you decide to do now :Swim or wait")
    swim=input("\nEnter your opinion:\n")
    swim=swim.lower().strip()
    
    if swim=="wait":
        print("Congrats! you have completed Second step.")
        print("Now last step choose which door you want to go :Red ,yellow or Blue")
        color=input("Enter your selection of gate\n")
        color=color.lower().strip()
        if color=="red":
            print("oo Sorry you are burned by fire. Game Over!\n")
        elif color=="blue":
            print("OO man! you are eaten by beasts .Game Over!\n")
            
        elif color=="yellow":
            print("Congrats You had now become the world richest's person:\n")
        else:
            print("Fucked up! you loose the Game")
        
    else:
        print("Bad Luck ! you are attacked by trout.Game Over\n")
        
    
    
    
else:
    print("you fucked up! you fall into Hole !\n Game Over")
    
