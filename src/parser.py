import re
import os

def test_device_parser(line):
    '''
    Takes in a line in the form:
    Test Device: Eaton 10kA MAIN w/ Siemens 125 Branch
    returns:
    main_brand: Eaton
    main_rating: 10
    branch_brand: Siemens
    branch_rating: 125
    '''
    packet = line.split(':')[1].strip()
    main_part = '*'
    branch_part = '*'
    branch_brand = '*'
    branch_rating = '*'
    main_brand = '*'
    main_rating = '*'

    if '/' in packet:
        main_part = packet.split('/')[0].strip()
        branch_part = packet.split('/')[1].strip()
    else:
        branch_part = packet.strip()

        # Use regular expression to extract the non-numeric part for branch brand
    branch_brand = re.search(r'[^0-9]+', branch_part).group().strip()
    if branch_brand.lower() in ["siemens"]: branch_brand = "Siemens"
    elif branch_brand.lower() in ["sq d", "square d"]: branch_brand = "Square D"
    elif branch_brand.lower() in ["eaton"]: branch_brand = "Eaton"

    # Use regular expression to extract the numeric part for branch rating
    branch_rating = re.search(r'(\d+)', branch_part).group().strip()
    # Use regular expression to extract the non-numeric part for branch brand
    if main_part not in ['*']:
        main_brand = re.search(r'[^0-9]+', main_part).group().strip()
        if 'd' in main_brand.lower():
            main_brand = "Square D"
        # Use regular expression to extract the numeric part for branch rating
        main_rating = re.search(r'(\d+)', main_part).group().strip()

    output = f"main_brand: {main_brand}\nmain_rating: {main_rating}\nbranch_brand: {branch_brand}\nbranch_rating: {branch_rating}\n"

    return output

def oscillogram_parser(line):
    '''
    for lines of the form
    HPL3-77414 or HPL3-77415   OCV = 242 V
    only return 
    HPL3-77414
    '''
    # Regular expression pattern to match the desired format
    pattern = r'([A-Z0-9-]+)'

    match = re.search(pattern, line)
    if match:
        extracted_text = f"oscillogram: {match.group(1)}\n"
    return extracted_text    

def run_parser(clean_directory_path):
    # Iterate over files in the directory
    for filename in os.listdir(clean_directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(clean_directory_path, filename)

            # Create a list to store modified lines
            modified_lines = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    if line.startswith("Test Device:"):
                        # Call the parser function and append the modified line
                        modified_line = test_device_parser(line)
                        modified_lines.append(modified_line)
                    
                    elif line.lower().startswith("oscillogram:"):
                        # Call the parser function and append the modified line
                        modified_line = oscillogram_parser(line)
                        modified_lines.append(modified_line)
                    
                    else:
                        # Keep other lines as they are
                        modified_lines.append(line)

            # Join the modified lines and save them back to the file
            modified_text = ''.join(modified_lines)
            with open(file_path, 'w') as file:
                file.write(modified_text)
