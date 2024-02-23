import time

def countdown():
    t = int(input("Enter coundown time in seconds: "))
    for x in range (t,0,-1): # we can aslo do reversed(range(0,t))
        seconds = x % 60 #since it cannot be above 60
        minutes = int(x / 60) #60sec = 1 min
        hours = int(x / 3600)# we don't add %24 since we are not including days
        
        print(f'{hours:02}:{minutes:02}:{seconds:02}')# to make it display it with 2 digits
        time.sleep(1)
    print("Time's up!")
    
countdown()

        