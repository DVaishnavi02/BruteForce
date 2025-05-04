import random
import string
import time
from itertools import product

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Generates a random password of the specified length using ASCII characters."""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def brute_force(correct_password):
    """Attempts to crack the password using a brute-force approach."""
    start_time = time.time()
    attempt_count = 0

    for attempt_list in product(characters,repeat=len(correct_password)):
        attempt = ''.join(attempt_list)
        attempt_count += 1
        if attempt == correct_password:
            end_time = time.time()
            duration = end_time - start_time
            return attempt_count, duration


password_length = 4
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")

print("Starting brute-force attack...")
total_possible_passwords = len(characters)**password_length

print(f"Going through {len(characters)} X {password_length} = {total_possible_passwords} possible options")
attempts, duration = brute_force(generated_password)

    
print(f"Password cracked!")
print(f"Cracked Password: {generated_password}")        
print(f"Number of attempts: {attempts}")
print(f"Time taken: {duration:.4f} seconds")