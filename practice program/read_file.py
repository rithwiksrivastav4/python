# Define the file path
file_path = 'sudo add-apt-repository ppadotnetba.txt'

# Open the file and read all lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Print the lines
for line in lines:
    print(line.strip())  # Using strip() to remove any trailing newline characters
