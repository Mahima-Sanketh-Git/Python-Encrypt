# Python Encrypt

A simple Python-based text encryption and decryption utility using a custom substitution cipher. This project demonstrates how to apply basic encryption concepts to protect text messages using character mapping.

## Features

- **Encrypt text files** — converts plain text into an encoded format using a substitution cipher
- **Decrypt encoded files** — reverses the encryption to recover the original text
- **File-based workflow** — reads input from text files and writes output to new files
- **Lightweight** — no external dependencies; uses Python's built-in capabilities only

## Tech Stack

- **Language:** Python 3

## Supported Algorithms

### Substitution Cipher

The project uses a custom alphanumeric substitution cipher that maps each lowercase letter and space to a unique character:

| Plain | Cipher | Plain | Cipher |
|-------|--------|-------|--------|
| a     | 1      | n     | e      |
| b     | 2      | o     | f      |
| c     | 3      | p     | g      |
| d     | 4      | q     | h      |
| e     | 5      | r     | i      |
| f     | 6      | s     | j      |
| g     | 7      | t     | k      |
| h     | 8      | u     | l      |
| i     | 9      | v     | m      |
| j     | a      | w     | n      |
| k     | b      | x     | o      |
| l     | c      | y     | p      |
| m     | d      | z     | q      |
| (space) | r   |       |        |

**Example:** `simple notion` → `j9dgc5refk9fe`

## Project Structure

```
Python-Encrypt/
├── enc.py          # Encryption script
├── dec.py          # Decryption script
├── message.txt     # Source file containing the plain text to encrypt
├── my.txt          # Example encrypted output file
├── show1.txt       # Example decrypted output file
└── README.md       # Project documentation
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mahima-Sanketh-Git/Python-Encrypt.git
   cd Python-Encrypt
   ```

2. **Ensure Python 3 is installed:**
   ```bash
   python --version
   ```
   No additional packages are required.

## Usage

### Encrypt a Message

1. Write your plain text message (lowercase letters and spaces only) into `message.txt`.
2. Run the encryption script:
   ```bash
   python enc.py
   ```
3. When prompted, enter a name for the output encrypted file (without `.txt`):
   ```
   Enter a Name for encrypt file : secret
   ```
   The encrypted text will be saved to `secret.txt`.

### Decrypt a Message

1. Run the decryption script:
   ```bash
   python dec.py
   ```
2. Enter the name of the encrypted file you want to decrypt:
   ```
   Enter Name of encrypt file : secret
   ```
3. Enter a name for the output decrypted file:
   ```
   Enter A Name for decrypt file : recovered
   ```
   The decrypted text will be saved to `recovered.txt`.

### Example

**Input (`message.txt`):**
```
simple notion
```

**After running `enc.py` → `my.txt`:**
```
j9dgc5refk9fe
```

**After running `dec.py` → `show1.txt`:**
```
simple notion
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please make sure your code follows the existing style and is well-documented.

## License

This project is open source and available under the [MIT License](LICENSE).
