letter = ''' Dear <|NAME|> ,
you are selected!

Date : <|DATE|>
'''
name = input("enter your name\n")
date = input("enter your date\n")

letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)

print(letter)
