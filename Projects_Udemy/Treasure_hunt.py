print("Welcome to Treasure Island. Your mission is to find the treasure.")
choose_1 = input("Left or Right?")

if choose_1 == "Left":
    choose_2 = input("Swim or Wait")
    if choose_2 =="Wait":
        choose_3 = input("which door Red or Blue or Yellow?")
    else:
        print("Attacked by trout. Game over")
        if choose_3 == "Red":
            print("Burned by fire. Game over")
        elif choose_3 == "Blue":
           print("Eaten by beasts. Game over")
        elif choose_3 == "Yellow":
            print("You Win!")
        else:
            print("Game over")
else:
    print("Fall into a hole.Game over")