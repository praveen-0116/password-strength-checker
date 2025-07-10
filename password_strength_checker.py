import re
import string
import math

def calculate_entropy(password):
  pool = 0
  if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    entropy = len(password) * math.log2(pool) if pool > 0 else 0
    return entropy

def classify_entropy(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 35:
        return "Weak"
    elif entropy < 59:
        return "Reasonable"
    elif entropy < 127:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    entropy = calculate_entropy(password)
    strength = classify_entropy(entropy)

    print(f"Password Entropy: {entropy:.2f} bits")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
