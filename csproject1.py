def Intro():
    print("Hello User, Welcome to the Game!")


def scene1(): #choice 2-scene 3, 3- scene4, 1- scene2
    print("Welcome Legends of Avalor!")
    print("                         ")
    print(" The princess of Avalor is in danger")
    print(" Abducted by the infamous Vader Dark and held captive in the Vermillion temple.")
    print(" To start your Legendary journey begin by making a choice")
    print("")
    print("Choice 1: Get out of bed and open the door   ")
    print("Choice 2: Keep sleeping because its a Saturday ")
    print ("Choice 3: Start debating with your friend whether a cereal is a soup?")
    print("Would you like to do Choice 1, 2, or 3?")
    choice1= int(input("Make your choice: "))
    return choice1

def scene2(): #choice 1- scene6, 2- ends, 3- ends
    print("You have selected choice 1!")
    print(" You open the door and leave our house and see an old mysterious house")
    print(" You see an open meadow but don't know what lurks within")
    print(" Finally you see a treacherous river with a unearthly glow")
    print("")
    print("Choice 1: Go into the mysterious house ")
    print(" Choice 2: Go into the meadow ")
    print("  Choice  3: Go towards the river ")
    choice2= int(input("Make your next choice: "))
    return choice2

def scene3(): #ends
    print("You have selected choice 2!")
    print(" You keep sleeping and the princess is killed and Vader Dark takes over the kingdom")
    print(" Game Over (please restart the game to start again)")

def scene4(): #ends
    print("You have selected choice 3!")
    print(" You begin to debate with your friend about cereal")
    print("You suddenly see something crawling within the bushes with a dark aura")
    print("Choice1: Explore what ")
    choice4= int(input("Make your next choice: "))

def scene5(): #if other number is entered than 1, 2 or 3
     print("Invalid input please restart the game ")

def scene6(): #choice 1- ends, 2- scene 7
    print("You have selected choice number 1!")
    print("You go inside the mysterious house and find and an old man sitting by a candle, giggling")
    print(" You tell him about your quest to save the princess")
    print("He murmurs to you how Vader Dark's power can only be broken with the Sword of Life ")
    print("He had long ago once seen it hidden among the meadows shining atop a stone")
    print("He warns you that only the pure of heart can only wield true power")
    print("")
    print("Choice1: ignores the old man's advice and returns back home")
    print("Choice2: Set toward the meadows guided by the old man")                        
    print ("  ")
    choice6= int(input("Make your next choice: "))
    return choice6

def scene7(): #choice 1- scene 9, 2- ends, 3- scene 8
    print(" You have selected choice number 2!")
    print(" You arrive at a luminous meadow with glowing flowers ")
    print("You see it, the legendary sword of life but before you can take it a spirit warrior emerges from the ground")
    print("He tells you that to get the sword of life you must defeat him before")
    print("You embark in the battle fighting fiercely you deliver the final blow defeating the warrior")
    print("Before the warrior fades away he tells you the coordinates of the Vermillion Temple and that")
    print(" only the brave and the pure of heart can bring light to the Kingdom of Light")
    print("")
    print("Suddenly you hear a gigantic explosion, you see the old man's cabin buring, flames fiery")
    print("Choice1:set towards the coordinates to the Vermillion Temple that the warrior tells you ")
    print("Choice2: Go home because you almost lost your life and your tired ")
    print ("Choice3: Runs towards the old man's house")
    choice7= int(input("Make your next choice: "))
    return choice7

def scene9(): #choice 1- scene 12, 2- ends, 3- ends
    print("You have selected choice 1! ")
    print("Despite seeing the old man's house in flames you run past by tears streaming")
    print("Through a treacherous journey, you arrive at a bridge leading to the temple")
    print(" The bridge collapses fire bursts from the ground and dark shadows lurk in every shadow")
    print("As you venture through the halls you realize that Vader Dark was once a knight but was corrupted by greed and darkness")
    print(" You reach the final chamber of the temple and see Vader standing in the center his blade pulsing with a black aura")
    print("")
    print("Choice1: You pull out the Sword of Life and begin fighting")
    print("Choice2: Stunned by the aura, turn and run ")
    print("Choice3: Quickly hide behind a pillar and think of what to do.")
    choice9 = int(input("Make your choice:"))

def scene12(): #choice 1- scene 14, 2- ends, 3- ends
    print("You have selected choice 1!")
    print("You begin your duel and charge towards Vade Dark, your blades clashing and unleashing a fury of attacks")
    print(" Vader Dark soon unleashes a fury of attacks pinning you to a wall, the darkness surrounding you quickly")
    print("Choice1: Decide that you fulfill your duty and keep fighting till the end")
    print(" Choice2: Accept your fate and let the darkness pull you in")
    print(" Choice3: Attempt to make a deal with Vader Dark")
    choice12 = int(input("Make your choice:"))

