# number of each pastry in stock
muffins = 10
cupcakes = 10

# loops if there is still stock and stops if there is not
while not ((muffins <= 0) and (cupcakes <= 0)):

    # ask for which pastry theyre buying, or if the shop is done selling for the day
    print('Do you want a muffin or cupcake? Or, are you done selling? [0]')
    whichPastry = input()

    # attempt to change to string loops again if value error
    try:
        str(whichPastry)

        # if the chosen pastry is muffin take one stock off muffin. if chosen pastry is cupcake, take one off cupcake.
        # if the user entered 0, then exit code and print the stock left
        if whichPastry == 'muffin':
            if muffins <= 0:
                print('Muffins are out of stock')
            else:
                muffins -= 1
                print('You bought 1 muffin')
        elif whichPastry == 'cupcake':
            if cupcakes <= 0:
                print('Cupcakes are out of stock')
            else:
                cupcakes -= 1
                print('You bought 1 cupcake')
        # note, changes the pastry stock values to -10000 so that the while loop stops looping
        elif whichPastry == '0':
            print('muffins:', muffins, 'cupcakes:', cupcakes)
            muffins = -10000
            cupcakes = -10000

        else:
            print('Please enter "muffin", "cupcake", or "0" next time.')

    except ValueError:
        print('Please enter "muffin" or "cupcake" next time.')

    # if stock runs out, notify user and end code
    if (cupcakes == 0) and (muffins == 0):
        print('All out of stock come again soon!')