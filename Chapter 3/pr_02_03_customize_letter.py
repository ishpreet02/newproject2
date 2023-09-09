letter = '''Dear <|NAME|>,
Greetings!
We are happy to let you know about your selection at Akamai.

You have been selected!

Thanks & regards,
Ish
Date: <|DATE|> '''

name = input("Enter your name: \n")
date = input("Enter the date: \n")

letter =  letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)