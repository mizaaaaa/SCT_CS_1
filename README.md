# Caesar Cipher Tool

This repository provides a simple interactive Caesar Cipher tool implemented in Python. The Caesar Cipher is a classic encryption technique that shifts each letter in a message by a fixed number of positions in the alphabet.

## Features

- **Encrypt or Decrypt messages** using the Caesar Cipher.
- **Handles both uppercase and lowercase letters.**
- **Preserves spaces, punctuation, and numbers** in the message.
- **Input validation** for shift values and operation mode.
- Repeats the process until the user chooses to exit.

## Usage

1. **Clone the repository or copy the `task1.py` file.**

2. **Run the script:**
   ```bash
   python task1.py
   ```

3. **Follow the prompts:**
   - Enter your message.
   - Enter the shift value (an integer, e.g., 3).
   - Select whether to Encrypt (`E`) or Decrypt (`D`).
   - View the result.
   - Choose whether to try again or exit.

## Example

```
🔐 === CAESAR CIPHER TOOL === 🔐

💬 Enter your message: Hello, World!
 Enter the shift value (e.g., 3): 3
 Choose mode - Encrypt[E] or Decrypt[D]: E

✅ Result (Encrypted): Khoor, Zruog!

 Try again? (Yes/No): n
 Exiting Caesar Cipher Tool. Goodbye!
```

## How It Works

- **Encryption** shifts each letter forward by the specified value.
- **Decryption** shifts each letter backward by the specified value.
- Non-alphabetic characters are not changed.

## License

This project is licensed under the MIT License.

---

*Created by [mizaaaaa](https://github.com/mizaaaaa)*
