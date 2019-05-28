vowels = "aeiou"
char = input("Type a character")

if char.lower() in vowels:    
    print("Vowel")
elif ord(char.lower()) in range(97,138):    
    print("Consoant")    
elif ord(char) in range(48, 57):    
    print("number")
else:
    print("special character")
    
    
