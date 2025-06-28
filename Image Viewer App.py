from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

MAX_WIDTH = 900
MAX_HEIGHT = 700

root = Tk()
root.title("My Photos")
root.geometry("900x700")

image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/7/7c/Peugeot_206_WRC.jpg?20061126235419",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/DTM_Mercedes_W204_Lauda09_amk.jpg/1200px-DTM_Mercedes_W204_Lauda09_amk.jpg?20090521234845",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Adam_Simmons%2C_Swaffham_Raceway%2C_2017-03-11.JPG/1200px-Adam_Simmons%2C_Swaffham_Raceway%2C_2017-03-11.JPG?20210515105252",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Rally_Finland_2010_-_shakedown_-_Nasser_Al-Attiyah_1.jpg/1200px-Rally_Finland_2010_-_shakedown_-_Nasser_Al-Attiyah_1.jpg?20101015123936",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/DTM_Mercedes_W204_DiResta09_amk.jpg/1200px-DTM_Mercedes_W204_DiResta09_amk.jpg?20090611124444",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/2013_Porsche_911_Carrera_4S_%28991%29_%289626546987%29.jpg/1200px-2013_Porsche_911_Carrera_4S_%28991%29_%289626546987%29.jpg?20131024163505",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Trabant_P_601_S%2C_Bj._1986_%28Foto_Sp_2016-06-05%29.JPG/640px-Trabant_P_601_S%2C_Bj._1986_%28Foto_Sp_2016-06-05%29.JPG"
]

def resize_image(pil_image, max_width=MAX_WIDTH, max_height=MAX_HEIGHT):
    original_width, original_height = pil_image.size
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return pil_image.resize((new_width, new_height), Image.LANCZOS)

image_list = []
headers = {'User-Agent': 'Mozilla/5.0'}

for url in image_urls:
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('image'):
            pil_image = Image.open(BytesIO(response.content))
            resized_image = resize_image(pil_image)
            tk_image = ImageTk.PhotoImage(resized_image)
            image_list.append(tk_image)
        else:
            print(f"Skipped {url}: Not an image or bad response.")
    except Exception as e:
        print(f"Error loading {url}: {e}")

if not image_list:
    print("No images loaded. Exiting.")
    root.destroy()
    exit()

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label, button_forward, button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label, button_forward, button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
