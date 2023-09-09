#This program detects the double spaces and replaces it with single space

st = "This is a string with double  spaces and we will replace  them"
doubleSpace = st.find("  ")
print(doubleSpace)

st = st.replace("  "," ")
print(st)