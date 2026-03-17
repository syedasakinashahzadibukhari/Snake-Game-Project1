import random

computer = random.choice([1, -1, 0])
user=int(input("Enter ur choice  :   "))
game_dict = { 1 : "SNAKE" ,
             -1 : "WATER" ,
              0 : "GUN"   }
if ( computer == user  ):
    print (" Draw ")
    print(" Computer chooses  ",game_dict[computer])
    print(" You chooses  ",game_dict[user])
elif((computer - user )==-2 or (computer - user )== 1):
    print("you won ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])
else:
    print("you loss")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])