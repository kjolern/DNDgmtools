import dice
import npcgenerator
import villaingenerator
import sys

#main function with menu that enters the chosen module of the program.
def main():
    while True:
        print(" ")
        print(25 * "*")
        print("1.Dice Roller")
        print("2.Generate NPC")
        print("3.Generate Villain")
        print("4. Quit")
        print(25 * "*")
        print(" ")

        userchoice = input("Enter the number of the function you want to run and press enter: ")

        if userchoice == "1":
            dice.diceroller()
            main()

        elif userchoice == "2":
            npcgenerator.npcgen()
            main()

        elif userchoice == "3":
            villaingenerator.villgen()
            main()
        
        elif userchoice =="4":
            sys.exit()

        else:
            print("Invalid choice")
            print(25* "*")
            main()



if __name__=="__main__":
    main()