text = """
Python is a widely used high-level programming language created by Guido van Rossum in 1991.
Its simple syntax makes it easy to read and write. Python supports multiple programming paradigms, 
including procedural, object-oriented, and functional programming. It is popular in data science, web development, 
automation, and artificial intelligence.
"""
print(text.count("Python"))

print(text.strip().startswith("Python"))

print(text.upper())

# extract the name of creator from the passage
start = text.find("is popular") + len("is popular")# to reach to the particular index 
end = text.find(" and artificial intelligence")
created = text[start:end]
print(created.strip())

sentence = text.strip().split(".")
for sentence in sentence:
    print(sentence.strip())

words = text.split()
long_words = [word.strip(".,") for word in words if len(word.strip(".,").strip()) > 8]
print(long_words)

word = text.split()
cleared_words =[word.strip(",.")for word in words]
unique_word = set(cleared_words)
print(unique_word)