# Image Viewer App

A simple Python desktop application to view images from online URLs with navigation controls.

## Features

- View images from a list of online URLs.
- Navigate forward and backward through images.
- Images are resized to fit the window while maintaining aspect ratio.
- Buttons to move between images and exit the app.

## Requirements

- Python 3.x
- tkinter (included with Python)
- Pillow (`pip install pillow`)
- requests (`pip install requests`)

## Usage

1. Run the script.
2. Use the forward (>>) and back (<<) buttons to navigate images.
3. Click "Exit Program" to close the app.

## Eligible URLs

**You can use any image URL that:**
- Points directly to an image file (ends with `.jpg`, `.jpeg`, `.png`, `.gif`, etc.).
- Is publicly accessible (does not require login or special headers).
- Returns a valid image when opened in your browser (not a webpage).

**Examples of eligible URLs:**
- `https://upload.wikimedia.org/wikipedia/commons/a/a0/Bill_Gates_2018.jpg`
- `https://images.unsplash.com/photo-1506744038136-46273834b3fb`
- `https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg`

**Not eligible:**
- URLs that lead to a webpage, not directly to an image (e.g., `https://commons.wikimedia.org/wiki/File:SomeImage.jpg`)
- URLs that require login or are behind a paywall
- URLs that do not return image content

**Tip:**  
To get a direct image URL, right-click the image in your browser and choose “Open image in new tab” or “Copy image address.”  
The link should open only the image, not a webpage.

## How it works

- Downloads images from specified URLs.
- Resizes images to fit the display area.
- Displays images in a Tkinter window with navigation buttons.

## Author

Developed by Arav Singh Patel.

Feel free to modify and extend this app!
