'''
Name:Loubna Dufrane
Date:08/07/2014
Assignment: Mad libs
Class: Design Patterns for Web Programming

Mad libs from nursery rhyme -
Three blind mice
'''

#Global Variables
punc = ''

# Inputs - 3 strings and 4 numbers
animal = raw_input("Type in animal in plural:   ")
occupation = raw_input("Type in a profession:  ")
adjective = raw_input("Type in an adjective:   ")
number = raw_input("Type in a number from 2 to 10:  ")
wives = raw_input("Type in any number:  ")
knives = raw_input("Type in another number from 2 to 10:  ")
year = raw_input ("Type in a year: ")


#add number variables into array
numbers_list = [number, knives, wives, year]

#calculate age - using mathematical operator
age = 2014 - int(numbers_list[3])

#add another animal to the mix - using 2nd mathematical operator
total_animals = int(numbers_list[0]) + 1

#condition - check ordinal number
if int(numbers_list[2]) == 1:
    punc = 'st'
elif int(numbers_list[2]) == 2:
    punc = 'nd'
elif int(numbers_list[2]) == 3:
    punc = 'rd'
else:
    punc = 'th'

#condition with logical operator - check to change noun to plural
if (int(numbers_list[1]) == 0  or int(numbers_list[1]) == 1):
    knife = 'knife'
else:
    knife = 'knives'

#dictionary
dict = {'sight': 'blind', 'action': 'run', 'years' : age}

'''
Print Mad libs
'''
#creating loops for repetitive code
for x in range(0, 2):
    print str(total_animals) + " " +  dict['sight'] + " "  + animal + ". "
for y in range(0, 2):
    print "See how they " + dict['action'] + ", see how they " + dict['action'] + "."

print "They all ran after the "+ occupation + "'s " + str(numbers_list[2]) + str(punc) + " "  + str(dict['years']) +  " year old wife."
print "Who cut off their tails with " + str(numbers_list[1]) + " " + adjective + " " + knife + "."
print"Did you ever see such a thing in your life."
print "As " + str(total_animals) + " " + dict['sight'] + " " + animal