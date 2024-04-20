# IFC Space Export

This Python script extracts space parameters from an Industry Foundation Classes (IFC) file, such as space names, global IDs, areas, volumes, and the corresponding floor names. It then exports this data to a CSV file for further analysis or reporting.

## How It Works

The script utilizes the `ifcopenshell` library to parse the IFC file and extract relevant information about spaces within the building model. It calculates the area and volume of each space by analyzing the geometric representations defined in the IFC file.

The main functionalities of the script include:

- **Extracting Space Data**: The script iterates through all space entities in the IFC file and retrieves their attributes such as name, long name, global ID, and floor association.
- **Calculating Area and Volume**: It calculates the area and volume of each space by analyzing the geometric representation defined in the IFC file. This includes handling extruded area solids and composite curves.
- **Exporting to CSV**: The extracted space data is then exported to a CSV file, including columns for space name, long name, global ID, associated floor, area, and volume.

## Usage

To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Place your IFC file in the same directory as the script or specify the file path in the `ifc_path` variable.
4. Run the script using `python ifc_space_data_extractor.py`.
5. The script will generate a CSV file named `exported_spaces.csv` containing the extracted space data in the same directory as the input IFC file.

## Dependencies

- `ifcopenshell`: A Python library for working with IFC files.
- `shapely`: A Python library for geometric operations.
- `csv`: A built-in Python module for working with CSV files.
- `os`: A built-in Python module for interacting with the operating system.

## Example

```bash
Name,LongName,GlobalId,Floor,Area,Volume
01-A0001,Office,3TIREkwQv9Sx3FZ1VFezvk,PLAN 01,4812598.399900446,14437795199.701338
01-B0001,WC,3TIREkwQv9Sx3FZ1VFezpB,PLAN 01,1627949.9999999509,3907079999.999882
01-C0002,Space,3TIREkwQv9Sx3FZ1VFezbe,PLAN 01,1006252.9999251805,2453647315.01756
02-A0002,Hallway,3TIREkwQv9Sx3FZ1VFezb_,PLAN 02,298266.79154437076,894800374.6331123
02-D0001,Kitchen,3TIREkwQv9Sx3FZ1VFezbz,PLAN 02,0,0
