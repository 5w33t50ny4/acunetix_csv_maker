### Description:

This Python script reads a text file containing addresses and splits it into multiple CSV files, each containing up to 500 lines. The output files are named sequentially (e.g., `filename_part1.csv`, `filename_part2.csv`). It logs the number of lines written to each file in the console.

### How to Use:

1.  Save the script as `acu_csv_maker.py` or any other preferred name.
2.  Open a terminal or command prompt.
3.  Run the script using the following command:
    
    bash:
    `python acu_csv_maker.py input.txt` 
    
    Replace `input.txt` with the actual filename of your text file.
4.  The script will generate multiple CSV files (`input_part1.csv`, `input_part2.csv`, etc.) if the input file has more than 500 lines.
5.  The console will display how many lines were written to each CSV file.
