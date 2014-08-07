'''
Name:Loubna Dufrane
Date:08/07/1977
Assignment: Madlibs
Class: Design Patterns for Web Programming

Madlibs from nursery rhyme -
Three blind mice
'''

#Global Variables
punc = ''

# Inputs - 3 strings and 4 numbers
animal = raw_input("Type in animal in plural:   ")
occupation = raw_input("Type in a profession:  ")
adjective = raw_input("Type in an adjective.  ")
number = raw_input("Type in a number from 2 to 10 ")
wives = raw_input("Type in any number:  ")
knives = raw_input("Type in another number from 2 to 10:  ")
year = raw_input ("Type in a year: ")


#add number variables into array
numbers_list = [number, knives, wives, year]

#calculate age
age = 2014 - int(numbers_list[3])

#conditions
if int(numbers_list[2]) == 1:
    punc = 'st'
elif int(numbers_list[2]) == 2:
    punc = 'nd'
elif int(numbers_list[2]) == 3:
    punc = 'rd'
else:
    punc = 'th'

#story
print str(number) + " blind "  + animal + ", " + str(number) + " blind "  + animal + "."
print ", See how they run, see how they run."
print "They all ran after the "+ occupation +"'s " + str(wives) + str(punc) + " wife."
print "Who cut off their tails with " + knives + " " + adjective + " knives."
print" Did you ever see such a thing in your life."
print "As " + str(number) + " blind " + animal