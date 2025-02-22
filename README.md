# Edunet-Project

# Steganography Project

## Overview
This project implements image steganography using Python and OpenCV. It allows users to hide a secret message within an image and later retrieve it using a passcode.

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Files
- `encrypt.py` - Script for encoding a secret message into an image.
- `decrypt.py` - Script for retrieving the hidden message from an encrypted image.
- `input.png` - Original image to be used for encryption.
- `encryptedImage.png` - Output image containing the hidden message.

## Steps to Run

### Encryption
1. Run the `encrypt.py` script.
2. Enter the secret message when prompted.
3. Enter a passcode to secure the message.
4. The encrypted image will be saved as `encryptedImage.png`.
5. Note the length of your secret message, as it is required for decryption.

Example:
```
$ python encrypt.py
Enter secret message: hello
Enter a passcode: mypassword
Image encrypted and saved as encryptedImage.png
Length of the secret message: 5
```

### Decryption
1. Run the `decrypt.py` script.
2. Enter the passcode used for encryption.
3. Provide the length of the original message.
4. Re-enter the passcode for verification.
5. The decrypted message will be displayed.

Example:
```
$ python decrypt.py
Enter the passcode used for encryption: mypassword
Enter the length of the original message: 5
Enter passcode for Decryption: mypassword
Decrypted message: hello
```

## Future Scope
- Enhancing security by applying AES encryption before embedding.
- Supporting more file formats beyond PNG.

## Author
Raid Dandekar

