# Marleyna Goodrich
# 3.4 Project: Calculations and Return Values

from datetime import datetime

# Convert Fahrenheit to Celsius
def convertData(value):
    if conversionType == "1":
        convertedValue = (value - 32) * 5 / 9
    elif conversionType == "2":
        convertedValue = value / 2.205
    else:
        convertedValue = value * 2.54
    return convertedValue

# Collect dates and tempretures
def getInput():
    global conversionType
    
    print("What type of data would you like to enter?")
    print("1 Temperature (Fahrenheit)")
    print("2 Weight (Pounds)")
    print("3 Rain Amount (Inches)")

    conversionType = input()
    
    numberOfEntries = int(input("How many entries are you inputting?\n"))

    for entry in range(numberOfEntries):
        entryDate = input("Enter a date:\n")

        if conversionType == "1":
            value = float(input("Enter the highest temp for the inputted date:\n"))
        elif conversionType == "2":
            value = float(input("Enter the weight in pounds for the inputted date:\n"))
        else:
            value = float(input("Enter the rain amount in inches for the inputted date:\n"))

        # Call convertData with a float argument and expect a float return value
        convertedValue = convertData(value)

        print(f"The following was saved at {datetime.now()}:")
        print(f"{entryDate},{value},{convertedValue}\n")
        
# Display Spreadsheet Automation Menu
print("margoo6728's Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1 Input Data")
print("2 View Current Data")
print("3 Generate Report")

number = input()

timestamp = datetime.now()
print(f"You selected {number} at {timestamp}\n")

# Call getInput when option 1 selected
if number == "1":
    getInput()
else:
    print("Error: The chosen functionalisty is not implemented yet")
        
    
