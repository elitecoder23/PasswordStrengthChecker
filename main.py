#This is the main file that will have the code to run the application

def check_password_strength(password):

    #Score counter
    score = 0
    feedback = []

# The first thing we want to do is check the length of the password
    password_length = len(password)
    if password_length < 8:
        print("The password is too short")
        score += 1
    elif password_length < 12:
        print("The password is somewhat short so it could be longer")
        score += 2
    elif password_length > 12 and password_length < 16:
        print("The password length is alright")
        score += 3
    else:
        print("The password length is great!")
        score += 4

    for char in password:
        if char in "abcdefghijklmnopqrstuvwxyz":
            has_lower = True
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_upper = True
        if char in "0123456789":
            has_digit = True
        if char in "!@#$%^&*()-+":
            has_special = True

    if has_lower == False:
        feedback.append("Add lowercase letters")
    if not has_upper:
        feedback.append("Add uppercase letters")
    if not has_digit:
        feedback.append("Add digits")
    if not has_special:
        feedback.append("Add special characters")
    
    for element in feedback:
        print(element)
    
    


print("Welcome to the Password Strength Checker!")
print(check_password_strength("12345678"))