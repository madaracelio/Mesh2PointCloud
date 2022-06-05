import open3d as o3d
import sys
import argparse


def obj2xyz(input_file_path, output_file_path):
    """
        Convert objet (.obj) format to (.xyz) format
        Points : X Y Z
        Colors: empty
        Normals: empty
    """
    with open(input_file_path,'r', encoding="utf8") as f:
        lines = f.readlines()
    
    if output_file_path == "":
        nom = input_file_path.split(".")[0]
    else:
        nom = output_file_path

    out_ext = ".xyz"

    file_out = open(nom + out_ext, 'w')
    file_out.write("X Y Z\n")

    for line in lines:
        # Vertices
        if line[0] =='v' and line[1] != 'n' and line[1] != 't':
            final_line = line[2:] # replace "v " from each line before de value coordinates --> v x y z
            
            file_out.write(final_line)
    
    print("Conversion done, file saved...")
    file_out.close()
    

def obj2pcd(input_file_path, output_file_path):
    # Reading object file
    print("Read file...")
    obj = o3d.io.read_triangle_mesh(input_file_path)

    # Split the path to get file path and change to the final export extension
    if output_file_path == "":
        nom = input_file_path.split(".")[0]
    else:
        nom = output_file_path

    out_ext = ".pcd"

    print("Convert and and...")
    o3d.io.write_point_cloud(nom + out_ext , obj)
    print("Done\n")


# def obj2pcd(input_file_path):
#     print("Read object file...")
#     obj = o3d.io.read_triangle_mesh(input_file_path)
#     # (Points, colors, normal vector)
#     print("Check: (Points, colors, normal vector)...")
#     pcdmesh_obj = o3d.geometry.PointCloud()
#     pcdmesh_obj.points = obj.vertices
#     pcdmesh_obj.colors = obj.vertex_colors
#     pcdmesh_obj.normals = obj.vertex_normals

#     nom = input_file_path.split(".")[0]
#     out_ext = ".pcd"

#     # Convert and save to point cloud
#     print("Convert and save obj file to xyz file")
#     o3d.io.write_point_cloud(nom + out_ext , pcdmesh_obj)


parser = argparse.ArgumentParser(description='Convert a mesh object to point cloud.')

parser.add_argument('--i', type=str,
                    help='input path to the object file.')
parser.add_argument('--o', type=str,
                    help='outpout path to the converted file.')

parser.add_argument('--conv_type',
                    help='convert .obj file format to .xyz, .pcd format.')

# parser.add_argument('--obj_pcd',
#                     help='convert .obj file format to .pcd format.')

# argument
args = parser.parse_args()

"""
    Main function to run conversion
"""

if args.conv_type == "obj_xyz":
    obj2xyz(args.i, args.o)
if args.conv_type == "obj_pcd":
    obj2xyz(args.input, args.output)