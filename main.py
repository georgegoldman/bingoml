import os
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score, hamming_loss

# Prepare data
input_dir = '/home/goldman/Documents/data_set/TrashType_Image_Dataset'
categories = ['glass', 'metal', 'paper', 'plastic']

data = []
labels = []

for category in categories:
    category_dir = os.path.join(input_dir, category)
    for file in os.listdir(category_dir):
        img_path = os.path.join(category_dir, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())

        # Assuming filenames represent multi-labels, e.g., "glass_plastic.jpg" 
        image_labels = [idx for idx, cat in enumerate(categories) if cat in file]
        labels.append(image_labels)

data = np.array(data)
labels = np.array(labels)

# Convert labels to multi-label format
mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(labels)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True)

# Define the classifier
classifier = MultiOutputClassifier(SVC())

# Train classifier
classifier.fit(x_train, y_train)

# Test performance
y_prediction = classifier.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_prediction)
hamming = hamming_loss(y_test, y_prediction)

print(f'Accuracy: {accuracy * 100}%')
print(f'Hamming Loss: {hamming}')

# Save model
with open('./model_multilabel.p', 'wb') as model_file:
    pickle.dump(classifier, model_file)
