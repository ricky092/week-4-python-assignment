
# question 1
# Simple Python program to read a file, modify its content, and write to a new file

# Step 1: Define input and output file names
input_file = 'input.txt'
output_file = 'output.txt'

# Step 2: Open the input file and read the content
with open(input_file, 'r') as infile:
    content = infile.read()

# Step 3: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 4: Write the modified content to the output file
with open(output_file, 'w') as outfile:
    outfile.write(modified_content)

print(f"Modified content written to '{output_file}'")




# question 2

# Ask user for input filename and handle errors
input_file = input("Enter the name of the input file (e.g., input.txt): ")

try:
    # Try to open and read the file
    with open(input_file, 'r') as infile:
        content = infile.read()
except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
    exit()  # Stop the program
except IOError:
    print(f"Error: The file '{input_file}' cannot be read.")
    exit()  # Stop the program

# Modify the content (convert to uppercase)
modified_content = content.upper()

# Define output filename (you can also ask user if you want)
output_file = 'output.txt'

# Write the modified content to the output file
with open(output_file, 'w') as outfile:
    outfile.write(modified_content)

print(f"Modified content written to '{output_file}'")

