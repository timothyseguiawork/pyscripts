from pathlib import Path

#C:\Users\tseguia\OneDrive - New York State Office of Information Technology Services\Documents\SSI CALENDAR\2022\secquarter2022
filePath = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Documents\\SSI CALENDAR\\2022\\secquarter2022\\2ndquarter2022.txt"
print(filePath) 
with open(filePath) as fP:
    for line in fP: 
        print(line)