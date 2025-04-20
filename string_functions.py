# endswith("string to be checked")
str1 = "I'm studying python for my exams"
print(str1.endswith("ams"))# true
print(str1.endswith("aoo"))# false

# capitalize() -> make the 1st letter of the string capital 
# this function temporarily capitalize the 1st letter
str2 = "i love music"
print(str2.capitalize())
#for permanent capilatization of 1st letter
str2 = str2.capitalize()
print(str2)

# upper() -> to convert a whole string to uppercase
# isupper() ->provide true or false value for the particular case
text = "hello i'am srijita"
text_convert = text.upper()
print(text_convert)

# lower() -> converts the capitalized text into lowercase
# is lower() -> provide true or false value for the particular value
text1 = "HELLO MY NAME IS SRIJITA"
text_convert = text.lower()
print(text_convert)

# title() -> capitalize the first character of each letter
text2 = "i have a big house in which i love living"
print(text2.title())

# replace() -> replaces all the old values with the new ones we can also replace a whole word whith this function 
txt = "I'm ordering book of python for exams"
txt_conv = txt.replace("o" , "b")
print(txt_conv)

# find() -> finds a particular word in parameter and returns exactly the 1st index of 1st occurance for that word
txt1 = "I'm ordering book of python for exams"
txt_conv1 = txt1.find("o")
print(txt_conv1)
txt_conv2 = txt1.find("book")
print(txt_conv2)

# count() -> counts the occurance of a particular word or character , returns the np. of occurance
txt2 = "This is practice of python programing for exams which is benifitial is also is is is"
conv = txt2.count("i")
print("The occurance of i is = ", conv)
conv1 = txt2.count("is")
print("The occurance of is in my txt2 is = " , conv1)




#startswith() -> checks if the string starts with this particular paramenter
s = "I'm studying python for my exams"
check = s.startswith("exams")
check2 = s.startswith("I'm")
print(check)
print(check2)

# strip() -> removes all the whitespace or char from both ends
# lstrip() -> removes form left
# rstrip() -> removes form right
s = " hello "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# split() -> breaks a string into list of words based on a seperator
s = "apple, mango, pear, banana , garpes"
print(s.split(" "))

# join() -> Joins a list of strings into one string, using a separator.
s = 'hello' 'world!'
print("".join(s))

# swapcase -> swaps the case upper to lower and vice versa
text3 = "pYegOggibFYHvRYJvRUnFrumnliyRFNKITFhkoutfbJUYFhJuTfbj"
print(text3.swapcase())

