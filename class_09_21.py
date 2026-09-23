numbers = [12, -15, 16, 14, -16]
negative_count = 0
positive_count = 0
zero_count = 0

for i in range(len(numbers )):
    if numbers[i] < 0:
        print("Negative number detected: ", numbers[i])
        negative_count += 1
    elif numbers[i] > 0:
        print("Positive number detected: ", numbers[i])
        positive_count += 1
    else:
        print("Zero detected: ", numbers[i])
        zero_count += 1

if positive_count > 0:
    print("Total positive numbers: ", positive_count)
if negative_count > 0:
    print("Total negative numbers: ", negative_count)
if zero_count > 0:
    print("Total zero numbers: ", zero_count)