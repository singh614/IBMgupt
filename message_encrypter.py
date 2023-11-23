import cv2
import os

def encrypt_message(img, msg):
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("Encryptedmsg.jpg", img)

def decrypt_message(img, password):
    c = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0

    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        for i in range(len(msg)):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decrypted Message: ", message)
    else:
        print("Not a valid key")

if __name__ == "__main__":
    img = cv2.imread(input("Enter the name of the file (with extension): "))
    msg = input("Enter Secret Message: ")
    password = input("Enter Password: ")

    encrypt_message(img, msg)

    # Display the Encrypted Image in a new window
    os.system("open Encryptedmsg.jpg")  # for mac

    decrypt_message(img, password)
