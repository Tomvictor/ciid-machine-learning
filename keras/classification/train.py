import pandas as pd
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

print("loading datasets..")
train_df_2 = pd.read_csv('diabetes_data.csv')
print("data loaded.")
print(train_df_2.head())


print("create a dataframe with all training data except the target column")
train_X_2 = train_df_2.drop(columns=['diabetes'])
print("dataset -> x")
print(train_X_2.head())

print("one-hot encode target column")
train_y_2 = to_categorical(train_df_2.diabetes)

print("check that target column has been converted")
print(train_y_2[0:5])

print("create model")
model_2 = Sequential()

print("get number of columns in training data")
n_cols_2 = train_X_2.shape[1]
print(n_cols_2)

print("add layers to model")
model_2.add(Dense(250, activation='relu', input_shape=(n_cols_2,)))
model_2.add(Dense(250, activation='relu'))
model_2.add(Dense(250, activation='relu'))
model_2.add(Dense(2, activation='softmax'))

print("compile model using accuracy to measure model performance")
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


print("train model")
# model_2.fit(train_X_2, train_y_2, epochs=30, validation_split=0.2, callbacks=[early_stopping_monitor])
model_2.fit(train_X_2, train_y_2, epochs=30, validation_split=0.2)
print("traingin completed")


print("predict output...")
test_df = pd.read_csv('input_predit.csv')
print("test data loaded")
testX = test_df.drop(columns=['diabetes'])
print("TEST x")
print(testX.head())


y_predictions = model_2.predict(testX)

print(y_predictions)