def scene14(): #ends
    print("You have selected choice 1!")
    print("With all of your strength and courage you unleash one last attack at Vader Dark shattering the dark ")
    print("The shadows vanish and the princess freed from her prison, she runs to you with tears of joy")
    print ("You begin to cry as you realize that you had left the old man behind")
    print("She exclaims how Avalor is forever grateful for your bravery")
    print("Afterward, you return outside with the princess and see the people of Avalor cheering and you see the old man cheering as well")
    print("The End")

def scene10(): # choice 1- scene 11, 2- ends, 3- ends
    print("You have selected choice 1!")
    print("You go through the portal and arrive the temple and begin walking through.")
    print("As you walk through creatures lurk in the shadows and you realize that Vader Dark was once a knight of Avalor but was corrupted by greed")
    print("Finally you reach the highest chamber in the temple and encounter the Vader Dark, his dagger pulsing with a dark aura")
    print("")
    print("Choice1: You pull out the Sword of Life and begin fighting")
    print("Choice2: Stunned by the aura and turn and run ")
    print("Choice3: Quickly hide behind a pillar and think of what to do.")
    choice10 = int(input("Make your choice:"))

def scene11(): # choice 1- scene 13, 2- ends, 3- ends
    print("You have selected choice 1!")
    print(" You remember the old man's words and charge at Vader Dark as he unleashes waves of shadows")
    print("Your duel begins and his shadow blade clashes against your sword's light but he soon unleashes a multiple wave attack, pinning you to the ground")
    print("In the corner of your eye you see the worried princess trembling inside of a cage, tears streaming ")
    print("Choice1: Decide that you fulfill your duty and keep fighting till the end")
    print(" Choice2: Accept your fate and let the darkness pull you in")
    print(" Choice3: Attempt to make a deal with Vader Dark")
    choice11 = int(input("Make your choice:"))

def scene13(): #ends
    print("You have selected choice 1! ")
    print("You decide to valiantly fight to the end remembering your dream to become a hero and save this kingdom")
    print("Summoning all courage you unleash a final move striking Vader Darke shattering the Darkness flooding the chamber with light ")
    print("The shadows vanish and the princess freed from her prison, she runs to you with tears of joy")
    print("She exclaims how Avalor is forever grateful for your bravery")
    print("Afterward, you return outside with the princess and see the people of Avalor cheering")
    print("")
    print("The End")

def scene8(): # choice 1- scene 10, 2- ends, 3- ends
    print("You have selected choice 3!")
    print("")
    print(" You run towards the old man's house seeing the flames ablaze, you hope the old man has escaped safely")
    print("You run into the house and see the old man stuck under the rubble, you decide to help and when you both reach outside safely")
    print("As you see more blasts from the sky. He tells you are truly are the knight that will save this kingdom")
    print("Suddenly the old man opens a mysterious portal and you see the Vermilion Temple on the other side")
    print("")
    print("Choice1: Go valiantly into the portal ")
    print("Choice2: Apologize to the old man and leave ")
    print("Choice3: Enter the portal but, end up in an unknown realm of eternal darkness... ")
    choice8 = int(input("Make your choice:"))
    return choice8

def story():
    Intro()
    choice1 = scene1()
    if choice1 == 1:
        choice2 = scene2()
        if choice2 == 1:
            choice6 = scene6()
            if choice6 == 1:
                # ignores the old man's advice and returns back home (ends)
                print("You ignored the old man's advice and returned home. The princess remains captive. Game Over.")
            elif choice6 == 2:
                choice7 = scene7()
                if choice7 == 1:
                    # set towards the coordinates to the Vermillion Temple (scene 9)
                    choice9 = scene9()
                    if choice9 == 1:
                        # fight Vader Dark (scene 12)
                        choice12 = scene12()
                        if choice12 == 1:
                            scene14()
                        elif choice12 == 2 or choice12 == 3:
                            print("You failed to save the princess. Game Over.")
                    elif choice9 == 2 or choice9 == 3:
                        print("You failed to save the princess. Game Over.")
                elif choice7 == 2:
                    print("You went home. The princess remains captive. Game Over.")
                elif choice7 == 3:
                    choice8 = scene8()
                    if choice8 == 1:
                        choice10 = scene10()
                        if choice10 == 1:
                            choice11 = scene11()
                            if choice11 == 1:
                                scene13()
                            elif choice11 == 2 or choice11 == 3:
                                print("You failed to save the princess. Game Over.")
                        elif choice10 == 2 or choice10 == 3:
                            print("You failed to save the princess. Game Over.")
                    elif choice8 == 2 or choice8 == 3:
                        print("You failed to save the princess. Game Over.")
            else:
                scene5()
        elif choice2 == 2 or choice2 == 3:
            print("You failed to save the princess. Game Over.")
        else:
            scene5()
    elif choice1 == 2:
        scene3()
    elif choice1 == 3:
        scene4()
    else:
        scene5()

story()