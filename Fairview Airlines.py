#what will be printed inside functions/// basic information (set variables)
data = ' All Fairview Premier Status members are eligible for two complimentary non-oversized checked bags at 70 pounds (32 kg) or less each for travel between the U.S., Canada, Puerto Rico and the U.S. Virgin Islands. For travel to and from international markets (other than the destinations listed above), Fairview Premier Status members are eligible for three complimentary non-oversized checked bags at 70 pounds (32 kg) each or less. (If the bags are oversized and/or overweight, they are subject to the standard overweight and oversize fees so they are not free)'
nonp = " From not being a Premier member you are willing to be charged more based off of your current bag situation"
numberOfBags = input("how many bags do you have?: ")






#initial code begins
def status():
    userStatus = input('Are you a premier member?:')
    clear
    travelStyle= input('How are you traveling today?: (internationally or interlocally, type help to learn more about what these mean)')
    if travelStyle=='help':
        clear
        print('Internationally means you are leaving the country. interlocally means you are traveling internationally but to local locations listed here: U.S., Canada, Puerto Rico and the U.S. Virgin Islands.')
    elif travelStyle == 'internationally':
        internationally=input('where will go be going today?')
        destint = print('you are going to', internationally)
        print(destint)
    if travelStyle=='interlocally':
        clear
        interlocalDest = input("Where will you be traveling today out of the following destinations: U.S., Canada, Puerto Rico and the U.S. Virgin Islands? : ")
    if userStatus == 'yes':
        print(data)
    else:
        print(nonp)
    print(travelStyle)
status();