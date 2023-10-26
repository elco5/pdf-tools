
# remove lines beginning with these words / strings
line_removal_target_words = ["Voltage",
                             "Current",
                             "High",
                             " ",
                             "-",
                             "\n",
                             "Sweep#",
                             "Cedar",
                             "NOTE",
                             "Data",
                             "INSTRUMENTATION",
                             "Performance",
                             "ANALYSIS",
                             "AVAILABLE",
                             "GRID",
                             "INVESTIGATION",
                             "OSC",

                             ]

# Define the dictionary of word replacements
replacements = {
    "Was the Breaker Tripped after the test?": "breaker_tripped: ",
    "Could the Breaker be Reset?": "breaker_reset: ",
    "Did it have continuity in all poles?": "breaker_continuity: ",
    "Was the Enclosure Fuse Opened?": "enclosure_fuse_open: ",
    "Closing Angle": "closing_angle(deg): ",
    "Closing time  (V0)+": "closing_time(us): ",
    "Peak Current (Ip)": "peak_current(kA): ",
    "Time to Ip": "time_to_peak_current(ms): ",
    "I2T": "i_sq_t(k): ",
    "I Duration": "i_duration(ms): ",
    "Sample No.:": "\nsample: ",
    "Oscillogram No.:": "\noscillogram: ",
    "Date of Test:": "test_date: ",
    "  Time of Test:": "\ntime_of_test: ",
    " Comment Section": "\nCOMMENT SECTION",
    "  Calibration Date:": "\ncalibration_date:",
    "2OCV =": "\nOCV:",
    " Rms Sym Current =": "\ngrid_rms_sym_current: ",
    "Power Factor =": "\npower_factor:",
    "  OCV = 244 V": "",
    "  OCV = 240 V": "",
    "AVAILABLE CIRCUIT CHARACTERISTICS:": "\nAVAILABLE CIRCUIT CHARACTERISTICS",
    "ANALYSIS RESULTS TABLE": "",
    "Osc. No:": "",
    " Comment Section": "\nComments: ",
    # Add more word replacements as needed
}
closing_angle = "closing_angle(deg)"
columns = [
    "test_date",
    "time_of_test",
    "grid_rms_sym_current",
    "main_brand",
    "main_rating",
    "branch_brand",
    "branch_rating",
    "closing_time(us)",
    "peak_current(kA)",
    "time_to_peak_current(ms)",
    "i_sq_t(k)",
    closing_angle,
    "power_factor",
    "i_duration(ms)",
    "oscillogram",
    "sample",
    "breaker_tripped",
    "breaker_reset",
    "breaker_continuity",
    "enclosure_fuse_open",
    "calibration_date",
    "comments"
]
use_raw_column_data = [
    "oscillogram",
    "breaker_tripped",
    "breaker_reset",
    "breaker_continuity",
    "main_brand",
    "branch_brand",
    # "i_2_t(kA^2s)",

]

# Specify the directory path where the text files are located
pdf_directory = r'C:\Users\ecountrywood\dev\tools\pdf_tools\data\pdf_inputs'  # Replace with the path to your directory of PDF files
raw_output_directory = r'C:\Users\ecountrywood\dev\tools\pdf_tools\data\raw_outputs'  # Replace with the path to the directory where you want to save text files
dirty_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\raw_outputs"
clean_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\clean_outputs"
results_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\results"
