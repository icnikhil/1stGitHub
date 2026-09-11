''' Wap in python to check a given
 year is a leap year or not..'''

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