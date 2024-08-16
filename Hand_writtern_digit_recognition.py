import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
data = keras.datasets.mnist.load_data()

(X_train, Y_train), (X_test, Y_test) = keras.datasets.mnist.load_data()

# Scaling the values from 0 to 1
X_train = X_train / 255
X_test = X_test / 255

# X_train.shape = (60000,28,28) -> same format, should be flattened. So below line

X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)

'''Now the shape of X_train and Y_train will be (60000,784) and (10000,784)
and it became 1-d array from 2-d array and this is called as flattening'''

# As hidden layer increases, Accuracy increases too.

model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(100, activation='sigmoid'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    # as our output is from 0-9 so we use 'sparse'
    loss='sparse_categorical_crossentropy',
    # metrics is my accuracy while the model is compiling
    metrics=['accuracy']
)

# fit where the training actually happens
model.fit(X_train,Y_train, epochs=5)

train_loss, train_accuracy = model.evaluate(X_train, Y_train)
train_accuracy = np.ceil(100*train_accuracy)
print(f'Training Accuracy :{train_accuracy} %')

test_loss, test_accuracy = model.evaluate(X_test, Y_test)
test_accuracy = np.ceil(100*test_accuracy)
print(f'Test Accuracy :{test_accuracy} %')


plt.matshow(X_train[9])
plt.xlabel(Y_train[9])
plt.xticks([])
plt.yticks([])
plt.show()

y_predicted = model.predict(X_train)
print(y_predicted[9])
# the above print statement will print the array of outputs like the total probability of the 10 classes
# we need to print the index of the maximum value

# this will find the maximum value in the array of output and prints the index of that value
print(np.argmax(y_predicted[9]))


def plot_images(images, label_true, num_images=5):
    plt.figure(figsize=(10, 6))
    for i in range(num_images):
        plt.subplot(1, num_images, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid = False
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(label_true[i])
    plt.show()

num_of_images_to_show=5

# we can give length of the array or the array itself to np.random.choice
random_indices = np.random.choice(len(X_test), num_of_images_to_show)

sample_images = X_test[random_indices]
sample_labels = Y_test[random_indices]

plot_images(sample_images, sample_labels)
