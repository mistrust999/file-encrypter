# file-encrypter
Small python based file encryption script that garuntees only the intended reciever with the key you made/generated can have your private files

## ChatGPT Write-up
This is a simple Python GUI application for encrypting and decrypting files using AES-256 encryption. The application uses the `tkinter` library for the GUI and the `cryptography` library for encryption and decryption. The encryption key is automatically copied to the clipboard when generated.

## Features

- Generate a new AES-256 encryption key
- Encrypt files using the generated or provided key
- Decrypt files using the provided key
- Copy the encryption key to the clipboard

## Requirements

- Python 3.x
- `cryptography` library
- `pyperclip` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

    ```bash
    pip install cryptography pyperclip
    ```

## Usage

1. Run the script:

    ```bash
    python encfile.py
    ```

2. The application window will appear.

3. To generate a new encryption key:
   - Click the "Generate Key" button.
   - The generated key will be displayed in the entry field and copied to the clipboard.

4. To encrypt a file:
   - Enter the encryption key in the entry field (or use the generated key).
   - Click the "Encrypt File" button and select the file to encrypt.
   - The encrypted file will be saved with the extension `.encrypted`.

5. To decrypt a file:
   - Enter the encryption key in the entry field.
   - Click the "Decrypt File" button and select the file to decrypt.
   - The decrypted file will be saved with the original file extension.

## Notes

- Keep the encryption key safe. You will need it to decrypt the files.
- The encryption key is automatically copied to the clipboard when generated.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
