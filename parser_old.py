import re
import os


def parse_test_device(original_text):
    """
    Parse and extract information from lines containing test device information.

    Args:
        original_text (str): A string containing test device information in the format "Test Device: ...".

    Returns:
        str: A formatted text representation of the parsed test device information.
    """
    # Initialize a dictionary to store the parsed test device information
    test_device = {
        "main": {
            "brand": None,
            "aisc_ka": None,
        },
        "branch": {
            "brand": None,
            "rating": None,
        }
    }

    # Search for lines that start with "Test Device:"
    lines = original_text.split('\n')
    split_string = '/'
    for i, line in enumerate(lines):
        if line.strip().startswith("Test Device:"):
            # Use regular expression to extract the non-numeric part for main brand
            print(line.strip())
            # no mcb
            if ":" not in line.split(":")[1]:
                main_brand = "None"

            else:
                main_brand = re.search(
                    r'[^0-9]+', line.split(":")[1].split(split_string)[0])

            # Use regular expression to extract the numeric part for main aisc_ka
            main_aisc_ka = re.search(
                r'(\d+)', line.split(":")[1].split(split_string)[0])

            # Use regular expression to extract the non-numeric part for branch brand
            branch_brand = re.search(
                r'[^0-9]+', line.split(":")[1].split(split_string)[1])

            # Use regular expression to extract the numeric part for branch rating
            branch_rating = re.search(
                r'(\d+)', line.split(":")[1].split(split_string)[1])

            # Update the test_device dictionary with extracted values
            if main_brand:
                mb = main_brand.group().strip()
                if mb.lower() in ["sq d", "square d"]:
                    mb = "Square D"
                if mb.lower() in ["schneider", "schnieder"]:
                    mb = "Schneider"
                test_device["main"]["brand"] = mb

            if main_aisc_ka:
                test_device["main"]["aisc_ka"] = main_aisc_ka.group(1)

            if branch_brand:
                test_device["branch"]["brand"] = branch_brand.group().strip()

            if branch_rating:
                test_device["branch"]["rating"] = branch_rating.group()

            # Create a formatted text representation of the parsed information for this line
            text_result = ''
            for category, attributes in test_device.items():
                for attribute, value in attributes.items():
                    text_result += f'{category}_{attribute}: {value}\n'

            # Replace the line in 'lines' with the formatted result
            lines[i] = text_result

    # Rejoin the lines to reconstruct the updated 'original_text'
    updated_original_text = '\n'.join(lines)

    return updated_original_text


def parsed_line(line):
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



def collect_test_devices(clean_directory_path):
    # Create a 'test_devices' file in the current directory
    output_dir = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\results"
    test_devices_file_name = 'test_devices.txt'
    test_devices_file_path = os.path.join(output_dir, test_devices_file_name)
    # Open the 'test_devices' file for writing
    with open(test_devices_file_path, 'w', encoding='utf-8') as test_devices_file:
        # List all files in the 'clean_directory_path'
        for filename in os.listdir(clean_directory_path):
            # Build the full path of the current file
            file_path = os.path.join(clean_directory_path, filename)

            # Check if the file exists and is a regular file
            if os.path.isfile(file_path):
                # Open the current file for reading
                with open(file_path, 'r', encoding='utf-8') as current_file:
                    # Iterate through the lines in the current file
                    for line in current_file:
                        # Check if the line starts with "Test Device:"
                        if line.startswith("Test Device:"):
                            # Write the line to the 'test_devices' file
                            test_devices_file.write(line)
                            # test_devices_file.write('\n')
                            test_devices_file.write(parsed_line(line))

    print(f"Test devices collected and saved to '{test_devices_file_path}'")


# Example usage:
# Specify the directory path containing the clean text files
clean_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\clean_outputs"
collect_test_devices(clean_directory_path)
