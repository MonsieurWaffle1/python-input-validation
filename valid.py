def check(input, value):
    # Checks a string for a specific value.

    # Declares starting variables
    present = False
    valid = False
    
    # Increments through the string
    for letter in input:
        if letter == value:
            # Only valid if appears once
            if present == False:
                present = True
                valid = True
            else:
                valid = False
    return valid

def DOB_validate(date):
    # Declares starting variables
    valid = True
    limit = 0
    codes = []
    current_year = 2024
    min_year = current_year - 120

    # Check 1
    if date == '':
        valid = False
        codes.append(1)
        return valid, codes

    # Check 2
    if len(date) != 10:
        valid = False
        codes.append(2)
        return valid, codes

    # Check 3
    if date[2] != '/' or date[5] != '/':
        valid = False
        codes.append(3)
        return valid, codes
    
    # Seperates the input
    try:
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    except:
        codes.append(3)
        return False, codes

    # Check 4 
    if day < 1:
        valid = False
        codes.append(4)
    if not 0 < month < 13:
        valid = False
        codes.append(5)
    if not min_year < year < (current_year + 1):
        valid = False
        codes.append(6)

    # Check 5
    if month == 2:
        if year % 4 == 0:
            limit = 29
        else:
            limit = 28
    elif month == 4 or 6 or 8 or 10 or 12:
        limit = 31
    elif month == 1 or 3 or 5 or 7 or 9 or 11:
        limit = 30
    else:
        valid = False
        codes.append(5)
    if limit != 0:
        if day > limit:
            valid = False
            codes.append(4)

    return valid, codes
        
def DOB_input():
    # Gets a DOB from the user and validates.

    # Defines the error codes
    valid = False
    error_codes = {
        1 : 'No input entered!',
        2 : 'Date wrong length!',
        3 : 'Date wrong format!',
        4 : 'Day out of range!',
        5 : 'Month out of range!',
        6 : 'Year out of range!',
    }

    while valid == False:
        # Gets the user's initail input.
        print('Please give your date of birth. DD/MM/YYYY ')
        date = input('')
        valid, codes = DOB_validate(date)
        if valid != True:
            for code in list(set(codes)):
                print(error_codes[code])
    print('The provided date is valid.')

def validate_email(email):
    # Declares starting variables
    valid = True
    codes = []
    email = email.lower()

    # Check 1
    if email == '':
        codes.append(1)
        return False, codes

    # Check 2
    if not check(email, '@'):
        codes.append(2)
        valid = False
    
    # Check 3
    if email[0] == '.' or email[-1] == 0:
        codes.append(3)
        valid = False
    
    # Check 4
    if not check(email, '.'):
        codes.append(4)
        valid = False

    return valid, codes  

def email_input():
    # Gets an email from the user and validates.

    # Declares starting variables
    valid = False
    error_codes = {
        1 : 'No input given',
        2 : 'No/too many "@"s',
        3 : '"." in invalid position',
        4 : 'No/too many "."s'
    }

    while valid == False:
        email = input('Please enter your email: \n')
        valid, codes = validate_email(email)
        if valid == False:
            for code in codes:
                print(error_codes[code] + ' -_-')
    return(valid)

# print(DOB_input())
# print(email_input())
