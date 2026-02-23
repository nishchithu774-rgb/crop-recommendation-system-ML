import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Input values
X = data[['N','P','K','temp','humidity']]

# Output values
y = data['crop']

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X,y)

# Save Model
pickle.dump(model, open("crop_model.pkl","wb"))

print("Model Trained Successfully")