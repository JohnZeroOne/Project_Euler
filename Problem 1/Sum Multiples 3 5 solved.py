print """Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

num = 0
tot = 999
sav = 0

while num < tot:
    num += 3
    sav = sav + num
    if num >= tot:
        break
    num += 2
    sav = sav + num
    if num >= tot:
        break
    num += 1
    sav = sav + num
    if num >= tot:
        break
    num += 3
    sav = sav + num
    if num >= tot:
        break
    num += 1
    sav = sav + num
    if num >= tot:
        break
    num += 2
    sav = sav + num
    if num >= tot:
        break
    num += 3
    sav = sav + num
    if num >= tot:
        break
    
print "Answer =", sav
    
