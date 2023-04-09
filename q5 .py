string = "Hello, World!"  # string a ser invertida
inverted_string = ""

for i in range(len(string)-1, -1, -1):
    inverted_string += string[i]

print(inverted_string)
