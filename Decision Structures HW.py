# what is the speed limit, User speed, and distance traveled
print('What is the speed limit (mph)')
speedLimit = input()
print('What is your speed (mph)')
userSpeed = input()
print('What distance are you driving (mi)')
distanceDriven = input()


# attempts to change previous vars to ints if one isn't an int exit code, if all are ints continue
try:
    speedLimitB = int(speedLimit)
    userSpeedB = int(userSpeed)
    distanceDrivenB = int(distanceDriven)

    # gets the total time driven while driving the speed limit (hrs)
    timeDrivingOnLimit = distanceDrivenB / speedLimitB

    # gets the total time driven while driving the user's speeding speed (hrs)
    timeDrivingOnUserV = distanceDrivenB / userSpeedB

    # gets the total time driven in hours then converts to minutes
    minutesSaved = (timeDrivingOnLimit - timeDrivingOnUserV) * 60

    # prints the minutes saved
    print("You saved ", int(minutesSaved), ' mins')

except ValueError:
    print('Please enter a positive, whole integer')
