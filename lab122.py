# pylint: disable=invalid-name

class Caesar_Cipher():
    """ encryted message to numbers"""
    
    def __init__(self) -> None:
        pass
       
    def getDoubleAlphabet(self, alphabet: str) -> str:
        doubleAlphabet = alphabet + alphabet
        return doubleAlphabet

    def getMessage(self):
        stringToEncrypt = input("Please enter a message to encrypt: ")
        return stringToEncrypt

    def getCipherKey(self):
        shiftAmount = input( "Please enter a key (whole number from 1-25): ")
        return shiftAmount
    
    def encryptMessage(self, message, cipherKey, alphabet):
        encryptedMessage = ""
        uppercaseMessage = ""
        uppercaseMessage = message.upper()
        for currentCharacter in uppercaseMessage:
            position = alphabet.find(currentCharacter)
            newPosition = position + int(cipherKey)
            if currentCharacter in alphabet:
                encryptedMessage = encryptedMessage + alphabet[newPosition]
            else:
                encryptedMessage = encryptedMessage + currentCharacter
        return encryptedMessage
    
    def decryptMessage(self, message, cipherKey, alphabet):
        decryptKey = -1 * int(cipherKey)
        return self.encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    encryted = Caesar_Cipher()
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = encryted.getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = encryted.getMessage()
    print(myMessage)
    myCipherKey = encryted.getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryted.encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = encryted.decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()
