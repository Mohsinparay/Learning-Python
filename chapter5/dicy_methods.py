mydict = {
    "fast": "in a quick manner",
    "mohsin": "a coder",
    "marks": [1,3,5,6],
    "anotherdict":{'this':'player'},
    1:2
}
# print(mydict.keys()) #prints the keys of the dictiopnary
# print(mydict.values()) #prints the values of dictionary
# print(mydict.items()) prints the keys , values for all the contents of the dictionay

updatedict = {
    "animals" : "Forests",

    "mohsin" : "blckhat"
}
# mydict.update(updatedict) #updates the dictionary by adding key values or adding values and keys to the dict

# mydict.update(updatedict)


print(mydict.get("mohsin")) # as if any key isn't present in the dictionary it prevents the thrown of error it returns the none


print(mydict)


