import pandas as pd
import subprocess
# load path
file_path = r"C:\Users\SSD\Documents\GitDemo"

df = pd.read_excel(file_path + r"\data.xlsx")
#df = pd.read_excel(r"C:\Users\SSD\Documents\GitDemo\data.xlsx")
# Print data
print(df)
# Access a specific column
print(df["Sales"])
# Access a specific cell
print(df.iloc[0, 0])

path = r"C:\Program Files\Notepad++\notepad++.exe"
subprocess.Popen([path])
with open(file_path + r"sample.txt", "w") as file:
    file.write("Hello\n")
    file.write("This file was created using Python\n")
    file.write("Line 3\n")
print("File created successfully")

with open(file_path + r"sample.txt", "r") as file:
    content = file.read()
    print(content)
