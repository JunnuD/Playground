alku = int(input("Viikonpäivän numero lomalle lähtöön? "))
kesto = int(input("Kuinka pitkä loma on päivissä? "))

def saa_paiva(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"




day = (kesto % 7) + alku

print(saa_paiva(day))