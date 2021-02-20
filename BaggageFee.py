def numOfBags(bags, internationalS, premier):
    bagFee=0
    input = int(bags)
    for bag in range(1,bags+1):
        if bag == 1 and premier=='n':
            bagFee=bagFee+25
        elif bag == 2 and premier=='n':
            bagFee=bagFee+35
        elif bag == 3 and premier =='n':
            bagFee=bagFee+100
        elif bag==3 and premier=='y' and internationalS=='n':
            bagFee = bagFee+100
        elif bag > 3:
            bagFee=bagFee+100
    return bagFee

def overweight(bagsoverweight):
    overWeightFee=0
    overweight=input("are any of your bags overweight? (y/n):  ")
    if overweight == 'y':
        numOfbagsOverweight=input("how many bags are overweight?:  ")
        numOfbagsOverweight=int(numOfbagsOverweight)
        for weights in range(1,numOfbagsOverweight+1):
            weight=input("how much does this bag weigh?:  ")
            weight=int(weight)
            if weight > 70:
                overWeightFee=overWeightFee+200
            elif weight > 50:
                overWeightFee=overWeightFee+100
    return overWeightFee
    
def oversized(bags):
    oversizeFee=0
    oversizednum=0
    oversized=input("are any of your bags oversized? (y/n):  ")
    if oversized == 'y':
        oversizednum=input("how many bags are oversized?:  ")
        oversizednum=int(oversizednum)
    if oversizednum >= 1 :
        oversizeFee=oversizeFee+100*oversizednum
    if oversized =='n':
        oversizedFee=oversizeFee+0
    return oversizeFee

def status(internationalS):
    totalfee=0
    if internationalS =='y' and premier=='y':
        if overweight == 'n' and oversized=='n':
            totalfee=totalfee-numOfBags(bags)
    return totalfee

def weightoversize(oversized, overweight):
    weightoversizeFee=0
    if overweight =='y' and oversized =='y':
        if oversizeFee > overWeightFee:
            return weightoversizeFee+oversizeFee-overWeightFee
        elif overWeightFee > oversizeFee:
            return weightoversizeFee+overWeightFee
    return weightoversizeFee
    


totalfee=0
bags=input("How many bags do you have?:  ")
bags=int(bags)
internationalS=input("are you traveling internationally? (y/n):  ")
premier=input("Are you a premier member? (y/n):  ")
        

totalfee=totalfee+numOfBags(bags, internationalS, premier)
print(totalfee)
totalfee=totalfee+overweight(bags)
print(totalfee)
totalfee=totalfee+oversized(bags)
totalfee=totalfee+weightoversize(oversized, overweight)
totalfee=totalfee-status(internationalS)
print("your total fee is $",totalfee)

    
