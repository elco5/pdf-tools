import os
import config
import re


def remove_lines_starting_with(lines, strings_list):
    result_lines = [line for line in lines if not any(
        line.startswith(prefix) for prefix in strings_list)]
    return result_lines


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
                test_device["main"]["brand"] = main_brand.group().strip()

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


def run_remove_lines_starting_with(before_file_path, after_file_path):
    # Read the file
    # print("reading file:  ", file_path)
    with open(before_file_path, 'r') as file:
        lines = file.readlines()

    lines = remove_lines_starting_with(lines=lines,
                                       strings_list=config.line_removal_target_words)

    # Join the remaining lines to reconstruct the text
    original_text_with_removals = ''.join(lines)

    with open(after_file_path, 'w') as file:
        file.write(original_text_with_removals)


def clean_up_output(dirty_directory_path, clean_directory_path, replacements):

    # Make sure the clean directory exists, creating it if necessary
    os.makedirs(clean_directory_path, exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(dirty_directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(dirty_directory_path, filename)

            # Read the file
            # print("reading file:  ", file_path)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            lines = remove_lines_starting_with(lines=lines,
                                               strings_list=config.line_removal_target_words)

            # Join the remaining lines to reconstruct the text
            original_text = ''.join(lines)

            # Perform replacements for each word in the dictionary
            for old_word, new_word in replacements.items():
                original_text = original_text.replace(old_word, new_word)

            updated_original_text = parse_test_device(original_text)
            # updated_original_text = original_text

            # create new filepath for the modified text
            cleaned_file_path = os.path.join(clean_directory_path, filename)

            # Write the modified text to the new file
            with open(cleaned_file_path, 'w') as file:
                file.write(updated_original_text)

            run_remove_lines_starting_with(before_file_path = cleaned_file_path,
                                             after_file_path = cleaned_file_path)

# Specify the directory path where the text files are located
dirty_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\raw_outputs"
clean_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\clean_outputs"

# Call the function to make replacements
clean_up_output(dirty_directory_path=dirty_directory_path,
                clean_directory_path=clean_directory_path,
                replacements=config.replacements)
