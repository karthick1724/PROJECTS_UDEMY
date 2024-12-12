print("Welcome to Treasure Island. Your mission is to find the treasure.")
choose_1 = input("Left or Right?").lower()

if choose_1 == "left":
    choose_2 = input("Swim or Wait").lower()
    if choose_2 =="wait":
        choose_3 = input("which door Red or Blue or Yellow?").lower()
        if choose_3 == "red":
            print("Burned by fire. Game over")
        elif choose_3 == "blue":
           print("Eaten by beasts. Game over")
        elif choose_3 == "yellow":
            print("You Win!")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game over")
else:
    print("Fall into a hole.Game over")