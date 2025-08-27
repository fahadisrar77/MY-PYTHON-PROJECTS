#THE IQ LEVEL PREDICTOR
print("NOTE : THIS IS ALL FOR FUN PURPOSE!\n")
#score
score= 0

#userinputs and conditions


#Q1

q1=input("What is capital of Pakistan?\n(a) Islamabad  (b) Karachi\n(c) Lahore    (d) Multan\n:").strip().lower() 
if q1=="islamabad"or q1=="a":
    print("CORRECT! +1 \n")
    score+=1
else:
    print("WRONG! -1\n")
    
#Q2

q2=input("Which one is the world tallest building?\n(a) Efil tower (b) Washing ton building\n(c) Burj khalifa (d)Centorus Pakistan\n: ").strip().lower() 
if q2=="burj khalifa"or q2=="c":
    print("CORRECT! +1 \n")
    score+=1
else:
    print("WRONG! -1\n")
    

#Q3

q3=input("what comes next in the series 1 3 5 7 9 11 22?\n(a) 33 (b) 23 (c) 32 (d) 1\n:").strip().lower() 
if q3=="33" or q3=="a":
    print("CORRECT! 1+ \n")
    score+=1
else:
    print("WRONG! -1\n")
    

#score
print("==============================================")


print(f"WELL YOUR IQ SCORE IS {score}/3!\n")

#IQ LEVEL ASSIGNMENT

if score==3:
    print("OMG BRO YOU JUST CRACKED! , ARE YOU A SON OF MR ALBART.E?")
elif score==2:
    print("BRO WITH DUE RESPECT YOU HAVE BORN LESS INTELLIGECT SO DONT WORRY\nYOU CAN LIVE WITHOUT BRAIN IQ!")
elif score==0:
    print("NAH NAH I THINK PEOPLE FOUGHT YOUR BRAIN\nIN YOUR CHILDHOOD THAT IS WHY YOU ARE THAT DUMB!!")
elif score==1:
    print("BRO YOU KNOW YOUR FULL BODY STRESSED THAT NIGHT THAT IS WHY YOU\nARE DUMB! NOW TRAIN YOURSELF!!!")        


