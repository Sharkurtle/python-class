# defines the assumptions made in the original problem
familyMembers = 4
slicesInPizza = 8

# ask and get input if everyone wants the same number of slices
print('Does everyone want the same number of slices? [Y/N]')
everyPplWantsSame = str(input())

# if everyone wants same number of slices then go down the Y tree if not then go down the N tree
if everyPplWantsSame == 'Y':
    # asks and gets input on how many slices everyone wants
    print('How many slice(s) does each person want?')
    slicesEachPplWant = input()

    # tries to change the last asked for value into an integer, if not integer, end run, if integer, continue run
    try:
        int(slicesEachPplWant)
        print('Everyone wants', slicesEachPplWant, 'slice(s)')
        # next three vars calculate or define total slices needed, how many pizzas are needed,
        # and how many slices will be left over
        totalSlices = int(slicesEachPplWant) * int(familyMembers)
        pizzasNeeded = 0
        slicesLeftover = 0
        # calculate pizzasNeeded and slicesLeftover based on what the value of totalSlices is
        if totalSlices % slicesInPizza == 0:
            pizzasNeeded = totalSlices // slicesInPizza
        else:
            pizzasNeeded = (totalSlices // slicesInPizza) + 1
            slicesLeftover = (pizzasNeeded * slicesInPizza) - totalSlices

        # gives output of successful run
        print('You need', pizzasNeeded, 'pizza(s) and will have', slicesLeftover, 'slices left')

    # ends run if there's a value error when attempting to change slicesEachPplWant to an int
    except ValueError:
        print('Please enter a whole number next time')

# tree for if not everyone wants the same number of slices
elif everyPplWantsSame == 'N':

    # next four prints and vars ask for and define how many slices each person wants respectively
    print('How many slice(s) does person 1 want?')
    person1Slices = input()

    print('How many slice(s) does person 2 want?')
    person2Slices = input()

    print('How many slice(s) does person 3 want?')
    person3Slices = input()

    print('How many slice(s) does person 4 want?')
    person4Slices = input()

    # same as last try and except check
    # tries to change the last asked for value into an integer, if not integer, end run, if integer, continue run
    try:
        # next three vars calculate or define total slices needed, how many pizzas are needed,
        # and how many slices will be left over
        totalSlices = int(person1Slices) + int(person2Slices) + int(person3Slices) + int(person4Slices)
        print('The total needed slices is', totalSlices)
        pizzasNeeded = 0
        slicesLeftover = 0

        # calculate pizzasNeeded and slicesLeftover based on what the value of totalSlices is
        if totalSlices % slicesInPizza == 0:
            pizzasNeeded = totalSlices // slicesInPizza
        else:
            pizzasNeeded = (totalSlices // slicesInPizza) + 1
            slicesLeftover = (pizzasNeeded * slicesInPizza) - totalSlices

        # gives output of successful run
        print('You need', pizzasNeeded, 'pizza(s) and will have', slicesLeftover, 'slices left')

    # ends run if there's a value error when attempting to change slicesEachPplWant to an int
    except ValueError:
        print('Please make sure all entered values are whole number next time')
