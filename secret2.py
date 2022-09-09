alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    r = input("Encrypt or Decrypt?(e/d)")
    if r == 'e':
        stringToEncrypt = input("please enter a message to encrypt: ")
        stringToEncrypt = stringToEncrypt.upper()
        shiftAmount = int(input("Please enter a whole number from 1-25 to be your key."))
        encryptedString = ""
        for currentCharacter in stringToEncrypt:
            position = alphabet.find(currentCharacter)
            newPosition = position + shiftAmount
            encryptedString = encryptedString + alphabet[newPosition]
        print("your encrypted message is", encryptedString) 

    elif r == 'd':
        stringToDecrypt = input("please enter a message to Decrypt: ")
        stringToDecrypt = stringToDecrypt.upper()
        shiftAmount = int(input("Please enter a whole number from 1-25 to be your key."))
        DecryptedString = ""
        for currentCharacter in stringToDecrypt:
            position = alphabet.find(currentCharacter)
            newPosition = position - shiftAmount
            DecryptedString = DecryptedString + alphabet[newPosition]
        print("your Decrypted message is", DecryptedString)    
