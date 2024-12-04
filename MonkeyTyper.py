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
    time_per_combination = int(input("Enter the time per combination in seconds: "))

    print("")

    if min_length < 1 or max_length < 1:
        print("Invalid input. Minimum and maximum letter counts must be at least 1.")
        sys.exit(1)

    if min_length > max_length:
        print("Invalid input. Minimum letter count cannot be greater than maximum letter count.")
        sys.exit(1) 

    word_list = load_word_list(filename)
    overview = {}
    time_overview = {}
    total_attempts = {}

    for length in range(min_length, max_length + 1):
        start_time = time.time()  # Start time for this length
        end_time = start_time + time_per_combination
        attempts = 0
        found_words = set()
        word_times = []
        used_attempts = 0
        used_time = 0
        
        while time.time() < end_time:
            attempts += 1
            current_string = generate_random_string(length)
            sys.stdout.write("\r" + current_string)
            sys.stdout.flush()
            time.sleep(0.001)

            if current_string in word_list:
                found_time = time.time() - start_time
                attempts_word = attempts - used_attempts
                time_word = found_time - used_time
                word_times.append(time_word)  # Record the time taken to find this word
                found_words.add(current_string)
                print("\nFound a word: " + current_string + f" (Attempts: {attempts_word}, Time taken: {time_word} seconds)")
                print("")
                used_attempts += attempts_word
                used_time += time_word

        # Store the results for the current length
        overview[length] = len(found_words)
        time_overview[length] = word_times
        total_attempts[length] = attempts  # Store total attempts for this length
        # Change the text color to red for the "Time's up for ..." message
        print("")
        print("\033[31m\nTime's up for length {}: Found {} words.\033[0m".format(length, len(found_words)))
        print("\033[31m\nTotal attempts made: {}\033[0m".format(attempts))
        print("")

    # Print overview
    print(f"\nOverview of results in {time_per_combination} seconds:")
    for length in range(min_length, max_length + 1):
        if time_overview[length]:  # Check if there are any found words
            total_time = sum(time_overview[length])  # Total time taken for found words
            avg_time = total_time / len(time_overview[length])  # Calculate average time
            avg_attempts = total_attempts[length] / max(1, overview[length])  # Calculate average attempts, avoid division by zero
        else:
            avg_time = 0  # No words found, average time is 0
            avg_attempts = 0  # No words found, average attempts is 0

        # Ensure avg_attempts is not less than 1 if there are found words
        if overview[length] > 0:
            avg_attempts = max(1, avg_attempts)  # Ensure at least 1 attempt per found word

        print("Word Length {}: Found {} words. Average time to find: {:.6f} seconds. Average attempts per word: {:.2f}".format(length, overview[length], avg_time, avg_attempts))

main()
