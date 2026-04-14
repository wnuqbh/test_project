from checker import check_strength, get_strength_label

def main():
    password = input("Enter your password: ")

    score = check_strength(password)
    strength = get_strength_label(score)

    print(f"\nScore: {score}/5")
    print(f"Strength: {strength}")

if __name__ == "__main__":
    main()