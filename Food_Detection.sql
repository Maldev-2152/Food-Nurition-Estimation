CREATE DATABASE IF NOT EXISTS food;
USE food;
CREATE TABLE IF NOT EXISTS food_nutrition (
    food_name VARCHAR(50) PRIMARY KEY,
    calorie INT,
    fat FLOAT,
    carbohydrate FLOAT,
    protein FLOAT,
    fiber FLOAT
);

INSERT INTO food_nutrition (food_name, calorie, fat, carbohydrate, protein, fiber)
VALUES
('apple', 52, 0.2, 14, 0.3, 2.4),
('banana', 89, 0.3, 23, 1.1, 2.6),
('beetroot', 43, 0.2, 10, 1.6, 2.8),
('bell pepper', 31, 0.3, 6, 1.3, 2.1),
('cabbage', 25, 0.1, 6, 1.3, 2.5),
('capsicum', 20, 0.2, 4.6, 0.9, 1.7),
('carrot', 41, 0.2, 10, 0.9, 2.8),
('cauliflower', 25, 0.3, 5, 1.9, 2),
('chilli pepper', 40, 0.4, 8.8, 1.9, 3.3),
('corn', 96, 1.5, 21, 3.4, 2.7),
('cucumber', 15, 0.1, 3.6, 0.7, 0.5),
('eggplant', 25, 0.2, 6, 1, 3),
('garlic', 149, 0.5, 33, 6, 2.1),
('ginger', 80, 0.8, 18, 2, 2),
('grapes', 69, 0.2, 18, 0.7, 0.9),
('jalapeño', 29, 0.4, 5, 1.2, 2.8),
('kiwi', 61, 0.5, 15, 1.1, 2.1),
('lemon', 29, 0.3, 9.3, 1.1, 2.8),
('lettuce', 15, 0.1, 2.9, 1.4, 1.3),
('mango', 60, 0.4, 15, 0.8, 1.6),
('onion', 40, 0.1, 9.3, 1.1, 1.7),
('orange', 47, 0.1, 12, 0.9, 2.4),
('paprika', 26, 0.3, 6, 1, 2),
('pear', 57, 0.1, 15, 0.4, 3.1),
('peas', 81, 0.4, 14, 5, 5),
('pineapple', 50, 0.1, 13, 0.5, 1.4),
('pomegranate', 83, 1.2, 19, 1.7, 4),
('potato', 77, 0.1, 17, 2, 2.2),
('radish', 16, 0.1, 3.4, 0.7, 1.6),
('soy beans', 446, 20, 30, 36, 9),
('spinach', 23, 0.4, 3.6, 2.9, 2.2),
('sweetcorn', 86, 1.2, 19, 3.2, 2.7),
('sweetpotato', 86, 0.1, 20, 1.6, 3),
('tomato', 18, 0.2, 3.9, 0.9, 1.2),
('turnip', 28, 0.1, 6, 0.9, 1.8),
('watermelon', 30, 0.2, 8, 0.6, 0.4);