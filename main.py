#This is the main file that will have the code to run the application

def check_password_strength(password):

    #Score counter
    score = 0
    feedback = []

# The first thing we want to do is check the length of the password
    password_length = len(password)
    if password_length < 8:
        return "The password is way too short"
        score += 1
    elif password_length < 12:
        return "The password is somewhat short so it could be longer"
        score += 2
    elif password_length > 12 and password_length < 16:
        return "The password length is alright"
        score += 3
    else:
        return "The password length is great!"
        score += 4

    
    

    