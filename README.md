# Mesh2PointCloud
Convert a ``mesh (.obj)`` to ``point cloud(.pcd, .xyz)``.

``NB`` : Some functions used in this 3D file conversion code are functions that already exist in the [Open3D](http://www.open3d.org/docs/release/) library. The goal is to simplify the conversion of files without coding, just by running the script and everything is good.

## Requirements
---------------

> python version 3.x.x

```
    python -m pip install -r requirements.txt
```


## How to run the conversion script ?
-------------------------------------
Make sure that input objet file path exist and the output path folder, and just run this command line to convert file
### 1. Obj to xyz

```
python mesh2pc.py --i "path_to_object_file/filename.obj" --o "path_to_converted_file/filename" --conv_type "obj_xyz"
```

### 2. Obj to pcd

```
python mesh2pc.py --i "path_to_object_file/filename.obj" --o "path_to_converted_file/filename" --conv_type "obj_pcd"
```