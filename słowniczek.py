drivers = {
    "Lewis Hamilton" : 44 ,
    "Sebastian Vettel" : 5,
    "Carlos Sainz" : 55,
    "Daniel Ricciardo" : 3,
}

print(len(drivers))
print(drivers)
print(drivers["Sebastian Vettel"])
print("Robert Kubica" in drivers)
print("Lewis Hamilton" in drivers)
drivers ["Robert Kubica"] = 1
print(drivers)
for driver in drivers:
    print(driver)