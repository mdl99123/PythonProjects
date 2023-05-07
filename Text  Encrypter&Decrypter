from cryptography.fernet import Fernet
import base64
import pyperclip


option="-1"
while option!="3":
    print("Main Menu")
    print("1.- Encrypt Text")
    print("2.- Decrypt Text")
    print("3.- Exit")
    option=input()
    if option=="1":
        key = Fernet.generate_key()
        f = Fernet(key)
        print("Please enter text to encrypt: ")
        TextToEncrypt=input()
        TextToEncrypt=f.encrypt(TextToEncrypt.encode('utf-8'))
        print("To display the key used to encrypt the text press any key.\nStore it in a secure location as you will need to decrypt the text")
        input()
        print(key.decode())
        pyperclip.copy(key.decode())
        print()
        print("The key has been copied to clipboard, paste it in a secure location")
        print()
        print("To display the encrypted text press the enter key")
        input()
        print(TextToEncrypt.decode())
        pyperclip.copy(TextToEncrypt.decode())
        print()
        print("The encrypted text has been copied to clipboard, paste it in a secure location")
        print()
    if option=="2":
        try:
            print("Please enter text to decrypt: ")
            TextToDecrypt=input()
            print("Please enter the encryption key to decrypt the text: ")
            key=input().encode('utf-8')
            f= Fernet(key)
            DecryptedText=f.decrypt(TextToDecrypt.encode('utf-8'))
            print("Press the enter key to view decrypted text: ")
            input()
            print(DecryptedText.decode())
            print()
        except BaseException:
            print()
            print("Check Input")
            print()
