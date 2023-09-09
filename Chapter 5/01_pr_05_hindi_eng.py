myDict = {
    "Pankha" : "Fan",
     "Hawa" : "Air",
     "Kutta" : "Dog"
}


print("Please select the hindi word from these: \n", myDict.keys())

word = input("Please enter the word: \n")
print("The neglish meaning of word is: ", myDict.get(word))