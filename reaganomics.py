file_path = 'reaganomics.txt'
target_subheading = 'Federal income tax and payroll tax levels'

# Read the file and copy the content
content = ''
with open(file_path, 'r') as file:
    for line in file:
        if target_subheading in line:
            break
        content += line

# Print the copied content
print(content)