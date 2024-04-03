#30 MARCH 2024

n = float(input("enter number between 0 to 100 : "))

if (n == 0 or n == 100) :
    print("Between 0 to 100 bola hai bhai 0 and 100 nhi daal skte. Run the code again and enter a number between 0 to 100 : TRY AGAIN ")
elif (n > 100):
    print("Your number greater than 100. Run the code again and enter a number between 0 to 100 : TRY AGAIN ")
elif (n >= 1 and  n<=99):
    if (n == 69):
        print("Naughty ho rhe ho :)")
    if (n >= 1 and n <= 50):
        print("Your number is between 0 and 51")
    elif (n >=51 and n <= 99):
        print("Your number is betwwen 50 and 100")
else:
    print("It is a negative number Run the code again and enter a number between 0 to 100 : TRY AGAIN")
