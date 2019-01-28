# division
##def sum3_5(total):
##    withthree = 3
##    totthree = total / withthree
##    addthree = 0
##    print "total three", totthree
##    withthree -= 3
##    
##    while withthree <= totthree:
##        withthree += 3
##        addthree = addthree + withthree
##
##    print addthree
##
##    withfive = 5
##    totfive = total / withfive
##    addfive = 0
##    print "total five", totfive
##    withthree -= 5
##    
##    while withfive <= totfive:
##        withfive += 5
##        addfive = addfive + withfive
##
##    print addfive
##
##    print addthree + addfive
##    
##sum3_5(1000)

def sum3_5(total):
    withthree = 3
    totthree = total / withthree
    addthree = 0
    print "total three", totthree
    withthree -= 3
    withfive = 5
    totfive = total / withfive
    addfive = 0
    print "total five", totfive
    withthree -= 5
    
    while withthree <= totthree or withfive <= totfive:
        withthree += 3
        addthree = addthree + withthree
        withfive += 5
        addfive = addfive + withfive

    print addthree + addfive


    
    
sum3_5(1000)
