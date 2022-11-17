from datetime import datetime

def magic_date(date):
    '''Ensure date is in dd/mm/yyyy format with the backslash'''
    
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    
    dd = date_obj.day
    mm = date_obj.month
    yy = date_obj.year
    prod = dd * mm

    #to get the last x digits of any integer => num % 1x (x being number of zeros after 1)
    #e.g: 1234 mod 100 == 34 
    #     1234 mod 10 == 4
    last_one = yy % 10
    last_two = yy % 100
    last_three = yy % 1000

    if prod == last_one or prod == last_two or prod == last_three:
        return True
    else:
        return False

def palindrome_checker(text):
    result = [] 
    text = text.lower()
    
    i = len(text)   #if text = 'abc', len returns length of an iterable, i.e i=3

    for counter in range(i):        #loop will run i times, i.e 3 times...FOR EACH letter in text
        result.append(text[i-1])    #add each character from the end of the text to the result list
        i -=1    
    reversed_text = "".join(result)

    if text == reversed_text:
        return True

    


# magic_date("5/02/2010")
print(palindrome_checker("abcde"))
