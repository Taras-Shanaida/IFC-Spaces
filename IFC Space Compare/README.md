# IFC Spaces Compare

This Python script compares data between two CSV files containing exported space data from Industry Foundation Classes (IFC) files. It identifies differences in the space attributes between the two datasets and outputs the discrepancies to a new CSV file for further analysis or reporting.

## How It Works

The script performs the following steps:

1. **Read CSV Data**: It reads the content of two input CSV files, each containing space data exported from separate IFC files. The data is stored as dictionaries, with global IDs as keys and space attributes as values.

2. **Compare Data**: It compares the space data between the two datasets, identifying differences in attributes such as space names, global IDs, and other parameters. It determines if a space is missing in one file or if there are differences in attributes between corresponding spaces in both files.

3. **Write Differences to CSV**: It writes the identified differences to a new CSV file, including the attributes that differ between corresponding spaces in the two datasets. Each row in the output CSV file represents a discrepancy between the datasets.

## Usage

To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Place your CSV files containing exported space data in the same directory as the script or specify the file paths in the `csv_file_path_1`, `csv_file_path_2`, and `output_csv_path` variables.
3. Run the script using `python ifc_spaces_data_comparator.py`.
4. The script will generate a new CSV file named `ifc_report.csv` containing the identified differences between the datasets.

## Dependencies

- `csv`: A built-in Python module for working with CSV files.

## Example Report

```bash
Name,LongName,GlobalId,Floor,Area,Volume
01-A0001,Office,5UOQVfyRw2Ty9FD8NBgmlx,PLAN 01,4812598.399900446,14437795199.701338,Area different in second file: 4812598.399900446 vs 4123598.421544309
701-B0001,WC,1HJKNpzXc4Aw6YG2MBouqv,PLAN 01,1627949.9999999509,3907079999.999882,Missing in first file
02-D0001,Kitchen,8CKXMrtQa3Fb7PH6YZowln,PLAN 02,0,0,Missing in first file
