# Dataset Instructions

This folder contains the dataset configuration files used by the project, but **not the dataset itself**.  
The full dataset is approximately **3 GB** and is therefore **not included in the repository**.

To run training or inference locally, you must download the dataset manually and place it in the correct folder structure as described below.

---

## Dataset source

The project uses the **AeroScan: Military Aircraft Classification** dataset from Kaggle.

Dataset link:  
https://www.kaggle.com/datasets/aeroscan/military-aircraft-classification

Download the dataset from Kaggle and extract it on your local machine.

---

### Notes

- The `images/` folders must contain all `.jpg` or `.png` files.
- The `labels/` folders must contain the corresponding YOLO `.txt` annotation files.
- Each image must have a matching label file with the same filename (e.g., `000123.jpg` ↔ `000123.txt`).
- The dataset is not tracked by Git and is excluded via `.gitignore`.

---

## About `dataset.yaml`

The `dataset.yaml` file defines how YOLO should load the dataset.  
It specifies:

- paths to training, validation, and test images
- number of classes (`nc`)
- class names (`names`)
