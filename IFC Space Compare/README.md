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

## Example

```bash
python ifc_spaces_data_comparator.py
