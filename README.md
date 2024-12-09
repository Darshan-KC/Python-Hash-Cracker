
# Python Hash Cracker

This project is a Python-based hash cracker that uses a dictionary attack to reverse hashed passwords. It is designed to demonstrate how file handling, hashing, and brute force techniques can be implemented in Python. The tool supports common hashing algorithms like MD5, SHA-1, SHA-256, and others.

---

## Features

- Supports **MD5**, **SHA-1**, and **SHA-256** hashing algorithms.
- Uses a dictionary file containing potential passwords.
- Simple command-line interface.
- Easy to customize and extend for other hashing algorithms.

---

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.6 or higher
- A dictionary file (e.g., `passwords.txt`) containing potential password guesses.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Darshan-KC/Python-Hash-Cracker.git
   cd Python-Hash-Cracker
   ```

2. Prepare a dictionary file (e.g., `passwords.txt`) with potential passwords, one per line.

3. Run the hash cracker script:
   ```bash
   python hash_cracker.py
   ```

4. Follow the prompts to:
   - Input the hash to crack.
   - Select the hashing algorithm.
   - Provide the path to your dictionary file.

5. The script will attempt to match the hash with a password in the dictionary and display the result.

---

## Example

Input:
```text
Enter the hash: 5f4dcc3b5aa765d61d8327deb882cf99
Select hashing algorithm (MD5/SHA1/SHA256): MD5
Enter the path to the dictionary file: passwords.txt
```

Output:
```text
Hash cracked successfully!
Password: password
```

---

## Customization

- To add support for additional hashing algorithms, modify the hashing logic in the script.
- Adjust the dictionary file to include stronger or more varied password guesses.

---

## Limitations

- The effectiveness of the cracker depends on the quality and comprehensiveness of the dictionary file.
- Not designed for high-speed or distributed cracking.

---

## Disclaimer

This project is for **educational purposes only**. Do not use it for unauthorized or illegal activities. The author is not responsible for misuse of this tool.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the tool.

---

## Contact

For questions or suggestions, please reach out via [GitHub Issues](https://github.com/Darshan-KC/Python-Hash-Cracker/issues).
