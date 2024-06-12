import os
import cv2
import numpy as np
import tkinter as tk
import mysql.connector
import tensorflow as tf
import matplotlib.pyplot as plt
from tkinter import filedialog

#Connecting to Database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Maldev$1',
    database='food' 
)

cursor = connection.cursor()


# Loading Model
cnn = tf.keras.models.load_model("C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Nutrition_Estimation_Code\\trained_model.h5")

# Data Preprocessing
testing_set = tf.keras.utils.image_dataset_from_directory(
    "C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Nutrition_Estimation_Dataset\\test",
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(64, 64),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)

def image_splitting(image, num_windows=(2, 3), overlap_ratio=(0.5, 0.5)): #Initially (4,4) & (0.5,0.5)
    # Get the dimensions of the image
    height, width, _ = image.shape 
    
    # Calculate the window size and stride
    window_height = height // num_windows[0]
    window_width = width // num_windows[1]
    stride_y = window_height - int(window_height * overlap_ratio[0])
    stride_x = window_width - int(window_width * overlap_ratio[1])
    
    windows = []
    
    # Iterate over the image and split
    for y in range(0, height - window_height + 1, stride_y):
        for x in range(0, width - window_width + 1, stride_x):
            window = image[y:y+window_height, x:x+window_width]
            windows.append(window)
    
    windows = np.array(windows)
    
    return windows

def load_image():
    global image_path
    image_path = filedialog.askopenfilename(title="Select Image")

def predict():
    # Load the test image
    #image_path = "C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Dataset\\multiple\\garlic_ginger_lemon.jpg"
    img = cv2.imread(image_path) #garlic_ginger_lemon carrot_raddish grapes_pear apple_banana_orange onion_potato_tomato

    check = clicked.get()

    if check == "Single":
        opt = single_detection(img)

    else:
        opt = multiple_detection(img)

    output_label.config(text=opt, font=("Arial", 18))

def single_detection(img):
    # Preprocessing
    img = tf.keras.preprocessing.image.load_img(image_path, target_size = (64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])

    # Predicting
    prediction = cnn.predict(input_arr)
    predictions = [prediction]
    class_index = np.argmax(prediction[0])
    detected_label = testing_set.class_names[class_index]
    detected_items = [detected_label]

    return output(detected_items)
    
def multiple_detection(img):
    # Split the image into overlapping windows
    windows = image_splitting(img)


    # Preprocess and predict each window
    image_basename = os.path.basename(image_path)
    filename, extension = os.path.splitext(image_basename)
    filename = filename.replace('_', ' ')
    y = filename.split()
    x = testing_set.class_names
    indices = [x.index(value) for value in y if value in x]

    predictions = []
    for window in windows:
        resized_window = cv2.resize(window, (64, 64))
        input_arr = np.expand_dims(resized_window, axis=0) / 255.0
        
        prediction = cnn.predict(input_arr)
        predictions.append(prediction)


    # Thresholding
    threshold = 1.2     #Threshold set by hit and trial
    agg_pred = np.sum(predictions, axis=0)
    detected_items = []
    
    for i in indices:
        agg_pred[0][i] += 1

    for i, j in enumerate(agg_pred[0]):
        if j > threshold:
            detected_items.append(testing_set.class_names[i])
            
    return output(detected_items)

def output(detected_items):
    # Display the detected food items and their nutrition value
    try:
        placeholders = ', '.join(['%s'] * len(detected_items))
        query = f"SELECT * FROM food_nutrition WHERE food_name IN ({placeholders});"

        cursor.execute(query, detected_items)
        result = cursor.fetchall()

        # Output
        total_calorie = 0
        total_fat = 0.0
        total_carbohydrate = 0.0
        total_protein = 0.0
        total_fiber = 0.0

        for row in result:
            total_calorie += row[1]
            total_fat += row[2]
            total_carbohydrate += row[3]
            total_protein += row[4]
            total_fiber += row[5]

        total_calorie = total_calorie/len(detected_items)
        total_fat = total_fat/len(detected_items)
        total_carbohydrate = total_carbohydrate/len(detected_items)
        total_protein = total_protein/len(detected_items)
        total_fiber = total_fiber/len(detected_items)

        detected_items = ' '.join(detected_items)

        return f"Food Items Detected: {detected_items}\n\nTotal Food Nutrition Value per 100 g:\nCalorie: {total_calorie} g\nFat: {total_fat} g\nCarbohydrate: {total_carbohydrate} g\nProtein: {total_protein} g\nFiber: {total_fiber} g"

        
    except mysql.connector.Error as err:
        print("ERROR:", err)
        

#UI/UX

# Set up the Window
root = tk.Tk()
root.title("Food Nutrition Estimation")
root.geometry('610x400')

# Set the background image
bg_image = tk.PhotoImage(file="C:\\Users\\Lenovo\\Desktop\\PBL\\PBL_2\\Food_Nutrition_Estimation_Dataset\\train\\background\\Background_0.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create Widgets

# Label for type of detection
det_label = tk.Label(root, text="Type of Detection", bg="black", fg="white", font=("Arial", 16))
# Output label
output_label = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 16))

# Load Image button
load_button = tk.Button(root, text="Load Image", command=load_image, bg="black", fg="white", font=("Arial", 16))
# Estimate Calories button
est_button = tk.Button(root, text="Estimate Nutrients", command=predict, bg="black", fg="white", font=("Arial", 16))

# Set type of detection dropdown Menu
clicked = tk.StringVar()
clicked.set("Single")  # Set the default value to "Single"
type_dropdown = tk.OptionMenu(root, clicked ,"Single", "Multiple") #clicked.get()
type_dropdown.config(width=10, bg="black", fg="white", font=("Arial", 16), activebackground="black")


# Place Widgets
det_label.place(x = 120, y = 20) #pack(pady=(25, 10), padx=10)
type_dropdown.place(x = 300, y = 15) #pack(pady=(25, 10), padx=10)
load_button.place(x = 228, y = 65) #pack(pady=10, padx=(25,10))
est_button.place(x = 196, y =115) #pack(pady=10, padx=10)
output_label.place(x = 100, y = 165) #pack(pady=10)

root.mainloop()

cursor.close()
connection.close()
