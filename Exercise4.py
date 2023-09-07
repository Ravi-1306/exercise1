total_sum = 0
# collects 5 integer from the users
for i in range(5):
    while True:
        try:
            num = int(input("Enter int: "))
            total_sum += num
            break
        except ValueError:
            print("Invald input. Pleas enter an int.")
print("The sum of the 5 numbers is:", total_sum)
