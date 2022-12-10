gender=input("What is your gender(M/F): ")

price=int(input("car price: "))

if gender=="M":
    age=int(input("age: "))
    if age<=23:
        print("insurance of the car:",(23/100)*price)
    else:
        print("insurance of the car:",(9/100)*price)
elif gender=="F":
    car=input("Your car is(sports/non-sports): ") 
    if car=="sports":
        print("insurane of the car:",(21/100)*price)
    else:
        print("insurance of the car:",(10/100)*price)
else:
    print("Invalid")