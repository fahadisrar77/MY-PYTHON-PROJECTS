#ACTIVITY RECOMMENDER

print("=" * 50)
print("WELCOME TO ACTIVITY RECOMMENDER!\nPLEASE ANSWER QUESTIONS FOR RECOMMENDATION.\n")



#USER QUESTIONS and condintions 
#q1

q1=input("1.What are you feeling right now TIRED or FRESH?\n:").strip().lower()
if q1 not in ["fresh","tired"]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()
#q2

q2=input("2.Do you enjoy lite exercise plus nature YES or NO?\n:").strip().lower()
if q2 not in["yes","no"]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()
#q3

q3=input("3.Do you love adventure? YES or NO?\n:").strip().lower()
if q3 not in ["yes","no"]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()

#q4

q4=int(input("4.OK now tell your energy level from scale 1-10?\n:"))
if q4 not in [1,2,3,4,5,6,7,8,9,10]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()
#q5

q5=input(f"5.Well your energy level is {q4} so tell what your heart is saying to do \nany intresting task YES or NO?\n:").strip().lower()
if q5 not in["yes","no"]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()

#q6

q6=input("6.Well now last question tell your weather COLD , SUNNY , RAINY?\n:").strip().lower()
if q6 not in ["cold","sunny","rainy"]:
      print("Invalid option, accuracy will be disturbed try again from start!")
      exit()

print("=" * 50)
print("WELL YOUR ACTIVITY RECOMMENDATION IS:\n")

#ACTIVITY RECOMMENDATION
energy=int(q4)

if q1 == "tired" and energy <= 3:
    print("BRO YOU ARE TIRED AND LOW ON ENERGY → BEST TO REST OR WATCH SOMETHING CHILL!")
elif q1 =="tired" and energy in [4,5,6]:
    print("BRO YOU’RE TIRED BUT NOT DEAD → GO FOR A SHORT WALK OR STRETCHING.")
elif q1 == "fresh" and energy >= 7 and q3 == "yes":
    print("BRO YOU GOT AMAZING ENERGY AND LOVE ADVENTURE → GO FOR MOUNTAIN CLIMBING OR CYCLING!")
elif q1 == "fresh" and energy >= 7 and q2 == "yes":
    print("BRO YOU’RE FULL OF ENERGY AND LIKE NATURE → GO FOR A HIKE OR LONG JOG!")
elif energy in [5,6] and q2 == "yes":
    print("YOU’RE DECENTLY ENERGETIC → GO FOR A LITE JOG OR NATURE WALK!")
elif energy in [5,6] and q5 == "yes":
    print("ENERGY IS MID BUT HEART SAYS YES → TRY AN INTERESTING TASK OR INDOOR ACTIVITY!")
else:
    print("BRO MAYBE JUST RELAX, READ A BOOK, OR LISTEN TO MUSIC.")


print("="*50)
print("THANKS FOR PLAYING!")  
           
