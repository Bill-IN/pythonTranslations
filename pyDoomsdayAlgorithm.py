#Python version of doomsdayAlgorithm
import math

#Doomsday algorithm:Calculates day of the week for any given day in the Greogorian calendar.

'''  Sunday"Noneday"=0 			Doomsdates:All of the following dates fall on the same day of the week(doomsday for the year)
  Monday"Oneday"=1				January 3/4(common/leap year)		July 11			December 12
  Tuesday"Twosday"=2			February 28/29(common/leap year)	August 8		March 0(last day of febuary)
  Wednesday"Treblesday"=3		April 4								September 5
  Thursday"Foursday"=4			May 9								October 10
  Friday"Fiveday"=5				June 6								November 7
  Saturday"Six-a-day"=6 '''


#correctModulo function definition
def correctModulo(a, b):

	'''Zero cases'''

	#a = 0 and b = 0
	if ((a == 0) and (b == 0)):
		print("indeterminate : 0 / 0")
		return #break if this condition is met.

	#b = 0
	if (b == 0):
		print("undefined : division by zero")
		return #break if this condition is met.

	#a = 0
	if (a == 0):
		return 0 #The answer is 0.


	'''Negative cases'''

	#a is negative and b is positive
	if ((a < 0) and (b > 0)):
		while (a < 0):
			a = a + b
			'''Keep adding b to a until a becomes positive.
			Then return a.This gives -a mod b'''

		'''In the cycle (0...(b-1)),we are cycling in reverse.
		We start at 0 and move back to b-1 then from b-1 back
		to 0.We do this a times(minus is for direction(backwards)).
		The number in the cycle that we land on is -a mod b.'''

		return a

	#a is positive and b is negative
	if ((a > 0) and (b < 0)):
		while (a > 0):
			a = a + b

			'''Keep adding -b to a until a becomes negative.
			Then return a. This gves a mod (-b)'''

		'''In the cycle (0...-(b-1)), we are cycling in reverse.
		we start at -(b-1) and move down to 0.We do this a times.
		The number we land on in the cycle  is a mod (-b)'''

		return a

	#a is negative and b is negative
	if ((a < 0) and (b < 0)):
		'''C will return the correct result for this operation.It produces the
		correct result when both numbers are positive and when both numbers are
		negative.'''

		return a % b

		'''It may appear strange but this is actually quite
		intuitive.What we are essentially doing is the usual
		modulo operation but with negative numbers.It seems
		as though we are counting down.

		In the cycle (0,-(b-1),...(-b + b-1)),we start at 0 and count up
		to (-b + b-1).Then wrap around and repeat.We do this a times.
		In fact it would be better to display the cycle
		as follows'''

	#a is positive and b is positive
	if ((a > 0) and (b > 0)):
		return a % b


#*************Main program*************

#Tuple containing days of the week(DOTW).
DOTW = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

#List containing doomsdates.
doomsdates = [3,28,0,4,9,6,11,8,5,10,7,12]

#Getting user input.
print("Enter the date in the format dd/mm/yyyy: ")
userInputString = input()
userInputString = userInputString.split('/')
day = int(userInputString[0])
month = int(userInputString[1])
year = int(userInputString[2])

#Use format method to print integers without converting to string.
print("date: {}/{}/{}".format(day, month, year))

#Calculating anchor day for the century.
tmp = year/100
c = math.floor(tmp)
anchor = (5 * ((c % 4) % 7) + 2) % 7 #mod 7 to keep the days in modulo 7
print("\n\nThe anchor day for the century is {}\n\n".format(DOTW[anchor]))

#Calculating the doomsday for the year using the anchor day.
tmp = (year % 100) / 12
a = math.floor(tmp)
b = (year % 100) % 12
tmp = b / 4
e = math.floor(tmp)
doomsday = ((a + b + e) % 7 + anchor) % 7
print("The doomsday for the year is {}\n\n".format(DOTW[doomsday]))

'''Every year that is exactly divisible by four is a leap year,
 except for years that are exactly divisible by 100,
 but these centurial years are leap years if they are exactly divisible by 400.
 For example, the years 1700, 1800, and 1900 were not leap years,
 but the years 1600 and 2000 were.'''
if (((year % 100 == 0) and (year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0))):
    is_a_leap_year = True
    doomsdates[0] = 4
    doomsdates[1] = 29

else:
    is_a_leap_year = False

#Calculating day of the week
if (day >= doomsdates[month-1]):
	tmp = day-doomsdates[month-1] #Counting forward
	difference = abs(tmp);
	dayoftheweek = (doomsday + (difference) % 7) % 7
	print("The day of the week is: {}".format(DOTW[dayoftheweek]))

elif (day < doomsdates[month-1]):
	tmp = day - doomsdates[month-1]; #Counting back
	difference = abs(tmp);
	dayoftheweek = (doomsday - correctModulo(difference,7)) % 7;
	print("The day of the week is: {}".format(DOTW[dayoftheweek]))
