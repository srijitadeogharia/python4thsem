#lists in python are array same just in other languages
#stores orderd collection of data 

a=[]
length=len(a)
print(length)


b=['a','b','c',"probably","eight","ten",6,8,38]
#accessing elemets form the list
print("Acessing elemts from the list")
print(b[3])
print(b[5])
#acessing elemts from list by giving -ve input 
print(b[-2])
print(b[-5])
#counting how many no. of elements in b and what are they
length_b=len(b)
print(length)
print(b)


c=[4,6,8,9,10,8,7,6,8,3,2]
#how many times 8 existing in c 
count_of_8=c.count(8)
print(c)

#what is the type of a b and c
print(type(c))
print(type(b))
print(type(a))