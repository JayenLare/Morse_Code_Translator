# Python program to translates messages to Morse Code and vice versa --- Jayen Lare

# Dictionary containing characters and their corresponding morse code representation 
morseCodeDict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
                  'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                  'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                  'M':'--', 'N':'-.','O':'---', 'P':'.--.', 
                  'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                  'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                  'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', 
                  '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                  '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                  ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
                  '-':'-....-', '(':'-.--.', ')':'-.--.-' }

# Translates a message to Morse code
def messageToMorse(message):
  morseCode = ''
  message = message.upper()
  # Loops through each character in the message 
  for character in message:
    # checks for character and adds corresponding code, otherwise adds a space
    if character != ' ':
      morseCode += morseCodeDict[character] + ' '
    else:
      morseCode += ' '  
  return morseCode

# Translate Morse code to a message
def morseToMessage(code):
  message = ''
  morseCharacter = ''
  code = code.upper()
  code += ' '
  i = 0
  # Loops through each character in the code 
  for character in code:
    # checks for space 
    if character == ' ':
      i += 1
    else:
      i = 0
      morseCharacter += character
      # End of a word, adds space to messsage; otherwise adds letter to meassage
      if i == 2:
        message += ' '
      else:
        message += list(morseCodeDict.keys())[list(morseCodeDict.values()).index(morseCharacter)] 
        morseCharacter = ''
  return message

# Main function
def main():
  # User decides which way they want to translate
  print("Morse Code Translator")
  print("----------------------")
  print("Do you want to translate a message to Morse code or Morse code to a meassage?")
  flag = True
  # User enters 1 or 2, otherwise invalid and loops until choice is valid
  while flag == True:
    print("1: Message to Morse code")
    print("2: Morse code to Message")
    direction = input("Enter the number of your choice: ")
    # Message is received from user, and translates to Morse Code by calling messageToMorse function 
    if direction == '1':
      message = input("Enter a message you would like to translate to Morse code: \n")
      print("'" + message + "'" + " in Morse code is: ")
      print(messageToMorse(message))
      flag = False
    # Morse code is received from user, and translates to a message by calling morseToMessage function 
    elif direction == '2':
      code = input("Enter Morse code to be translated to a message: \n")
      print("'" + code + "'" + " translates to: ")
      print(morseToMessage(code))
      flag = False
    else:
      print("Invalid choice... Please enter either '1' or '2'")
      print("")

# Runs main function
if __name__ == "__main__":
  main()
