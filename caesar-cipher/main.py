import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print (art.logo)
length=len(alphabet) - 1
user = "Y"

def caesar(text,shift,direction): 
    x=[i for i in text]
    cipher_text=""
    shift %= 26
    for j in x:
        if j == " ":
            cipher_text+= j
        elif j not in alphabet:
            cipher_text += j
        if direction == "encode":
            if alphabet.index(j) <= (length-shift): 
                cipher_text += alphabet[alphabet.index(j)+shift]
            elif alphabet.index(j) > (length-shift): 
                cipher_text += alphabet[(alphabet.index(j)+shift)-26]
        elif direction == "decode":
            if alphabet.index(j) >= shift:
                cipher_text += alphabet[alphabet.index(j)-shift]
            elif alphabet.index(j) < shift:
                cipher_text += alphabet[(alphabet.index(j)-shift)]
    print(f"The {direction}d text is {cipher_text}.")

while user == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    user=input("Would you like to encode/decode a message again (Y/N): ")
