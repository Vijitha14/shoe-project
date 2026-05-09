# Shoe Image Rectification Pipeline

## Zero-Cost Product Catalog Generation Workflow

---

# Overview

This project implements a zero-cost shoe image rectification pipeline for generating standardized e-commerce catalog images using open-source tools and automation workflows.

The system preprocesses shoe images, removes backgrounds, organizes multiple viewing angles, and generates clean product-ready outputs suitable for professional catalog presentation.

---

# Features

* Background removal using AI segmentation
* Standardized white-background product images
* Multi-angle shoe image organization
* Automated preprocessing workflow
* Nike-style studio catalog presentation
* Open-source and zero-cost implementation
* Scalable folder structure
* Google Drive integration support

---

# Technologies Used

## Programming Language

* Python 3.10+

## Libraries

* OpenCV
* rembg
* Pillow
* numpy
* torch
* torchvision
* transformers
* streamlit

## Tools & Platforms

* Visual Studio Code
* Google Colab
* Google Drive
* GitHub
* GIMP

---

# Project Structure

```text
shoe-project/
│
├── raw-images/
├── refined-images/
├── processed-images/
├── output/
│   ├── left-side/
│   ├── right-side/
│   ├── front/
│   ├── back/
│   ├── top/
│   ├── sole/
│   ├── three-quarter-front/
│   └── three-quarter-back/
│
├── logs/
├── inventory/
├── scripts/
└── reports/
```

---

# Installation

## Clone Repository

```bash
git clone <repository-link>
cd shoe-project
```

---

# Install Dependencies

```bash
pip install opencv-python rembg pillow numpy torch torchvision transformers streamlit
```

---

# Workflow

## Step 1 — Add Raw Images

Place original shoe images inside:

```text
raw-images/
```

---

## Step 2 — Run Preprocessing Script

Example:

```python
from rembg import remove
from PIL import Image

input_path = 'raw-images/shoe.png'
output_path = 'processed-images/output.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print('Processing Complete')
```

---

## Step 3 — Organize Outputs

Move processed images into standardized angle folders:

* left-side
* right-side
* front
* back
* top
* sole
* three-quarter-front
* three-quarter-back

---

# Image Standards

## Background

* Pure white seamless background

## Lighting

* Soft diffused commercial lighting

## Quality

* High-resolution outputs
* Sharp edge preservation
* Clean product alignment

## Style

* E-commerce catalog presentation
* Nike-style premium studio aesthetic

---

# Classification Tracks

| Track   | Description                  |
| ------- | ---------------------------- |
| Track A | Ready PNG images             |
| Track B | Raw images requiring cleanup |
| Track C | Composite marketing images   |
| Track D | Unusable/insufficient images |

---

# Sample Output Types

The pipeline supports:

* Front product shots
* Rear heel shots
* Sole views
* Top views
* Three-quarter views
* Thumbnail close-ups
* Hero catalog images

---

# Google Drive Integration

Google Drive can be mounted in Google Colab for cloud-based workflow management.

Example:

```python
from google.colab import drive
drive.mount('/content/drive')
```

---

# Future Improvements

* Automatic angle classification
* Batch image preprocessing
* AI-based pose correction
* Product metadata generation
* Streamlit dashboard deployment
* Inventory management integration

---

# Result

The project successfully demonstrates a scalable and reusable product image rectification workflow using completely free and open-source technologies.

Generated outputs are suitable for:

* E-commerce product catalogs
* Product listings
* Online marketplaces
* Inventory management systems
* Brand presentation assets

---

# Author

Glory Vijitha

---

# License

This project is intended for e
