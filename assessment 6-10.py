# 7.Case Sensitive Replacement
text = input("enter a string: ")
old = input("enter word to replace: ")
new = input("enter new word: ")

words = text.split()
result = ""

for word in words:
    if word.lower() == old.lower():
        result = result + new + " "
    else:
        result = result + word + " "

print(result)


# 8.Splits String
text = input("enter a string: ")

words = []
word = ""

for ch in text:
    if 'A' <= ch <= 'Z' and word != "":
        words.append(word)
        word = ""

    word = word = ch

words.append(word)

print(words)

# 9.Removes non-Alphanumeric

text = input("enter a string: ")

result =""
for ch in text:
    if 'A' <= ch <= 'Z':
        result = result + ch
    elif 'a' <= ch <= 'z':
        result = result + ch
    elif '0' <= ch <= '9':
        result = result + ch

print(result)

# 10. Removes all Whitespace

text = input("enter a string: ")

result = text.replace(" ","")

print(result)
        
