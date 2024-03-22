import numpy as np

inputs = np.array(([2,9], [1,5], [3,6]), dtype=float)
targets = np.array(([92],[85],[89]), dtype=float)

inputs = inputs/np.amax(inputs, axis=0)
targets = targets/100

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def derivative_sigmoid(x):
    return x * (1 - x)

epoch = 5000
learning_rate = 0.1
input_layer_neurons = 2
hidden_layer_neurons = 3
output_layer_neurons = 1

weights_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
weights_out = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))
bias_out = np.random.uniform(size=(1, output_layer_neurons))

for i in range(epoch):
    # Forward
    hidden_input = np.dot(inputs, weights_hidden)
    hidden_input+=bias_hidden
    hidden_output=sigmoid(hidden_input)

    output_input = np.dot(hidden_output, weights_out)
    output_input+=bias_out
    predicted_output = sigmoid(output_input)

    # Backward
    error_output = targets - predicted_output
    output_derivative = derivative_sigmoid(predicted_output)
    delta_output = error_output * output_derivative

    error_hidden = delta_output.dot(weights_out.T)
    hidden_derivative = derivative_sigmoid(hidden_output)
    delta_hidden = error_hidden * hidden_derivative

    # update weights and biases
    weights_out += hidden_output.T.dot(delta_output) * learning_rate
    weights_hidden += inputs.T.dot(delta_hidden) * learning_rate
    bias_out += np.sum(delta_output, axis=0) * learning_rate
    bias_hidden += np.sum(delta_hidden, axis=0) * learning_rate

print("Input:\n", inputs)
print("Actual Output:\n", targets)
print("Predicted Output:\n", predicted_output)