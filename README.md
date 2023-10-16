# color_compress
To perform color clustering compression on an image using the K-Means method.



## Prerequisite

```bash
pip install pillow
pip install numpy
```



## Usage

```python
from color_compress import color_compress
input_file  = "path/to/input_file.png"
output_file = "path/to/output_file.png"
color_count = 16
color_compress(input_file, output_file, color_count)
print("DONE")
```

