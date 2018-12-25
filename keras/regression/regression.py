import pandas as pd
train_df = pd.read_csv('hourly_wages_data.csv')


# print(train_df)
train_df.head()
print(train_df.head())
print("data loaded")
train_X = train_df.drop(columns=['wage_per_hour'])
print("train x")
print(train_X.head())
print("create a dataframe with only the target column")
train_y = train_df[['wage_per_hour']]
print("view dataframe")
print(train_y.head())

print("Next, we have to build the model")

from keras.models import Sequential
from keras.layers import Dense

print("create model")
model = Sequential()

print("get number of columns in training data")
n_cols = train_X.shape[1]
print(n_cols)

print("add model layers")
model.add(Dense(10, activation='relu', input_shape=(n_cols,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

print("compile model using mse as a measure of model performance....")
model.compile(optimizer='adam', loss='mean_squared_error')


from keras.callbacks import EarlyStopping
print("set early stopping monitor so the model stops training when it won't improve anymore")
early_stopping_monitor = EarlyStopping(patience=3)
print("train model")
model.fit(train_X, train_y, validation_split=0.2, epochs=30, callbacks=[early_stopping_monitor])


print("training completed...")
print("testing...")

test_df = pd.read_csv('test.csv')
print("test data loaded")
testX = test_df.drop(columns=['wage_per_hour'])
print("TEST x")
print(testX.head())


test_y_predictions = model.predict(testX)

print(test_y_predictions)