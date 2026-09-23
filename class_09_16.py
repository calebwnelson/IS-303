# Print out Day 1, Appointment 1
# Day 1, Appointment 2
# ...
# Day 1, Appointment 5
# Day 2, Appointment 1
# ...
# Day 3, Appointment 5

Day = 1
Appointment = 1

for Day in range(1, 4):
    for Appointment in range(1, 6):
        print("Day", Day, ", Appointment", Appointment)
