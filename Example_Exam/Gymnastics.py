country = input()
ured = input()

sum_trudnost = 0
sum_izpulnenie = 0

if country == "Russia":
    if ured == "ribbon":
        sum_trudnost = 9.100
        sum_izpulnenie = 9.400
    elif ured == "hoop":
        sum_trudnost = 9.300
        sum_izpulnenie = 9.800
    elif ured == "rope":
        sum_trudnost = 9.600
        sum_izpulnenie = 9.000

elif country == "Bulgaria":
    if ured == "ribbon":
        sum_trudnost = 9.600
        sum_izpulnenie = 9.400
    elif ured == "hoop":
        sum_trudnost = 9.550
        sum_izpulnenie = 9.750
    elif ured == "rope":
        sum_trudnost = 9.500
        sum_izpulnenie = 9.400

elif country == "Italy":
    if ured == "ribbon":
        sum_trudnost = 9.200
        sum_izpulnenie = 9.500
    elif ured == "hoop":
        sum_trudnost = 9.450
        sum_izpulnenie = 9.350
    elif ured == "rope":
        sum_trudnost = 9.700
        sum_izpulnenie = 9.150


total = sum_trudnost + sum_izpulnenie


diff = 20 - total
percent = (diff / 20) * 100


print(f"The team of {country} get {total:.3f} on {ured}.")
print(f"{percent:.2f}%")
