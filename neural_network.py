import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid activation function
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Define the neural network class
class NeuralNetwork:
    def __init__(self, x, y, batch_size, learning_rate):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)
        self.batch_size = batch_size
        self.learning_rate = learning_rate

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output))) / self.batch_size
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1))) / self.batch_size

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += self.learning_rate * d_weights1
        self.weights2 += self.learning_rate * d_weights2

# Generate a more comprehensive random dataset for training
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1],
              [0,0,0],
              [0,1,0],
              [1,0,0],
              [1,1,0]])
y = np.array([[0],[1],[1],[0],[0],[0],[0],[0]])

# Normalize the input data
X = (X - np.min(X)) / (np.max(X) - np.min(X))

# Create a neural network with 3 input neurons, 4 hidden neurons, and 1 output neuron
batch_size = 4
learning_rate = 0.1
nn = NeuralNetwork(X, y, batch_size, learning_rate)

# Train the neural network for 10000 iterations
for i in range(10000):
    for j in range(0, len(X), batch_size):
        x_batch = X[j:j+batch_size]
        y_batch = y[j:j+batch_size]
        nn.feedforward()
        nn.backprop()

# Calculate the final output and accuracy of the model
nn.feedforward()
final_output = nn.output
accuracy = np.mean(np.round(final_output) == y) * 100

print("Final Output:")
print(final_output)
print("Accuracy: {:.2f}%".format(accuracy))
