leap_year = []
current_year = int(input("Enter Current Year "))
final_year = int (input("Enter Final Year "))


for year in range(current_year ,final_year +1):
    if year %4 == 0 and(year % 100 !=0 or year % 400 == 0 ):
        leap_year.append(year)


print("leap years ,",leap_year)
