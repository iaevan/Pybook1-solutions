#it takes about 100 guesses to guess the number
#uses binary search
import random
number = random.randint(1,1000000000000000000000000000000)
attemps = 0
low = 0
high = 1000000000000000000000000000000
while True:
    print("guess the number: ")
    input_number = (low + high) // 2
    print("my guess is", input_number)
    attemps += 1

    if input_number == number:
        print("youre correct!")
        break
    if input_number > number:
        print("way bigger")
        high = input_number - 1
    else:
        print("way smaller")
        low = input_number + 1

print("you tried", attemps, "times")

