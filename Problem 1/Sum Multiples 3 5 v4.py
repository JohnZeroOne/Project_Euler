def multiplesof3_5(inside):
    
    multiples = 0
    total = 0
    
    while multiples < inside:
        multiples += 3
        total += multiples
        multiples += 2
        total += multiples
        multiples += 1
        total += multiples
        multiples += 3
        total += multiples
        multiples += 1
        total += multiples
        multiples += 2
        total += multiples
        multiples += 3
        total += multiples
        
    print total

multiplesof3_5(1000)
