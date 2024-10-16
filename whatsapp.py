# Import necessary modules
import pywhatkit as kit
import time
import csv
import os

# Load phone numbers from a CSV file
def load_phone_numbers(csv_file):
    phone_numbers = []
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                phone_numbers.append(row[0])  # Assuming phone numbers are in the first column
    except Exception as e:
        print(f"Error reading phone numbers: {e}")
    return phone_numbers

# Message to send
message = """
Igoner this , this is a testing message for an automated whatsapp message
"""

# Send messages to all numbers
def send_messages(phone_numbers, message):
    for phone_number in phone_numbers:
        try:
            # Send the message instantly
            kit.sendwhatmsg_instantly(phone_number, message, 15, True)
            print(f"Message sent to {phone_number}")
        except Exception as e:
            print(f"Failed to send message to {phone_number}: {str(e)}")
        # Sleep for a few seconds to avoid potential spam blocking
        time.sleep(10)

# Entry point of the script
if __name__ == "__main__":
    # Path to CSV file containing phone numbers
    csv_file = 'phone_numbers.csv'  # Make sure to update the path to your CSV file
    
    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print("Phone numbers CSV file not found. Please make sure it's in the correct location.")
    else:
        phone_numbers = load_phone_numbers(csv_file)
        if phone_numbers:
            print(f"Loaded {len(phone_numbers)} phone numbers.")
            send_messages(phone_numbers, message)
        else:
            print("No phone numbers found. Please check your CSV file.")
