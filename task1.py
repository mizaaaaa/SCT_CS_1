def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = shift if mode == 'E' else -shift
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Keep punctuation, numbers, and spaces as is

    return result

def get_valid_shift():
    while True:
        try:
            return int(input(" Enter the shift value (e.g., 3): "))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_valid_mode():
    while True:
        mode = input(" Choose mode - Encrypt[E] or Decrypt[D]: ").strip().upper()
        if mode in ['E', 'D']:
            return mode
        print("❌ Invalid choice. Please enter 'E' or 'D'.")

def main():
    print("🔐 === CAESAR CIPHER TOOL === 🔐")
    while True:
        message = input("\n💬 Enter your message: ")
        shift = get_valid_shift()
        mode = get_valid_mode()

        result = caesar_cipher(message, shift, mode)
        action = "Encrypted" if mode == 'E' else "Decrypted"
        print(f"\n✅ Result ({action}): {result}")

        again = input("\n Try again? (Yes/No): ").strip().upper()
        if again not in ['Y', 'YES']:
            print(" Exiting Caesar Cipher Tool. Goodbye!")
            break

if __name__ == "__main__":
    main()
