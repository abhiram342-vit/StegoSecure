# Image-Based Text Steganography

This project implements a simple text steganography technique using OpenCV, where a secret message is embedded into an image and can be retrieved using a passcode.

## Features
- Encrypts a secret message into an image by modifying pixel values.
- Uses a simple character-to-ASCII mapping for encoding and decoding.
- Requires a passcode for decryption.

## Prerequisites
Make sure you have Python installed along with the following dependencies:
```sh
pip install opencv-python
```

## How It Works
1. The script reads an image using OpenCV.
2. The user inputs a secret message and a passcode.
3. The message is encoded into the image by modifying pixel values.
4. The modified image is saved as `encryptedImage.jpg`.
5. To decrypt, the user provides the correct passcode.
6. The script extracts the message and prints it.

## Usage
Run the script and follow the prompts:
```sh
python script.py
```

## Code Explanation
- **Encoding**: Each character in the message is stored in pixel values.
- **Decoding**: The message is retrieved by mapping pixel values back to characters.
- **Security**: Requires a passcode to decrypt the message.

## Example
```sh
Enter secret message: Hello
Enter a passcode: 1234
Encrypted image saved as encryptedImage.jpg

Enter passcode for Decryption: 1234
Decryption message: Hello
```

## Notes
- Ensure the image path is correct before running the script.
- The method used is basic and does not provide strong security.
- Image modifications are minimal but detectable.

