import string

# Lowercase alphabet
alphabet = list(string.ascii_lowercase)

#print(art.logo)

def caesar(original_text,shift_amount,path):
    cipher_text = ""
    if path == "decode":
                shift_amount *= -1
        
    for i in original_text:
        
        if i not in alphabet:
            cipher_text += i
        else:    
            shifted_position = alphabet.index(i) + shift_amount
            shifted_position %= len(alphabet) 
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {path}d result: {cipher_text}")
    

should_continue = True

while should_continue:
    direction = input("Encode or Decode?").lower()
    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))

    caesar(original_text = text, shift_amount = shift, path = direction)

    restart = input("Type yes for continue again, otherwise type no").lower()

    if restart == "no":
        should_continue = False
        print("GoodBye")
