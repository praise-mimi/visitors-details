
from datetime import datetime, timedelta

# Custom exception for duplicate visitor
class DuplicateVisitorError(Exception):
    pass

# Custom exception for time restriction
class TimeRestrictedVisitorError(Exception):
    def __init__(self, next_allowed_time):
        self.next_allowed_time = next_allowed_time
        super().__init__(f"Please wait until {next_allowed_time.strftime('%Y-%m-%d %H:%M:%S')} to enter.")

# Function to get the last visitor's name and timestamp from the file
def get_last_visitor(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                last_name, last_time_str = last_line.split(' - ')
                last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
                return last_name, last_time
    except FileNotFoundError:
        # If the file doesn't exist yet, return None values
        return None, None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return None, None

# Function to add a visitor's name and current timestamp to the file
def add_visitor(file_path, name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_path, 'a') as file:
            file.write(f"{name} - {timestamp}\n")
        print(f"✅ Visitor {name} added successfully at {timestamp}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Main function to control the logic
def main():
    file_path = 'visitors.txt'
    name = input("Enter your name: ").strip()

    last_visitor, last_time = get_last_visitor(file_path)

    try:
        now = datetime.now()

        # Rule 1: Prevent duplicate consecutive visits
        if name == last_visitor:
            raise DuplicateVisitorError(f"{name} is already the last visitor.")

        # Rule 2: Enforce 5-minute interval between visits
        if last_time:
            time_diff = now - last_time
            if time_diff < timedelta(minutes=5):
                next_allowed_time = last_time + timedelta(minutes=5)
                raise TimeRestrictedVisitorError(next_allowed_time)

        # If all checks pass, add the visitor
        add_visitor(file_path, name)

    except DuplicateVisitorError as e:
        print(f"⚠️ Duplicate visitor error: {e}")
    except TimeRestrictedVisitorError as e:
        print(f"⏳ Access restriction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()