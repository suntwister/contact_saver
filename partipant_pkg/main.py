from pathlib import Path
import file_ops as _file_ops
#from file_ops import save_participant, load_participants

file_path = Path("contact.csv")

while True:
    name = input("Enter your full name: ")
    if not name:
        print("Name cannot be empty. Please try again.")
        continue
    if not name.replace(" ", "").isalpha():
        print("Name must contain only alphabetic characters. Please try again.")
        continue

    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be a positive integer. Please try again.")
            continue
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")
        continue
    
    phone_number = input("Enter your phone number: ")
    if len(phone_number) != 11:
        print("Phone number must be 11 digits")
        continue
    if not phone_number.isdigit():
        print("Enter a valid number")
        continue

    # checking for existing number
    existing_participants = _file_ops.load_participants(file_path)
    existing_number = {p["Phone Number"] for p in existing_participants}
    if phone_number in existing_number:
        print("This phone number is already registered")
        continue

    track_list = ["Ai Engineer", "Ai Developer"]
    print("--- Select Track ---")
    print(f"Select\n\t 1 - for {track_list[0]}\n\t 2 - for {track_list[1]}")
    track_inp = int(input("Enter your track: "))
    track = track_list[track_inp - 1]
    if not track:
        print("Track cannot be empty, please try again")
        continue

    participant_dict = {
        "Name": name,
        "Age": age,
        "Phone Number": phone_number,
        "Track": track
    }

    _file_ops.save_participant(file_path, participant_dict)

    print("Participant information saved successfully.")

    # Adding another participant
    add_another = input("Do you want to add another participant? (yes/no): ").strip().lower()
    if add_another != 'yes':
        break
    

participants = _file_ops.load_participants(file_path)
print("\n---Registered Participants---")
print(participants)
# for p in participants[]:
#     print(p)
print("--" * 10)
print(f"Total participants: {len(participants)}")