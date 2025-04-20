str = "Data science is cool"
print("Data" in str) # str can be replace by Data science is cool
print(str.find("Data"))

print(str[5:13]) #science

# write a function to find a substring form the string
def contains_substring(mainstring , substring):
    return substring in mainstring
print(contains_substring("python is fun" , "python"))
print(contains_substring("python is not fun" , "javascript"))

# all possible substrings form a string and counting the sumber of substring
s = "Srijita"
count = 0
for i in range(len(s)):
    for j in range(i+1 , len(s)+1):
        print(s[i:j])
        count += 1
print("The number of substrings are : " ,count)