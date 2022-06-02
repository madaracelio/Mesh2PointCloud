# Mesh2PointCloud
Convert a ``mesh`` to ``point cloud``

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
python mesh2pc.py --input "path_to_object_file/filename.obj" --output "path_to_converted_file/filename" --conv_type "obj_xyz"
```

### 2. Obj to pcd

```
python mesh2pc.py --input "path_to_object_file/filename.obj" --output "path_to_converted_file/filename" --conv_type "obj_pcd"
```