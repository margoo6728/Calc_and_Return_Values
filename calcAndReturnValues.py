# Marleyna Goodrich
# 3.4 Project: Calculations and Return Values

from datetime import datetime

# Convert the inputted value based on the selected data type
def convertData(value):
    if conversionType == "1":
        convertedValue = (value - 32) * 5 / 9
    elif conversionType == "2":
        convertedValue = value / 2.205
    else:
        convertedValue = value * 2.54
    return convertedValue

# Collect dates and numerical values based on the selected data type
def getInput():
    global conversionType

    # Display data type options for the user
    print("What type of data would you like to enter?")
    print("1 Temperature (Fahrenheit)")
    print("2 Weight (Pounds)")
    print("3 Rain Amount (Inches)")

    conversionType = input()

    while conversionType not in ("1", "2", "3"):
        print("Invalid selection. Please enter 1, 2, or 3.")
        conversionType = input()
    
    numberOfEntries = int(input("How many entries are you inputting?\n"))

    # Repeat data entry based on the number of enteries selected
    for entry in range(numberOfEntries):
        entryDate = input("Enter a date:\n")

        # Request a numerical value based on the selected data type
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
    print("Error: The chosen functionality is not implemented yet")
        
    
