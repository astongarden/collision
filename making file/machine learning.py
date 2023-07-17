import numpy as np
import tensorflow as tf

# Generate random training data
np.random.seed(0)
num_samples = 1000
input_data = np.random.rand(num_samples, 2)  # Random values between 0 and 1
output_data = np.zeros((num_samples, 1))

# Define the collision function
def collision_function(x, y):
    # Define the collision condition (example: x + y > 1)
    return np.array(x + y > 1, dtype=int)

# Create labels for training data
for i in range(num_samples):
    output_data[i] = collision_function(input_data[i][0], input_data[i][1])

# Define the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(input_data, output_data, epochs=10, batch_size=32)

# Test the model
test_input = np.array([[0.3, 0.7], [0.8, 0.2]])
predictions = model.predict(test_input)

print("Predictions:")
for i in range(len(test_input)):
    print("Input:", test_input[i])
    print("Collision Probability:", predictions[i][0])
    print()
