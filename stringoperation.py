# Multiline text using triple quotes (single)
text1 = '''This is a multiline text.
It spans across multiple lines.
Each line is preserved as is.'''

print(text1)


print(f"Length of text1: {len(text1)} characters")

print(f"line occurence in text1: {text1.count('line')}")

text1 = text1.replace("multiline", "multi-line")
print("Updated text1:")
print(text1)

words = text1.split()

for word in words:
    print(word)