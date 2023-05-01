import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_virtual_device_configuration(
        gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)])

train_data = pd.read_csv('CUST_TRAIN.csv')
test_data = pd.read_csv('CUST_TEST.csv')

features = ['Region', 'BorrowSize', 'MaritalStatus', 'CreditScore']

X_train = pd.get_dummies(train_data[features])
y_train = train_data['PreferredScore']
X_test = pd.get_dummies(test_data[features])
y_test = test_data['PreferredScore']

input_dim = len(X_train.columns)

neurons = 64
epochs = 100
model = Sequential()

model.add(Dense(neurons, input_dim=input_dim, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=epochs, verbose=1, validation_split=0.33)
predictions = model.predict(X_test)

predictions = (predictions > 0.5)*1

output = pd.DataFrame(
    {'CustomerID': test_data.CustomerID,
     'PreferredScore': predictions.flatten()})
output.to_csv('preferred.csv', index = False)

scores = model.evaluate(X_test, y_test, verbose=0)
print(scores)



