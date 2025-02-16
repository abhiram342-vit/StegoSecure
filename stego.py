import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select an image
def select_image():
    global img, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        img = cv2.imread(img_path)
        messagebox.showinfo("Success", "Image Loaded Successfully")

# Function to encrypt the message into the image
def encrypt_message():
    global img
    if img is None:
        messagebox.showerror("Error", "Please select an image first")
        return
    
    msg = entry_msg.get()
    password = entry_pass.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Message and Password cannot be empty")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")  # Open image on Windows
    messagebox.showinfo("Success", "Message Encrypted and Image Saved")

# Function to decrypt the message from the image
def decrypt_message():
    global img
    if img is None:
        messagebox.showerror("Error", "Please select an image first")
        return
    
    pas = entry_decrypt_pass.get()
    original_pass = entry_pass.get()
    
    if pas != original_pass:
        messagebox.showerror("Error", "Incorrect Password")
        return
    
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    for i in range(len(entry_msg.get())):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    messagebox.showinfo("Decryption Result", f"Decrypted Message: {message}")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x400")

btn_select = tk.Button(root, text="Select Image", command=select_image)
btn_select.pack(pady=10)

lbl_msg = tk.Label(root, text="Enter Secret Message:")
lbl_msg.pack()
entry_msg = tk.Entry(root, width=30)
entry_msg.pack()

lbl_pass = tk.Label(root, text="Enter Passcode:")
lbl_pass.pack()
entry_pass = tk.Entry(root, width=30, show="*")
entry_pass.pack()

btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
btn_encrypt.pack(pady=10)

lbl_decrypt_pass = tk.Label(root, text="Enter Passcode for Decryption:")
lbl_decrypt_pass.pack()
entry_decrypt_pass = tk.Entry(root, width=30, show="*")
entry_decrypt_pass.pack()

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
btn_decrypt.pack(pady=10)

root.mainloop()
