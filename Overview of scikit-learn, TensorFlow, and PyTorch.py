from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import torch
import torch.nn as nn
import torch.optim as optim

# Scikit-learn Linear Regression
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=10)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2)
model_reg = LinearRegression()
model_reg.fit(X_train_reg, y_train_reg)
y_pred_reg = model_reg.predict(X_test_reg)
print("Scikit-learn Predictions:", y_pred_reg[:5])

# TensorFlow Sequential Model
X_tf = np.array([[10], [1], [2], [3]], dtype=np.float32)
Y_tf = np.array([[0], [1], [2], [3]], dtype=np.float32)
model_tf = Sequential([
    Dense(10, activation='relu', input_shape=(1,)),
    Dense(1)
])
model_tf.compile(optimizer='adam', loss='mean_squared_error')
model_tf.fit(X_tf, Y_tf, epochs=50, verbose=0)
print("TensorFlow Predictions:", model_tf.predict(np.array([[4], [5]], dtype=np.float32)))

# PyTorch Linear Model
X_pt = torch.tensor([[1.0], [2.0], [3.0]])
y_pt = torch.tensor([[2.0], [4.0], [6.0]])
model_pt = nn.Linear(1, 1)
criterion_pt = nn.MSELoss()
optimizer_pt = optim.SGD(model_pt.parameters(), lr=0.01)
for epoch in range(100):
    optimizer_pt.zero_grad()
    output_pt = model_pt(X_pt)
    loss_pt = criterion_pt(output_pt, y_pt)
    loss_pt.backward()
    optimizer_pt.step() # Added missing optimizer.step()
print("PyTorch model trained.") # Added print statement to indicate successful training
print(model_pt(torch.tensor([[4.0]])))
