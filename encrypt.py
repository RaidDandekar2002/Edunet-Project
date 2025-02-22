import cv2
import os

def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)
    
    d = {}
    for i in range(255):
        d[chr(i)] = i

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    encrypted_image_path = "encryptedImage.png"  # Save as .png
    cv2.imwrite(encrypted_image_path, img)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    print(f"Length of the secret message: {len(msg)}")  # Print message length for reference
    os.system(f"start {encrypted_image_path}")  # Open the image (Windows)

if __name__ == "__main__":
    image_path = "input.png"  # Replace with the correct image path
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypt_image(image_path, msg, password)