
import config
import pdf_scrape
# import clean_raw
import process_raw
import dataframe_builder
import parser

# Check if the script is being run as the main program
if __name__ == "__main__":

    pdf_scrape.pdf_scrape(pdf_directory=config.pdf_inputs_path,
                          raw_output_directory=config.raw_outputs_path)

    # Call the function to make deletions and replacements
    process_raw.clean_raw_pdf_output(dirty_directory_path=config.raw_outputs_path,
                              clean_directory_path=config.clean_outputs_path)
    
    # parse test device line                          
    parser.run_parser(clean_directory_path=config.clean_outputs_path)
    
    # build CSV from cleaned data
    dataframe_builder.process_clean_files_to_csv(columns=config.columns,
                                                 clean_directory_path=config.clean_outputs_path,
                                                 results_directory_path=config.results_path)

