import cv2

def decrypt_image(encrypted_image_path, password, original_msg_length):
    img = cv2.imread(encrypted_image_path)
    
    c = {}
    for i in range(255):
        c[i] = chr(i)

    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(original_msg_length):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT auth")

if __name__ == "__main__":
    encrypted_image_path = "encryptedImage.png"  # Use .png
    password = input("Enter the passcode used for encryption: ")
    
    # Input validation for original_msg_length
    while True:
        try:
            original_msg_length = int(input("Enter the length of the original message: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer for the message length.")

    decrypt_image(encrypted_image_path, password, original_msg_length)