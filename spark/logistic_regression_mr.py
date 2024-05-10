import numpy as np
from pyspark.sql.functions import size


class MulticlassLogisticRegression:

    def __init__(self, learning_rate, max_iter, num_classes):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.num_classes = num_classes
        self.classifiers = [LogisticRegression(learning_rate, max_iter) for _ in range(num_classes)]

    def fit(self, data):
        for i, classifier in enumerate(self.classifiers):
            print(f"Fitting classifier for class {i}")
            binary_labels = data.map(lambda point: (point[0], 1 if point[1] == i else 0))
            classifier.fit(binary_labels)

    def predict(self, point):
        probabilities = [classifier.predict(point) for classifier in self.classifiers]
        return np.argmax(probabilities)


class LogisticRegression:

    def __init__(self, learning_rate, max_iter):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None

    def stable_softmax(self, z):
        max_z = np.max(z)
        exp_z = np.exp(z - max_z)
        return exp_z / np.sum(exp_z, axis=0)

    def calculate_gradient(self, point, weights):
        features, target = point
        z = np.dot(weights, features)
        predicted_prob = self.stable_softmax(z)
        error = predicted_prob - target
        gradients_w = np.dot(features.reshape(-1, 1), error.reshape(1, -1))
        return gradients_w

    def calculate_cost(self, data, weights):
        logistic_loss = data.map(lambda point:
                                  -np.sum(point[1] * np.log(self.stable_softmax(np.dot(weights, point[0])) + 1e-8)))

        return logistic_loss.reduce(lambda x, y: x + y) / data.count()

    def predict(self, point):
        if self.weights is None:
            raise ValueError("Model not fitted yet!")
        features, _ = point
        z = np.dot(self.weights, features)
        predicted_prob = self.stable_softmax(z)
        return predicted_prob

    def fit(self, data):
        num_features = len(data.first()[0])
        if self.weights is None:
            self.weights = np.zeros((num_features, self.num_classes))

        cost_history = []
        tolerance = 1e-4

        for iter_num in range(self.max_iter):
            gradient_df = data.map(lambda point: self.calculate_gradient(point, self.weights))
            total_gradient = gradient_df.reduce(lambda g1, g2: np.add(g1, g2))
            self.weights = np.subtract(self.weights, np.multiply(self.learning_rate, total_gradient))
            cost = self.calculate_cost(data, self.weights)
            cost_history.append(cost)

            if iter_num > 0 and abs(cost_history[-1] - cost_history[-2]) < tolerance:
                print("Cost change below tolerance. Stopping early at iteration", iter_num)
                break

            print("Iteration %d => Cost: %f" % (iter_num, cost))

        return cost_history
