# Generate Password

A simple, secure, and customizable password generator.

## Features

- Generates passwords using `secrets` for cryptographic security.
- Customizable via command-line arguments:
  - Password length
  - Include or exclude uppercase letters, digits, and special characters.

## Usage

Clone the repo:
```bash
git clone https://github.com/christianfrey/generate-password.git
cd generate-password
````

Run the script:

```bash
python generate_password.py
```

Optional flags:

```bash
# Default generates a 12-character password with all character types
python generate_password.py

# Customize length (e.g., 16 characters)
python generate_password.py -l 16

# Exclude uppercase letters
python generate_password.py -U

# Exclude digits
python generate_password.py -D

# Exclude special characters
python generate_password.py -S
```

## Example output

```
🔐 Generated password: e.5YeQ_*gcgA
```

## Requirements

* Python 3.6 or newer
