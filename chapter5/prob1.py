dict = {
    "varkare" :"Good Luck",
    "trath":"Thunder",
    "maze" :"Fun",
    "tasruf":"ghost"


    }
print("options available inside the dicionary :\n", dict.keys())
a = input("Enter the kashmiri word\n")
print('The meaning of your word "',a,'" is: ',dict.get(a))
