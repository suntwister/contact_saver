

from pathlib import Path
import file_ops

file_path = Path("contact.csv")


while True:

    participant_dict = {}

    name = input("Enter your name: ")
    if not name:
        print("name must not be empty")
        continue
    if not name.replace(" "," ").isalpha():
        print("name must contain alphabet")
        continue

    try:
        age = int(input("Enter your age:"))
        if age <= 0:
            print("age should be positive integer")
    except ValueError:
        print("age should only be a number")

             
    phone = input("Enter your phone number:")
    if len(phone) != 11 or not phone.isdigit():
        print("phone number must be 11 digit")

    track_list = ["AI_Engineering", "AI Developer"]
    print("Available track:", track_list)
    print(f"select:\n1.\t{track_list[0]}\n2.\t{track_list[1]}")
    track = int(input("select one of the option from the track_list above:"))
    track = track_list[track - 1]
    
    
    
    # if track == 1:
    #     print(track_list[0])
    # elif track == 2:
    #     print(track_list[1])
        
    # else:
    #     print("not a valid entry")
    #     break


    participant_dict["name"] = name
    participant_dict["age"] = age
    participant_dict["phone"] = phone
    participant_dict["track"] = track

    print(participant_dict)
    print("Total participant:", len(participant_dict))

    file_ops.save_participants(file_path)

    file_ops.load_participants(file_path)
    
    print("-" * 18)
    print("Total participant:", len(participant_dict))



















