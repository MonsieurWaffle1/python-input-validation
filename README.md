# python-input-validation
A basic module for Python that takes input for and validates a variety of data.

To use this module, you can either:
1. Open the main valid file in python and uncomment the desired function.
2. Place the valid file in the same folder as your desierd python project, and call the respected functions using import.

-- FUNCTIONS --
check(input, value)
Checks a string (input) for a specific character (value).
Returns True if the charecter is found ONCE, false if otherwise.
To allow multiple characters, comment out else statement in line 15.

DOB_input()
Takes an input of a DOB from the user and checks to see if it is valid. Loops until a valid input is given.
Returns the valid date in the format DD/MM/YYYY.

email.input()
Takes an input of an email from the user and checks to see if it is valid. Loops until a vaild input is given.
Returns the validated email adress in lowercase format.