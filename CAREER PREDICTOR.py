#career predictor
print("==================================================================================")
print("NOTE : THIS IS FOR FUN PURPOSE!\n")
print("THIS IS YOUR CAREER PREDICTOR!!!!\n")

#score
score=0

#questions 

#Q1
q1=input("Do you prefer working alone or team? :").strip().lower()
if q1==("alone"):
    print("AHH YOU BOOST ALONE TOO!\n")
    score+=1
elif q1==("team"):
    print("AHH NICE!\n")
    
#Q2
q2=input("Are you more creative or logical? :").strip().lower()
if q2==("creative"):
    print("WELL! YOU WANNA DESIGN YOUR NEW GRAND PROJECT!\n")
    score+=1
elif q2==("logical"):
    print("OHO YOU ARE NOT JUST LOGICAL YOU ARE DAM CRAZY IN LOGIC BRO!\n")
        
#Q3    
q3=input("Would you like to put your ASS on stove\nNAH i mean like to take risks?\nYES or NO:").strip().lower()
if q3==("yes"):
    print("AHHH THEN YOU SHOULD GO IN ARMY GET LOSS AND SERVE YOUR COUNTRY!\n")
    score+=1
elif q3==("no"):
    print("OBVIOUSLY WHY WOULD YOU BECAUSE YOU ARE LITTLE MAYBE SMART!\n")
    
#Q4    
q4=input("Do you enjoy moving puzzles?\nYES or NO:").strip().lower()
if q4==("yes"):
    print("OHHH RIGHT THEN YOU ALSO LIKE MOVING YOUR HAND FOR CODING BRO FOR DAM CODING!!!\n")
    score+=1
elif q4==("no"):
    print("HMM NO PROBLEM YOU MOVE IN YOUR BRAIN!\n")
   


#career suggestion
print("=================================================================================")
print("CAREER SUGGESTION!\n")


if score==4:
    print("YOU ARE CRAZY YOU SHOULD CHOOSE SKYDIVING WITH FAULTY PARACHUTE!")
elif score==3:
    print("YOU CAN CHOOSE FREELANCE OR SLEEPING JOB BOTH BUT YOU ARE NICE!")
elif score==2:
    print("YOU SHOULD SLEEP AND WHEN YOUR T LEVELS SPIKES\nYOU CAN DO A CYCLE REPAIRING JOB.")
elif score==1:
    print("YOU FIRST OF ALL MUST ATTEMPT BRAIN SURGERY BY YOURSELF! THEN YOU SHOULD DO LAUNDRY JOB.")
elif score<=0:
    print("BRO LISTEN TO ME YOU SHOULD GO TO YOUR KITCHEN AND MAKE A COFFEE ADD\n1 TEASPOON OF WHITE POWDER YOUR MOM PLACED UNDER THE FRIDGE TRUST ME YOU WILL ENJOY OR REST IN PEACE!")

