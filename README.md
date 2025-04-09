# ClassificationAssignment04_SVM_FireOccurancePrediction

ClassificationAssignment04_SVM_FireOccurancePrediction

# Case:

Accurate prediction of fire occurrence can help in timely interventions and resource allocation. In this case study, we use a dataset containing various features related to forest fires to build and evaluate Support Vector Machine (SVM) models for classification.

Objective

The goal is to apply different SVM kernels (linear, polynomial, and radial basis function (RBF)) to classify forest fire occurrences and determine which kernel performs best based on accuracy metrics.

Data Description

Metadata for dataset forestfires.csv :

Columns:

month: Categorical ("jan" to "dec")
day: Categorical ("mon" to "sun")
FFMC: Numeric (Fine Fuel Moisture Code, range typically 18.7 to 96.20)
DMC: Numeric (Duff Moisture Code, range typically 1.1 to 291.3)
DC: Numeric (Drought Code, range typically 7.9 to 860.6)
ISI: Numeric (Initial Spread Index, range typically 0.0 to 56.10)
temp: Numeric (Temperature in Celsius, range typically 2.2 to 33.30)
RH: Numeric (Relative Humidity, range typically 15.0 to 100%)
wind: Numeric (Wind Speed in km/h, range typically 0.40 to 9.40)
rain: Numeric (Rainfall in mm/m2, range typically 0.0 to 6.4)
area: Numeric (Area burned in hectares, continuous variable; 0.00 to 1090.8)
dayfri, daymon, daysat, daysun, daythu, daytue, daywed: Binary (One-hot encoded days of the week)
monthapr, monthaug, monthdec, monthfeb, monthjan, monthjul, monthjun, monthmar, monthmay, monthnov, monthoct, monthsep: Binary (One-hot encoded months)
size_category: Categorical (Text, e.g., 'small', 'large')
 

Dataset Link:

https://drive.google.com/drive/folders/1lmoi1guyk4Stvvh_yRykq3c7Q3Ffe9Y3?usp=sharing


Questions:

Q1) Write a Python code snippet to load the dataset forestfires.csv from a given path and display the first 5 rows of the dataset.  (1 M)
Q2) Drop the unnecessary columns and apply min-max normalization to scale the feature columns (1.5 M)

Q3) Write the code to split the dataset into training and testing sets with a 75-25 split. Hint:  Consider target as size_category (1 M)

Q4) Write the code to train  SVM model with kernels (Linear, polynomial and RBF) and compare the performance. Also, calculate the accuracy scores for each kernel? (4 M)

Q5) Write a summary of which kernel performed best on test data and why. State conclusion properly. (1.5M)
