import hashlib
import itertools
import time
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Generates a random password of the specified length using ASCII characters."""
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_and_compare(attempt, correct_hash):
    """Hashes the attempt and compares it to the correct hash.

    Args:
        attempt (str): The password attempt to hash.
        correct_hash (str): The SHA-256 hash of the correct password.

    Returns:
        bool: True if the attempt's hash matches the correct hash, False otherwise.
    """
    attempt_hash = hashlib.sha256(attempt.encode('ascii')).hexdigest()
    return attempt_hash == correct_hash

def brute_force_sha256(correct_hash, password_length):
    """Attempts to crack the SHA-256 hash of a password using a brute-force approach,
    given the length of the original password.
    """
    start_time = time.time()
    attempt_count = 0

    for attempt_list in itertools.product(characters, repeat=password_length):
        attempt = ''.join(attempt_list)
        attempt_count += 1
        if hash_and_compare(attempt, correct_hash):
            end_time = time.time()
            duration = end_time - start_time
            return attempt, attempt_count, duration
    return None, attempt_count, time.time() - start_time # Return None if not found

if __name__ == "__main__":
    password_length = 4
    generated_password = generate_password(password_length)
    hashed_password = hashlib.sha256(generated_password.encode('ascii')).hexdigest()
    print(f"Generated Password: {generated_password}")
    print(f"SHA-256 Hash: {hashed_password}")

    print("Starting brute-force attack on the SHA-256 hash...")
    total_possible_passwords = len(characters)**password_length
    print(f"Going through {len(characters)}^{password_length} = {total_possible_passwords} possible options")
    
    cracked_password, attempts, duration = brute_force_sha256(hashed_password, password_length) # Pass the length

    if cracked_password:
        print("Password cracked!")
        print(f"Cracked Password: {cracked_password}")
        print(f"Number of attempts: {attempts}")
        print(f"Time taken: {duration:.4f} seconds")
    else:
        print("Password not found within the search space.")
        print(f"Number of attempts: {attempts}")
        print(f"Time taken: {duration:.4f} seconds")
