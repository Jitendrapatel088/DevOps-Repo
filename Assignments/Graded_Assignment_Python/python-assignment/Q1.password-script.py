def check_password_strength(password):
    ##check password strength
    if len(password) <8:
        return False
    ##upper case and lower case check
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    ##digit check
    if not any(char.isdigit() for char in password):
        return False
    ##special charaters check
    special_characters = "!@#$%"
    if not any(char in special_characters for char in password ): 
        return False
    ##if all criteria match 
    return True

password = input("Please Enter your password:- ")

##Check password strength 
if check_password_strength(password):
    print ("Password is strong. Good job!")
else:
    print ("Password strength not meet. Please try again")
