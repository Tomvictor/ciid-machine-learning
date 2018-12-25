import pandas as pd
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Dense
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


print("create model")
model_mc = Sequential()
print("get number of columns in training data")
n_cols = train_X.shape[1]
print(n_cols)

print("add model layers")

#add model layers
model_mc.add(Dense(1000, activation='relu', input_shape=(n_cols,)))
model_mc.add(Dense(1000, activation='relu'))
model_mc.add(Dense(1000, activation='relu'))
model_mc.add(Dense(1))

#compile model using mse as a measure of model performance
model_mc.compile(optimizer='adam', loss='mean_squared_error')
#train model
print("set early stopping monitor so the model stops training when it won't improve anymore")
early_stopping_monitor = EarlyStopping(patience=3)
# model_mc.fit(train_X, train_y, validation_split=0.2, epochs=50, callbacks=[early_stopping_monitor])
model_mc.fit(train_X, train_y, validation_split=0.2, epochs=100)


print("training completed...")
print("testing...")

test_df = pd.read_csv('test.csv')
print("test data loaded")
testX = test_df.drop(columns=['wage_per_hour'])
print("TEST x")
print(testX.head())


test_y_predictions = model_mc.predict(testX)

print(test_y_predictions)


#Save the model
# serialize model to JSON
model_json = model_mc.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model_mc.save_weights("model.h5")
print("Saved model to disk")