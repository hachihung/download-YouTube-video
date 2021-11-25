import time

number = input("Enter a number: ")

while True:
    sum = 0
    for digit in number:
        sum = sum + int(digit)**2
    print(sum)
    number = str(sum)
    time.sleep(1)
    if int(number) == 1:
        break
