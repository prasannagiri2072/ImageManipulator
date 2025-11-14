---

# 📸 Image Manipulator – Python Project

A simple and modular Python application for performing common image processing operations such as flipping, cropping, resizing, rotating, converting color modes, and exporting images.
The project includes both **interactive input mode** and **command-line (argparse) mode**, making it flexible for different use cases.

---

## 🚀 Features

This project supports multiple image manipulation tasks:

* **View Image Details** – format, size, and mode
* **Flip Vertically**
* **Flip Horizontally**
* **Convert to Black & White (Grayscale)**
* **Crop Image (Manual Coordinates)**
* **Rotate Image**
* **Resize Image**
* **Convert to JPG** (basic validation implemented)

The application uses the **Pillow (PIL)** library for all processing operations.

---

## 📂 Project Structure

```
Image-Manipulator/
│
├── image_manipulator.py   # Interactive mode (input prompts)
├── parser.py              # Command-line mode using argparse
├── func.py                # Core image processing functions
└── Images/                # Your input images (Optional folder)
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Pillow (PIL)** – For image manipulation
* **argparse** – For CLI interface
* **OS library** – For file handling

---

## 📥 Installation

1. Clone the repository:

```
git clone https://github.com/your-repo/image-manipulator.git
cd image-manipulator
```

2. Install required dependencies:

```
pip install pillow
```

---

## 💻 Usage

### **1️⃣ Interactive Mode**

Run the script and follow on-screen prompts:

```
python image_manipulator.py
```

The program will:

* Ask for the image path
* Ask which manipulation to apply
* Show or print the output

---

### **2️⃣ Command-Line Mode (argparse)**

Run specific operations using arguments:

```
python parser.py <option_number>
```

#### Options:

| Number | Operation                |
| ------ | ------------------------ |
| 1      | Get image details        |
| 2      | Flip vertically          |
| 3      | Flip horizontally        |
| 4      | Convert to black & white |
| 5      | Crop image               |
| 6      | Rotate image             |
| 7      | Resize image             |
| 8      | Convert to JPG           |

**Example:**

```
python parser.py 1
```

---

## 🧩 Core Functions (func.py)

This file contains reusable image-processing functions:

* `get_image_details(image)`
* `flip_image_vertically(image)`
* `flip_image_horizontally(image)`
* `convert_to_black_and_white(image)`
* `crop_image(image, x1, y1, x2, y2)`
* `rotate_image(image, angle)`
* `resize_image(image, height, width)`
* `convert_to_jpg()`

Error handling is included to prevent crashes caused by invalid file paths or user inputs.

---

## ⚠️ Known Issues

* `rotate_image()` uses an undefined variable `region` (bug).
* `convert_to_jpg()` only prints messages instead of converting files.
* Rotation functionality should use `img.rotate(angle)` for accuracy.

These can be improved in future updates.

---

## 📌 Future Enhancements (Optional)

* Add GUI using Tkinter or PyQt
* Improve rotation logic
* Add support for batch image processing
* Add save/export dialog for modified outputs
* Fix JPG conversion to actually output a converted file

---
