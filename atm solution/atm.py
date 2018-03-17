def ATM_Distributor(money,request):
    #request=input("Please enter the amount")
    if request > money :
        print "There is Not Enough Money !"
    if request <=0 :
        print "Please enter a positive number !"
    else:
        while request>=100:
            print "give 100"
            request-=100
        while request>=50:
            print "give 50 "
            request-=50
        while request>=10:
            print "give 10"
            request-=10
        while request>=5:
            print "give 5"
            request-=5
        if request>0:
            print "give "+str(request)
    return money

ATM_Distributor(500,277)
