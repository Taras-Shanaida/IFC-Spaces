import csv

# Paths to the CSV files
csv_file_path_1 = 'exported_spaces_oct.csv'  # Replace with the actual path to your first CSV file
csv_file_path_2 = 'exported_spaces_sep.csv'  # Replace with the actual path to your second CSV file
output_csv_path = 'ifc_report.csv'  # Replace with the actual path to your output CSV file

def read_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = {row['GlobalId']: row for row in reader}
    return data

def compare_data(data1, data2):
    differences = []
    all_keys = set(data1[list(data1.keys())[0]].keys()) | set(data2[list(data2.keys())[0]].keys())
    # Check for differences
    for global_id, values in data1.items():
        if global_id not in data2:
            diff = {key: values.get(key, '') for key in all_keys}
            diff['Difference'] = 'Missing in second file'
            differences.append(diff)
        else:
            for key in values:
                if values[key] != data2[global_id].get(key, ''):
                    diff = {k: values.get(k, '') for k in all_keys}
                    diff['Difference'] = f"{key} different in second file: {values[key]} vs {data2[global_id].get(key, '')}"
                    differences.append(diff)
                    break  # Assumes only one difference per global ID

    for global_id, values in data2.items():
        if global_id not in data1:
            diff = {key: values.get(key, '') for key in all_keys}
            diff['Difference'] = 'Missing in first file'
            differences.append(diff)

    return differences, all_keys

def write_differences_to_csv(differences, output_path, all_keys):
    with open(output_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(all_keys) + ['Difference']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for diff in differences:
            writer.writerow(diff)

# Main execution
if __name__ == "__main__":
    # Replace the paths with the actual paths where your CSV files are located
    data1 = read_csv_data(csv_file_path_1)
    data2 = read_csv_data(csv_file_path_2)

    # Compare the two data sets
    differences, all_keys = compare_data(data1, data2)

    # Write the differences to a CSV file
    write_differences_to_csv(differences, output_csv_path, all_keys)

    print(f"Differences written to {output_csv_path}")
