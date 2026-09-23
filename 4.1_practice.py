# Author: Caleb Nelson
# Purpose: Write a program that prompts the user for a first name, 
# last name, street address, city, state, and the birth year of the 
# individual. Calculate the age of the individual. Print the concatenated 
# full name all in upper case separated by a space. Print the address 
# on a separate line. Print the city and state on another separate 
# line separated by a tab. Make sure the state is all upper case. 
# Print the calculated age in years on another separate line concatenated 
# with "In 2020 ZZ was XX years old" - where ZZ is the first name and XX 
# is the calculated age in years.

# Gather user inputs
sFirstName = input("Enter your first name: ").upper()
sLastName = input("Enter your last name: ").upper()
sStreetAddress = input("Enter your street address: ")
sCity = input("Enter your city: ")
sState = input("Enter your state two-letter abbreviation: ").upper()
sBirthYear = input("Enter your birth year ")

#Calculate age
iBirthYear = int(sBirthYear)
sAge = str(2026-iBirthYear)

#Format and print output
print(sFirstName + " " + sLastName)
print(sStreetAddress)
print(sCity, sState, sep="\t")
print("In 2026 " + sFirstName + " was " + sAge + " years old")