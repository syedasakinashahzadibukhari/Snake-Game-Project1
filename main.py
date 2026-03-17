'''
1 for snake
-1 for water
0 for gun

00 draw 
11 draw
1-1 u loss 
-1 1 u win 
10 u win
01 u loss
-1 0 u loss 
0 -1 u won

'''
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

elif( computer == 1 and user == -1 ): # 2
    
    print(" You loss ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

elif( computer == -1 and user == 1 ): #2
    
    print(" You win ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

elif( computer == 1 and user == 0 ): #1
    
    print(" You win ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

elif( computer == 0 and user == 1 ): #1
    
    print(" You loss ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

elif( computer == -1 and user == 0): 
    
    print(" You loss ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

elif( computer == 0 and user == -1 ):#0
    
    print(" You win ")
    print(" Computer chooses ",game_dict[computer])
    print(" You chooses ",game_dict[user])

else:
    print("u r so dumb")








    
