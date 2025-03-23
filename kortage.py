def daysFromStart(day, month):
    if day>=1 and day<=30  and month>=1 and month<=12:
        return (month - 1) * 30 + day
    else:
        print("Помилка")

def showInfo(day, month):
    if day and month:
        print(f"Днів з початку року: {daysFromStart(day, month)}")

showInfo(1,1)

countries = {
    "Україна": "Київ",
}

def find(country):
    print(countries.get(country,"Інформація відсутня"))

def add(country, capital):
    countries[country] = capital


find("Україна")
add("Італія", "Рим")
find("Італія")
