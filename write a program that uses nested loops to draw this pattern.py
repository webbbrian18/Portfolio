# Brian Webb
#ITEC 209
#Write a program that uses nested loops to draw this pattern

number_of_asterisks = 7 

def draw(number_of_asterisks):
    for i in range(number_of_asterisks):
        asterisk = ""
        for _ in range(number_of_asterisks-i):
            asterisk += "*"
        print(asterisk)

draw(number_of_asterisks)
