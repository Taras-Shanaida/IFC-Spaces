import csv
import ifcopenshell
import os
from shapely.geometry import Polygon

def get_floor_name(space, ifc_file):
    for decomposition in space.Decomposes:
        if decomposition.is_a("IfcRelAggregates"):
            parent = decomposition.RelatingObject
            if parent.is_a("IfcBuildingStorey"):
                return parent.Name
            elif parent.Decomposes:
                return get_floor_name(parent, ifc_file)
    return "Not Found"

def calculate_area_of_polygon(points):
    polygon = Polygon(points)
    return polygon.area

def extract_points_from_composite_curve(composite_curve):
    points = []
    for segment in composite_curve.Segments:
        if segment.ParentCurve.is_a("IfcPolyline"):
            polyline_points = segment.ParentCurve.Points
            for point in polyline_points:
                coord = (point.Coordinates[0], point.Coordinates[1])
                if coord not in points:
                    points.append(coord)
    if points and points[0] != points[-1]:
        points.append(points[0])
    return points

def calculate_area_and_volume(room):
    area = 0
    volume = 0
    for representation in room.Representation.Representations:
        if representation.RepresentationType == 'SweptSolid':
            for solid in representation.Items:
                if solid.is_a("IfcExtrudedAreaSolid"):
                    profile_def = solid.SweptArea
                    if profile_def.is_a("IfcArbitraryClosedProfileDef"):
                        outer_curve = profile_def.OuterCurve
                        if outer_curve.is_a("IfcPolyline"):
                            points = [(point.Coordinates[0], point.Coordinates[1]) for point in outer_curve.Points[:-1]]
                            area = calculate_area_of_polygon(points)
                        elif outer_curve.is_a("IfcCompositeCurve"):
                            points = extract_points_from_composite_curve(outer_curve)
                            area = calculate_area_of_polygon(points)
                        extrusion_depth = solid.Depth
                        volume = area * extrusion_depth
                        return area, volume
    return area, volume

def extract_space_data(ifc_file):
    spaces_data = []
    for space in ifc_file.by_type('IfcSpace'):
        space_name = space.Name or 'Unnamed'
        space_long_name = getattr(space, 'LongName', space.Name)
        space_global_id = space.GlobalId
        space_floor = get_floor_name(space, ifc_file)
        area, volume = calculate_area_and_volume(space)

        spaces_data.append({
            'Name': space_name,
            'LongName': space_long_name,
            'GlobalId': space_global_id,
            'Floor': space_floor,
            'Area': area,
            'Volume': volume
        })
    return spaces_data

def write_csv(spaces_data, csv_output_path):
    fieldnames = ['Name', 'LongName', 'GlobalId', 'Floor', 'Area', 'Volume']
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for space_data in spaces_data:
            writer.writerow(space_data)

def main(ifc_path):
    ifc_file = ifcopenshell.open(ifc_path)
    spaces_data = extract_space_data(ifc_file)
    
    # Determine the directory path to save the CSV file
    output_dir = os.path.dirname(ifc_path)
    csv_output = os.path.join(output_dir, "exported_spaces.csv")
    
    write_csv(spaces_data, csv_output)
    print(f"Data exported to {csv_output}")

if __name__ == "__main__":
    ifc_path = "Model.ifc"
    main(ifc_path)
