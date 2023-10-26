import os
import config
import parser


def remove_lines_starting_with(lines, strings_list) -> list:
    result_lines = [line for line in lines if not any(
        line.startswith(prefix) for prefix in strings_list)]
    return result_lines


def replace_words(lines, replacements) -> list:
    updated_lines = []

    for line in lines:
        for old_word, new_word in replacements.items():
            line = line.replace(old_word, new_word)
        updated_lines.append(line)

    return updated_lines


def clean_raw_pdf_output(dirty_directory_path, clean_directory_path) -> None:

    # Make sure the clean directory exists, creating it if necessary
    os.makedirs(clean_directory_path, exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(dirty_directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(dirty_directory_path, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            lines = remove_lines_starting_with(lines=lines,
                                               strings_list=config.line_removal_target_words)

            lines = replace_words(
                lines=lines, replacements=config.replacements)

            lines = remove_lines_starting_with(lines=lines,
                                               strings_list=config.line_removal_target_words)

            updated_original_text = ''.join(lines)

            cleaned_file_path = os.path.join(clean_directory_path, filename)

            # Write the modified text to the new file
            with open(cleaned_file_path, 'w') as file:
                # file.write(cleaned_file_path)
                # file.write('\n')
                file.write(updated_original_text)


# Specify the directory path where the text files are located
dirty_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\sample_raw_outputs"
clean_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\sample_clean_outputs"

# Call the function to make replacements
clean_raw_pdf_output(dirty_directory_path=dirty_directory_path,
                     clean_directory_path=clean_directory_path)
