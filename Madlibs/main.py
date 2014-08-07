'''
Name:Loubna Dufrane
Date:08/07/1977
Assignment: Madlibs
Class: Design Patterns for Web Programming

Three blind mice, three blind mice,
See how they run, see how they run,
They all ran after the farmer's wife,
Who cut off their tails with a carving knife,
Did you ever see such a thing in your life,
As three blind mice?

'''
# Inputs - 3 strings and 3 numbers
animal = raw_input("Type in animal in plural. i.e. pigs  ")
occupation = raw_input("Type in a profession. i.e. Painter  ")
adjective = raw_input("Type in an adjective.  ")
number = raw_input("Type in a number ")
wives = raw_input("Type in another number ")
knives = raw_input("Type in another number  ")

#initial story
print str(number) + " blind "  + animal + ", " + str(number) + " blind "  + animal + ", See how they run, see how they run, They all ran after the "+ occupation +"'s " + str(wives) + "th wife, Who cut off their tails with " + knives + " " + adjective + " knives, Did you ever see such a thing in your life, As " + str(number) + " blind " + animal