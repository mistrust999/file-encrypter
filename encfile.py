from tkinter import filedialog, messagebox, Tk, Button, Label, Entry
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import secrets
import pyperclip

class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor/Decryptor")
        self.key = None

        self.label = Label(root, text="Enter encryption key (leave empty to generate new key):")
        self.label.pack()

        self.key_entry = Entry(root, width=50)
        self.key_entry.pack()

        self.generate_key_button = Button(root, text="Generate Key", command=self.generate_key)
        self.generate_key_button.pack()

        self.encrypt_button = Button(root, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack()

        self.decrypt_button = Button(root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack()

    def generate_key(self):
        self.key = secrets.token_bytes(32)
        encoded_key = urlsafe_b64encode(self.key).decode()
        self.key_entry.delete(0, 'end')
        self.key_entry.insert(0, encoded_key)
        pyperclip.copy(encoded_key)
        messagebox.showinfo("Key Generated", "A new encryption key has been generated, copied to clipboard, and inserted in the field.")

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            key = self.key_entry.get().encode()
            if not key:
                messagebox.showerror("Error", "No encryption key provided!")
                return
            try:
                key = urlsafe_b64decode(key)
                iv = secrets.token_bytes(16)
                cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                encryptor = cipher.encryptor()
                padder = padding.PKCS7(algorithms.AES.block_size).padder()
                with open(file_path, 'rb') as file:
                    original = file.read()
                padded_data = padder.update(original) + padder.finalize()
                encrypted = encryptor.update(padded_data) + encryptor.finalize()
                with open(file_path + '.encrypted', 'wb') as encrypted_file:
                    encrypted_file.write(iv + encrypted)
                messagebox.showinfo("Success", f"File encrypted successfully: {file_path}.encrypted")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            key = self.key_entry.get().encode()
            if not key:
                messagebox.showerror("Error", "No decryption key provided!")
                return
            try:
                key = urlsafe_b64decode(key)
                with open(file_path, 'rb') as encrypted_file:
                    iv = encrypted_file.read(16)
                    encrypted = encrypted_file.read()
                cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                decryptor = cipher.decryptor()
                padded_data = decryptor.update(encrypted) + decryptor.finalize()
                unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
                original = unpadder.update(padded_data) + unpadder.finalize()
                original_file_path = os.path.splitext(file_path)[0]
                with open(original_file_path, 'wb') as decrypted_file:
                    decrypted_file.write(original)
                messagebox.showinfo("Success", f"File decrypted successfully: {original_file_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    app = FileEncryptorApp(root)
    root.mainloop()
