import numpy as np
import random
from pyspark.sql.functions import size

def linear_regression(data, learning_rate, num_iterations):
  """
  Performs linear regression using MapReduce and Gradient Descent for N features

  Args:
      data: RDD containing data points with features and target variable
      learning_rate: Learning rate for gradient descent
      num_iterations: Number of iterations for gradient descent

  Returns:
      A tuple containing the final weights and the cost history
  """
  num_features = len(data.first()[0])
  # Initialize weights with zeros
  weights = [random.random() for _ in range(num_features)]

  cost_history = []
  for i in range(num_iterations):
    
    # Map step: Calculate gradient for each data point
    gradient_df = data.map(lambda point: calculate_gradient(point, weights, num_features))

    # Reduce step: Aggregate gradients to get overall update
    total_gradient = gradient_df.reduce(lambda g1, g2: np.add(g1, g2))

    # Update weights using learning rate
    # w = w - lr * gradient
    weights = np.subtract(weights, np.multiply(learning_rate/data.count(), total_gradient))
    
    # Calculate cost for this iteration
    cost = calculate_cost(data, weights)

    cost_history.append(cost)
    if i % 10 == 0:
        print("Iteration %d => Cost: %f" % (i, cost))

    return weights, cost_history

  def calculate_gradient(point, weights):
    """
    Calculates the gradient for a single data point
  
    Args:
        point: A tuple containing features and target variable [ex : ([1, 2,4,5,6], 1)]
        weights: Current weights for the model
  
    Returns:
        A list containing gradients for each weight
    """
    features, target = point
    hypothesis = np.dot(weights, features)
    error = np.subtract(hypothesis, target)
    gradients_w = np.multiply(error, features)
    return gradients_w

def calculate_cost(data, weights):
    """
    Calculates the mean squared error for the model

    Args:
        data: RDD containing data points
        weights: Current weights for the model

    Returns:
        The mean squared error
    """
    squared_errors = data.map(lambda point: (point[1] - predict(point, weights))**2)
    reduced_squared_errors = squared_errors.reduce(lambda x, y: x + y)
    return reduced_squared_errors / (2 * data.count())

def predict(point, weights):
  """
  Predicts the target variable for a data point

  Args:
      point: A tuple containing features
      weights: Current weights for the model

  Returns:
      The predicted target variable
  """
  features , _ = point
  return np.dot(weights, features)

# Example usage

# Assuming your data is loaded into an RDD named 'data'
# Each element in 'data' should be a tuple of (features, target)

#hyperparameters
# learning_rate = 0.0001
# num_iterations = 100


# weights, cost_history = linear_regression(data, learning_rate=learning_rate, num_iterations=num_iterations, num_features=20)

# print("Final weights:", weights)
# print("Cost history:", cost_history)

