# file_read_write.py

# Step 1: Open and read the input file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (convert everything to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content into a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been read, modified, and saved to output.txt")