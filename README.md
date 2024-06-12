# Food-Nurition-Estimation
Project Description:
for this project I have 1st trained a deep learning CNN model on the dataset fruits and vegetables that is taken from kaggle. The dataset has 3 directories, test train and validation & each of those directories contain 36 sub directories which are also the labels. These 36 subdirectories are the fruits and vegetables(banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango, cucumber, carrot, capsicum, onion, potato, lemon, tomato, raddish, beetroot, cabbage, lettuce, spinach, soy bean, cauliflower, bell pepper, chilli pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalepeño, ginger, garlic, peas, eggplant.) and each of those contain preprocessed images to test, train and validate the model. The deep learning CNN model is trained and validated using tensorflow and after the model is trained & validated it is saved as a .h5 file to be used later to detect fruits and vegetables. Then a database food is created consisting of only 1 table food_nutrition. This table has the following structure
•	food_name (VARCHAR(50)): The name of the food item.
•	calorie (INT): The calorie count per serving of the food item.
•	fat (FLOAT): The fat content per serving of the food item.
•	carbohydrate (FLOAT): The carbohydrate content per serving of the food item.
•	protein (FLOAT): The protein content per serving of the food item.
•	fiber (FLOAT): The fiber content per serving of the food item.
All the values are taken directly from google and all are pre 100 g. This database and table is created in mysql and mysql is later connected to python using mysql.connector. Then from the UI/UX the user can choose the type of object detection to be performed, single or multiple. After selection the type of detection the user can input the image and object in the images will be detected accordingly. If the type of detection is single then the save model which was trained by me will directly be used to detect the object(fruit or vegetable). If the type of detection is multiple then when the user input an image, the image is spited into a few overlapping windows. Each of the overlapping windows has an overlapping ratio of (0.5,0.5). Then the earlier saved model is used to detect object in each of the overlapping window and their confidence metrices is summed and thresholding is applied, i.e. if and only if an object having a confidence score greater than the threshold value(= 1.2) is assumed to to appearing in the image and this is how a single object detection algorithm can detect multiple objects in a single image. After the object is detected the corresponding values calorie, fat, carbon, protine, fiber, of those food items are selected and averaged and displayed as an output in per 100 g.

**Project Description**

This project focuses on building a food nutrition detection system using deep learning and database integration. It involves several stages, from training a convolutional neural network (CNN) model to detecting and analyzing food items' nutritional content.

**1. Training CNN Model on Fruits and Vegetables Dataset**

- The project starts with training a CNN model on a dataset sourced from Kaggle. The dataset comprises three directories: train, test, and validation, each containing 36 subdirectories representing different fruits and vegetables.
  
- These 36 subdirectories correspond to various fruits and vegetables, including banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango, cucumber, carrot, capsicum, onion, potato, lemon, tomato, radish, beetroot, cabbage, lettuce, spinach, soybean, cauliflower, bell pepper, chili pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalapeño, ginger, garlic, peas, and eggplant.
  
- The images within these subdirectories are preprocessed and used for training and validation of the CNN model.

**2. Database Creation**

- Following model training, a MySQL database named "food" is created, consisting of a single table named "food_nutrition."
  
- The table has the following structure:
  - `food_name` (VARCHAR(50)): Name of the food item.
  - `calorie` (INT): Calorie count per serving of the food item.
  - `fat` (FLOAT): Fat content per serving of the food item.
  - `carbohydrate` (FLOAT): Carbohydrate content per serving of the food item.
  - `protein` (FLOAT): Protein content per serving of the food item.
  - `fiber` (FLOAT): Fiber content per serving of the food item.
  
- The nutritional values are obtained from reliable sources and standardized to be per 100 grams.

**3. Integration with Python**

- MySQL database is connected to Python using the mysql.connector library, enabling seamless interaction between the database and the Python environment.

**4. User Interface**

- The user interface allows users to choose between two types of object detection: single or multiple.
  
- In the single detection mode, the pre-trained CNN model is directly utilized to detect a single food item in the input image.
  
- In the multiple detection mode, the input image is split into overlapping windows, each with an overlap ratio of (0.5, 0.5). The pre-trained model is applied to detect objects in each window. Confidence scores for detected objects are summed, and a threshold (set at 1.2) is applied to identify objects with scores surpassing this value.
  
- Once the objects are detected, the corresponding nutritional values (calorie, fat, carbohydrate, protein, fiber) of the food items are selected and averaged. These values are then displayed as output, standardized to per 100 grams.

**5. Requirements**

**Software Requirements**

Python: Used for implementing the machine learning algorithms, connecting to the MySQL database, and building the user interface.

TensorFlow: Employed for training and validating the convolutional neural network (CNN) model.

Keras: Utilized as a high-level neural networks API, running on top of TensorFlow, for building and training the CNN model.

MySQL: Database management system used for storing food nutrition data and integrating it with Python.

mysql.connector: Python library employed for connecting to the MySQL database from Python environment.

HTML/CSS: Used for front-end design and layout, particularly for creating aesthetically pleasing user interfaces.

Django: Used for making a web-application and connecting the front-end and back-end.

**Hardware Requirements**

No hardware is required for this project as it is entirely software-based. All processing tasks are performed on a standard computer system without any specialized hardware dependencies.
