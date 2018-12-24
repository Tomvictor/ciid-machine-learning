from keras.models import Sequential
from keras.layers import Dense, Activation

print("choosing model")
model = Sequential()
print("adding layers..")
model.add(Dense(32, activation='relu', input_dim=100))
print("adding layers..")
model.add(Dense(1, activation='sigmoid'))
print("setting learning method")
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
print("generate dummy data..")
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

print("Train the model, iterating on the data in batches of 32 samples")
# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

print("training completed.....")