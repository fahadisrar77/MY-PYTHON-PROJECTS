#THE AUTHENTICATOR

#PASSWORD
main_password="secret123"
backup_pin=7890

#user input
ask=input("PLEASE ENTER THE MAIN PASSWORD :")
#conditions

if ask==main_password:
    print("ACCESS LEVEL 1\nBASIC ACCESS GRANTED.")
    exit()
else:
    print("WRONG PASSWORD!")
#user input  
    ask2=(int)(input("ENTER BACKUP PIN :"))
#conditions
if ask2==backup_pin:
    print("ACCESS LEVEL 2\nBACKUP ACCESS GRANTED.")
else:
    print("INTRUDER ALERT\nACCESS DENIED")        
print("INVALID INPUT\nACCESS DENIED")




