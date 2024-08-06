# Image Processing Scripts README

Welcome to the Image Processing Scripts repository! This collection of Python scripts is designed to help you manage and manipulate your image files efficiently. Below is a description of each script, along with instructions on how to run them.

## Table of Contents

- [Scripts Overview](#scripts-overview)
  - [Duplicate Image Remover](#duplicate-image-remover)
  - [Format Converter](#format-converter)
  - [Meta Data Remover](#meta-data-remover)
  - [Unwanted Extension Remover](#unwanted-extension-remover)
  - [Rotate](#rotate)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Scripts Overview

### Duplicate Image Remover
This script scans a specified directory for duplicate images based on their content and removes them, keeping the original files intact.

### Format Converter
This script allows you to convert images from one format to another (e.g., JPEG to PNG, BMP to TIFF). You can specify the source and target formats.

### Meta Data Remover
This script removes all metadata from image files, ensuring privacy and reducing file size. It supports various image formats.

### Unwanted Extension Remover
This script identifies and removes image files with unwanted extensions from a specified directory, helping to keep your image library organized.

### Rotate
This script rotates images by a specified angle. You can choose to rotate images clockwise or counterclockwise.

## Requirements

To run these scripts, you will need:

- Python 3.x installed on your system.
- The following Python libraries:
  - `Pillow` for image processing
  - `os` for file handling
  - `hashlib` for duplicate detection

You can install the required libraries using pip:

```bash
pip install Pillow
```

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Abhimanue-rajesh/image-manipulation-scripts.git
```
2. Navigate to the project directory:
```bash
cd image-processing-scripts
```


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.