import random
print("WELCOME TO MY GAME")
inp=input("enter odd or even ")
inp1=int(input("Enter number :  "))
comp1=random.choice([1,2,3,4,5,6])
if(inp=="odd" and ((inp1+comp1)%2!=0) or (inp=="even" and ((inp1+comp1)%2==0))):
   print("You won toss")

   choose=input("Enter batting or bowling ")
   user_score=0
   computer_score=0
   if(choose=="batting"):
      print("You Choose Batting.\n You need to enter number between 1 to 6.")
      a=1  
      while(a>0):
         user=int(input("Enter Number : "))
         if(user>6 or user<1):
            print("enter number between 1 to 6")
         else:
            computer=random.choice([1,2,3,4,5,6])
            user_score=user_score + user
            if(user==computer):
               user1=user_score
               print(f"you are out .\n your score is {user_score}.\n Its Computers Batting.")
               

               b=1
               while(b>0):
                  user=int(input("Enter Number : "))
                  if(user>6 or user<1):
                     print("enter number between 1 to 6")
                  else:
                     computer=random.choice([1,2,3,4,5,6])
                     computer_score=computer_score + computer
                     if(user==computer or user_score>computer_score or computer_score>=user_score):
                        c_score=computer_score
                        print(f"Computer is out .\nComputer score is {computer_score}.")
                        if(user1>c_score):
                           print("You WON")
                        elif(user1==c_score):
                           print("it is a draw")
                        else:
                           print("You LOSE")
                        a=-1
                      

   else:
      print("You Choose Bowling.\n You need to enter number between 1 to 6.")
      b=1
      while(b>0):
         user=int(input("Enter Number : "))
         if(user>6 or user<1):
            print("enter number between 1 to 6")
         else:
            computer=random.choice([1,2,3,4,5,6])
            computer_score=computer_score + computer
            if(user==computer):
               c_score=computer_score
               print(f"Computer is out.\n Its Your Batting.\n Computer Score {computer_score}")

               a=1  
               while(a>0):
                  user=int(input("Enter Number : "))
                  if(user>6 or user<1):
                     print("enter number between 1 to 6")
                  else:
                     computer=random.choice([1,2,3,4,5,6])
                     user_score=user_score + user
                     if(user==computer or user_score>computer_score or computer_score>=user_score):
                        user1=user_score
                        print(f"you are out .\n your score is {user_score}.")
                        if(user1>c_score):
                           print("You WON")
                        elif(user1==c_score):
                           print("it is a draw")
                        else:
                           print("You LOSE")
                        b=-1
         


else:
   print("You lose TOSS")
   comp2=random.choice(["batting","bowling"])
   print(f"Computer choose : {comp2}")
   user_score=0
   computer_score=0

   if(comp2=="batting"):
      b=1
      while(b>0):
         user=int(input("Enter Number : "))
         if(user>6 or user<1):
            print("enter number between 1 to 6")
         else:
            computer=random.choice([1,2,3,4,5,6])
            computer_score=computer_score + computer
            if(user==computer):
               c_score=computer_score
               print(f"Computer is out .\nComputer score is {computer_score}.\n Its Your batting")
   
               a=1  
               while(a>0):
                  user=int(input("Enter Number : "))
                  if(user>6 or user<1):
                     print("enter number between 1 to 6")
                  else:
                     computer=random.choice([1,2,3,4,5,6])
                     user_score=user_score + user
                     if(user==computer or user_score>computer_score or computer_score>=user_score):            
                        user1=user_score
                        print(f"you are out .\n your score is {user_score}.")
                        if(user1>c_score):
                           print("You WON")
                        elif(user1==c_score):
                           print("it is a draw")
                        else:
                           print("You LOSE")
                        b=-1
         

   else:
      print("Its Your batting")
      print("enter number between 1 to 6")
      a=1  
      while(a>0):
         user=int(input("Enter Number : "))
         if(user>6 or user<1):
            print("enter number between 1 to 6")
         else:
            computer=random.choice([1,2,3,4,5,6])
            user_score=user_score + user
            if(user==computer):             
               user1=user_score
               print(f"you are out .\n your score is {user_score}.Its Computer Batting")
               b=1
               while(b>0):
                  user=int(input("Enter Number : "))
                  if(user>6 or user<1):
                   print("enter number between 1 to 6")
                  else:
                     computer=random.choice([1,2,3,4,5,6])
                     computer_score=computer_score + computer
                     if(user==computer or user_score>computer_score or computer_score>=user_score):
                        c_score=computer_score
                        print(f"Computer is out .\nComputer score is {computer_score}.")
                        if(user1>c_score):
                           print("You WON")
                        elif(user1==c_score):
                           print("it is a draw")
                        else:
                           print("You LOSE")
                        a=-1
         

      

     
      



