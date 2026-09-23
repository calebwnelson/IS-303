# A program that estimates the cost of a road trip by asking the user for trip information, 
# performing calculations, and displaying a personalized trip-cost summary.

# Gather inputs
user_name = input("Please enter your first and last name: ")
destination = input("Please enter your destination: ")
one_way_distance = float(input("Please enter the one-way distance to your destination in miles: "))
mpg = float(input("Please enter the miles per gallon of the vehicle you will be driving: "))
gas_price_per_gallon = float(input("Please enter the current price of gas per gallon: "))
num_travelers = int(input("Please enter the number of travelers: "))

# Calculate variables
round_trip_miles = one_way_distance*2
req_gas = round_trip_miles/mpg
est_gas_cost = req_gas*gas_price_per_gallon
est_cost_per_traveler = est_gas_cost/num_travelers

#Print out readable trip summary
print("Traveler name: " + user_name)
print("Your destination: " + destination)
print(f"Total estimated cost: ${est_gas_cost: .2f}")
print(f"Estimated cost per traveler: ${est_cost_per_traveler: .2f}")