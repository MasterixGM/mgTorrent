# Implement Register Interactions and Database Implementation

def register(user, email, password):
    try:
        if(user not in list or email not in list):
            pass
            #db.register(user, email, password)
            #Login.show
        else:
            return "User already exists"
    except:
        print("An error has ocurred try again later")    