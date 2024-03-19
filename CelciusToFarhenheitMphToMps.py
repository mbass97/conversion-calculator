
#converts celsius to farhenheit
def toCelsius(fahrenheit):
    celsius = ((fahrenheit - 32) * (5/9))
    print(celsius)

#converts speed from miles per hour to meters per second
def toMetersPerSecond(milesPerHour):
    milesPerSecond = (milesPerHour * 60 * 60)
    metersPerSecond = (milesPerSecond * 1.609344 * 1_000)
    print(metersPerSecond)

#main function, allows user to select between toCelsius and toMetersPerSecond functions and enter input
def main():
    print("Enter 1 to convert from Fahrenheit to Celsius\n")
    print("Enter 2 to convert speed from miles per hour to meters per second\n")
    mainInput = int(input("Please enter 1 or 2\n"))
    if(mainInput == 1):
        temperature = float(input("Please enter a temperature in Fahrenheit:\n"))
        toCelsius(temperature)
    elif(mainInput == 2):
        speed = float(input("Please enter a speed in Miles per Hour:\n"))
        toMetersPerSecond(speed)
    else:
        print("Error")

#starts the action
main()