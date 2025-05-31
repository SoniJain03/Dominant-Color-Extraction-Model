# Dominant Color Extraction using K-Means Clustering
This Streamlit app allows users to upload an image and extract its **top 3 dominant colors** using the **K-Means clustering algorithm**. 
It then reconstructs the image based on these dominant colors, providing a simplified, yet visually representative version.

## Features

- Upload any RGB image.
- View the original image.
- Extract top 3 dominant colors using unsupervised ML (K-Means).
- View the modified image with reduced colors.
- Interactive and user-friendly Streamlit interface.


## How It Works

1. The uploaded image is read and converted into a flat array of RGB pixels.
2. K-Means clustering is applied to group similar colors.
3. Each pixel is reassigned the RGB value of its cluster center (dominant color).
4. The image is reshaped and displayed using the dominant colors only.


## 🛠Tech Stack

- **Python**
- **Matplotlib** – For reading image files
- **NumPy** – Array manipulation
- **scikit-learn** – KMeans clustering
- **Streamlit** – UI for the web app

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dominant-color-extraction.git
   cd dominant-color-extraction
