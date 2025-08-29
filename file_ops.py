import csv
from pathlib import Path

header = ["Name", "Age", "Phone", "Track"]

def save_participant(path, participant_dict):
    file = Path(path)
    file_exists = file.exists()

    with open(file, mode= "a" , newline= '', encoding= 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        
        if not file_exists or file.stat().st_size ==0:
            writer.writeheader()
        writer.writerow(participant_dict)  

def load_participant(path):
    file= Path(path)
    file_exists = file.exists()

    if not file_exists:
        print("file does not exists")
        return[]
    else: 
        with open(file,mode= 'r', newline= '', encoding='utf8') as f:
            reader= csv.DictReader(f)
            return list(reader)