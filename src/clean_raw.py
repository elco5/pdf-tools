import os
import config
import re
import parser


def remove_lines_starting_with(lines, strings_list):
    result_lines = [line for line in lines if not any(
        line.startswith(prefix) for prefix in strings_list)]
    return result_lines





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
            print("reading file:  ", file_path)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            lines = remove_lines_starting_with(lines=lines,
                                               strings_list=config.line_removal_target_words)

            # Join the remaining lines to reconstruct the text
            original_text = ''.join(lines)

            # Perform replacements for each word in the dictionary
            for old_word, new_word in replacements.items():
                original_text = original_text.replace(old_word, new_word)

            # updated_original_text = parser.parse_test_device(original_text)
            updated_original_text = original_text

            # create new filepath for the modified text
            cleaned_file_path = os.path.join(clean_directory_path, filename)

            # Write the modified text to the new file
            with open(cleaned_file_path, 'w') as file:
                file.write(cleaned_file_path)
                file.write('\n')
                file.write(updated_original_text)

            run_remove_lines_starting_with(before_file_path = cleaned_file_path,
                                             after_file_path = cleaned_file_path)

# # Specify the directory path where the text files are located
# dirty_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\raw_outputs"
# clean_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\clean_outputs"

# # Call the function to make replacements
# clean_up_output(dirty_directory_path=dirty_directory_path,
#                 clean_directory_path=clean_directory_path,
#                 replacements=config.replacements)
