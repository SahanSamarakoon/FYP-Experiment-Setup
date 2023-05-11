import firebase_admin
from firebase_admin import credentials, db
from PIL import Image, ImageTk
import tkinter as tk

# Initializing the database with URL
cred = credentials.Certificate('./edge-genics-experiment-firebase-adminsdk-5j81b-1d738a8d9e.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://edge-genics-experiment-default-rtdb.asia-southeast1.firebasedatabase.app/'
}) 

# Create a Tkinter window
window = tk.Tk()
window.attributes('-fullscreen', True)

# Create a Tkinter canvas to display the image
canvas = tk.Canvas(window)
canvas.pack(fill=tk.BOTH, expand=True)

def listener(event):
    global count
    global label_array
    print("Data----", event.data)

    if isinstance(event.data, dict):
        for key, value in event.data.items():
            if str(value) == label_array[count]:
                count += 1
                print('Data updated as ', str(event.data))
                if count < 9:
                    count_str = "0" + str(count + 1)
                else:
                    count_str = str(count + 1)
                image = Image.open('pics/pic' + count_str + '.jpg')

                # Resize the image to fit the window using BICUBIC resampling filter
                image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.BICUBIC)

                # Convert the PIL Image object to a Tkinter PhotoImage object
                photo = ImageTk.PhotoImage(image)

                # Display the image on the canvas
                canvas.delete("all")
                canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                canvas.image = photo

    elif str(event.data) == None:
        print('Your data has been deleted!')

    else:
        if str(event.data) == label_array[count]:
                count += 1
                print('Data updated as ', str(event.data))
                if count < 9:
                    count_str = "0" + str(count + 1)
                else:
                    count_str = str(count + 1)
                image = Image.open('pics/pic' + count_str + '.jpg')

                # Resize the image to fit the window using BICUBIC resampling filter
                image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.BICUBIC)

                # Convert the PIL Image object to a Tkinter PhotoImage object
                photo = ImageTk.PhotoImage(image)

                # Display the image on the canvas
                canvas.delete("all")
                canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                canvas.image = photo

count = 0
label_array = ["person", "cat", "remote", "donut", "dog", "traffic light", "bicycle", "dog", "bicycle", "sandwich",
               "umbrella", "bus", "bowl", "banana", "person", "zebra", "potted plant", "elephant", "clock", "apple",
               "tv", "bird", "giraffe", "pizza", "train"]
               
db.reference('/').listen(listener)
count_str = "0" + str(count + 1)
image = Image.open('pics/pic' + count_str + '.jpg')
# Resize the image to fit the window using BICUBIC resampling filter
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.BICUBIC)
# Convert the PIL Image object to a Tkinter PhotoImage object
photo = ImageTk.PhotoImage(image)
# Display the image on the canvas
canvas.delete("all")
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.image = photo

# Run the Tkinter event loop
window.mainloop()