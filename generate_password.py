import secrets
import string
import argparse

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@.-_*?/"

    if length <= 0:
        raise ValueError("Length must be a positive integer.")

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(
        description="Customizable password generator"
    )
    parser.add_argument(
        "-l", "--length", type=int, default=12,
        help="Password length (default: 12)"
    )
    parser.add_argument(
        "-U", "--no-upper", action="store_false", dest="use_upper",
        help="Exclude uppercase letters"
    )
    parser.add_argument(
        "-D", "--no-digits", action="store_false", dest="use_digits",
        help="Exclude digits"
    )
    parser.add_argument(
        "-S", "--no-special", action="store_false", dest="use_special",
        help="Exclude special characters"
    )

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_upper=args.use_upper,
            use_digits=args.use_digits,
            use_special=args.use_special
        )
        print("🔐 Generated password:", pwd)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
