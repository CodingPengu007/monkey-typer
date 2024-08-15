import random
import string
import time
import sys

def load_word_list(filename):
    with open(filename, 'r') as f:
        return set(f.read().splitlines())

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def main():
    while True:
        language = input("Do you want to search for English, German, or Both words? (E/G/B): ")
        if language.upper() == 'E':
            filename = 'words(english).txt'
            break
        elif language.upper() == 'G':
            filename = 'words(german).txt'
            break
        elif language.upper() == 'B':
            filename = 'words(english, german).txt'
            break
        else:
            print("Invalid input. Please enter E for English, G for German, or B for Both.")
            continue

    min_length = int(input("Enter the minimum letter count: "))
    max_length = int(input("Enter the maximum letter count: "))

    if min_length < 1 or max_length < 1:
        print("Invalid input. Minimum and maximum letter counts must be at least 1.")
        sys.exit(1)

    if min_length > max_length:
        print("Invalid input. Minimum letter count cannot be greater than maximum letter count.")
        sys.exit(1)

    delay = float(input("Enter the delay between found words (in seconds): "))

    word_list = load_word_list(filename)
    attempts = 0
    for length in range(min_length, max_length + 1):
        while True:
            attempts += 1
            current_string = generate_random_string(length)
            sys.stdout.write("\r" + current_string)
            sys.stdout.flush()
            time.sleep(0.001)
            if current_string in word_list:
                print("\nFound a word: " + current_string)
                print("Attempts: " + str(attempts))
                attempts = 0
                time.sleep(delay)
                print("")
        sys.stdout.write("\r")
        sys.stdout.flush()

if __name__ == "__main__":
    main()