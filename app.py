# Register
# email(must contain "@" and ".")
# password( more than 6 symbols, must contain upper and lower - case letters, must contain number, or symbols as:"@","!",ect. )
# login (more or equal to 2 symbols, first letter must be in uppercase)


def is_email_valid(email) :   
    if "@" and "." in email :
        return True
    else :
        print("Invalid email") 
        return False   

def is_password_correct(password) :
    if len(password) < 6 :
        print("Invalid name")
        return False  
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case =  "abcdefghijklmnopqrstuvwxyz"
    has_upper_case = False
    has_lower_case = False
    has_spec_symbol = False
    for symbol_item in password :
        if symbol_item in upper_case :
            has_upper_case = True
        elif symbol_item in lower_case :      
            has_lower_case = True    
        else : 
            has_spec_symbol = True        
    if  has_upper_case == True and has_lower_case == True and has_spec_symbol == True :
        return True  
    else :
        return False

def is_login_correct(login) :
    if len(login) < 2 :
        print("Invalid login")
        return False
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    if login[0] in upper_case : 
         print("Ok")
         return True
    return False    

email = input("Enter your email :")
password = input("Enter your password :")    
login = input("Enter your login :")       

print(is_email_valid(email))
print(is_password_correct(password))
print(is_login_correct(login))
