import os
import config


def remove_lines_starting_with(lines, strings_list):
    result_lines = [line for line in lines if not any(
        line.startswith(prefix) for prefix in strings_list)]
    return result_lines


def clean_up_output(directory, replacements):
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            lines = remove_lines_starting_with(lines=lines,
                                               strings_list=config.line_removal_target_words)

            # Join the remaining lines to reconstruct the text
            original_text = ''.join(lines)

            # Perform replacements for each word in the dictionary
            for old_word, new_word in replacements.items():
                original_text = original_text.replace(old_word, new_word)

            # Write the modified text back to the file
            with open(file_path, 'w') as file:
                file.write(original_text)


# Specify the directory path where the text files are located
directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\dir"

# Call the function to make replacements and remove lines above the specified string
clean_up_output(directory = directory_path, replacements = config.replacements)
