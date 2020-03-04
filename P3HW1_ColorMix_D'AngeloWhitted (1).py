# CTI-110
# P3HW1 - Color Mixer
# D'Angelo Whitted
# Feburary 26, 2020

#Enter a primary color
primarycolor1 = input("Enter primary color 1: ")
primarycolor2 = input("Enter primary color 2: ")

if primarycolor1 == 'red' and primarycolor2 == 'blue' or primarycolor1 == 'blue' and primarycolor2 == 'red':
    print( 'primarycolor1 mixed with primarycolor2 is purple' )
elif primarycolor1 == 'red' and primarycolor2 == 'yellow' or primarycolor1 == 'yellow' and primarycolor2 == 'red':
        print( 'primarycolor1 mixed with primarycolor2 is orange')
elif primarycolor1 == 'blue' and primarycolor2 == 'yellow' or primarycolor1 == 'yellow' and primarycolor2 == 'blue':
        print ( 'primarycolor 1 mixed with primarycolor2 is green')
else:
    print ('second color is not a primary color')

    
    
        


    
