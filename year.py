''' Write a program in python to check a given
 year is a leap year or not leap year..'''

year=int(input("Enter Year Num : "))
if year%100==0:
   if year%400==0:
    print("Leap Year")
   else:
    print("Non Leap Year")
else:
  if year%4==0:
      print("Leap Year")
  else:
      print("Non Leap Year")



''' #Ask the user to enter a year and convert the input into an integer
year = int(input("Enter Year Number: "))

#Check whether the year is divisible by 100.
if year % 100 == 0:

    # If it is divisible by 100, check whether it is also divisible by 400.
    if year % 400 == 0:

        #A year divisible by both 100 and 400 is a leap year.
        print("Leap Year")

       #If the year is divisible by 100 but not by 400, it is not a leap year.
     else:
     print("Non-Leap Year")

#If the year is not divisible by 100, check whether it is divisible by 4.
else:

    #A year divisible by 4, but not by 100, is a leap year.
    if year % 4 == 0:

        #Display the leap-year message.
        print("Leap Year")

    #If the year is not divisible by 4, it is not a leap year.
    else:
        # Display the non-leap-year message.
      print("Non-Leap Year")'''

