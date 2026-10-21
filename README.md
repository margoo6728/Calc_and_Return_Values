# Calc_and_Return_Values
ECPI 202610E OL SDC205L AO Python for Data Analytics Lab

## 3.4 Project: Calculations and Return Values

# Criteria
- Write a function called convertData that takes one argument as the data to be converted and returns the converted value appropriate for the spreadsheet selected. The conversion formulas are as follows:
  > F to C: (F - 32) * 5/9
  > lbs to Kg: lbs / 2.205
  > in to cm: in * 2.54
- Write a function called getInput that takes no arguments and performs the following actions:
  > Asks the end-user how many entries are being entered.
  > Within a for-loop, ask the end-user to enter a date and a <value> where <value> is either temperature as F, weight as lbs., or rain in inches. Do this equal to the number inputted by the end-user.
  > Within the for-loop, call the convertData function and pass in the numerical value to be converted. Add a comment above the line calling convertData. It should also state the name of the function, the argument required, and the expected return value.
  > Within the for-loop, print "The following was saved at <datetime.now()>:" followed by the end-user's inputted date, numerical value, and converted value.
- Write an if statement below your previous error-checking code that calls getInput() if the end-user entered 1 from the presented menu and writes an else statement that prints "Error: The chosen functionality is not implemented yet" if anything other than "1" is selected.
