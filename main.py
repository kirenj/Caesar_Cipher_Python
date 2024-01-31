from replit import clear
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def casear(plain_text, shift_amount, direction_used):  
  crypto_word = ""  
  for i in plain_text:
    if i not in alphabet:
      crypto_word += i
    else:
      index = int(alphabet.index(i))
      if direction_used == "encode":      
        new_index = index + shift_amount
        crypto_word += alphabet[new_index]    
      elif direction_used == "decode":
        new_index = index - shift_amount
        crypto_word += alphabet[new_index]
      else:
        print("Wrong input. Try again.")
        #repeat_loop = False
        exit()
  print(f"The {direction_used}d text is {crypto_word}")


repeat_loop = True

while repeat_loop == True:
  
  clear()
  print(logo)
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  casear(plain_text = text, shift_amount = shift, direction_used = direction)
  
  repeat = input("Do you want to restart the cipher program? 'Y' for Yes and 'N' for No: ").lower()
  
  if repeat == 'y':
    repeat_loop = True
  elif repeat == 'n':
    print("Goodbye!")
    repeat_loop = False
  else:
    print("Unknown Entry")
    repeat_loop = False