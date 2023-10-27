import re
import os


def test_device_parser_old(line):
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
    if branch_brand.lower() in ["siemens"]:
        branch_brand = "Siemens"
    elif branch_brand.lower() in ["sq d", "square d"]:
        branch_brand = "Square D"
    elif branch_brand.lower() in ["eaton"]:
        branch_brand = "Eaton"

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

    # Initialize variables with default values
    main_brand = "N/A"
    main_rating = "N/A"
    branch_brand = "N/A"
    branch_rating = "N/A"

    # Split the line and extract the parts
    parts = line.split(':')
    if len(parts) > 1:
        device_info = parts[1].strip()
        device_parts = device_info.split('/')
        
        if len(device_parts) >= 1:
            main_part = device_parts[0].strip()
            branch_part = device_parts[-1].strip()
                        
            brand_mappings = {
                "siemens": "Siemens",
                "sq d": "Square D",
                "square d": "Square D",
                "eaton": "Eaton"
            }

            # Extract main_brand
            main_brand_match = re.search(r'[^0-9]+', main_part)
            if main_brand_match:
                main_brand = main_brand_match.group().strip()
                # Use the mapping if the brand is found in the dictionary
                main_brand = brand_mappings.get(main_brand.lower(), main_brand)

      
            # Extract main_rating
            main_rating_match = re.search(r'(\d+)', main_part)
            if main_rating_match:
                main_rating = main_rating_match.group().strip()


        # Extract branch_brand
        branch_brand_match = re.search(r'[^0-9]+', branch_part)
        if branch_brand_match:
            branch_brand = branch_brand_match.group().strip()
        
        # Extract branch_rating
        branch_rating_match = re.search(r'(\d+)', branch_part)
        if branch_rating_match:
            branch_rating = branch_rating_match.group().strip()

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


def value_parser(line):
    # split line into key and value
    line_key = line.split(":")[0].strip()
    line_value = line.split(":")[1].strip()

    # match the numeric (float) part of the value
    line_value_numeric = float(re.search(
        r'(\d+\.\d+|\d+)', line_value).group().strip())
    # parse numeric part based on the prefix given (milli, micro)
    # value will be now in milli - keys should reflect this
    if "m sec" in line_value.lower():
        line_value_numeric = line_value_numeric
    elif "u sec" or "µ sec" in line_value.lower():
        line_value_numeric = line_value_numeric * 0.001

    # recompose output
    line_value_numeric = round(line_value_numeric, 4)
    # print(f"{line_value} --> {line_value_numeric}")
    recomposed_text = f"{line_key}: {line_value_numeric}\n"

    return recomposed_text


def run_parser(clean_directory_path):
    # Create a dictionary that maps prefixes to parser functions
    parser_functions = {
        "Test Device:": test_device_parser,
        "oscillogram:": oscillogram_parser,
        "closing_time": value_parser,
        "time_to_peak_current": value_parser,
        "i_duration": value_parser
    }

    # Iterate over files in the directory
    for filename in os.listdir(clean_directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(clean_directory_path, filename)

            # Create a list to store modified lines
            modified_lines = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    # Check for a matching prefix in the dictionary
                    for prefix, parser_func in parser_functions.items():
                        if line.startswith(prefix):

                            # Call the associated parser function and append the modified line
                            modified_line = parser_func(line)
                            modified_lines.append(modified_line)
                            break  # Stop checking for other prefixes

                    else:
                        # If no match is found, keep the line as it is
                        modified_lines.append(line)

            # Join the modified lines and save them back to the file
            modified_text = ''.join(modified_lines)
            with open(file_path, 'w') as file:
                file.write(modified_text)

