
class NNClassifier:
    # Constructor
    def __init__(self):
        self.training_data = [] # array of training feature vectors
        self.training_labels = [] # array of traning class labels
    
    # Train method does not output anything
    def Train(self, training_data, training_labels):
        #stores training data and training labels
        self.training_data = training_data
        self.training_labels = training_labels

    # Test method : the output is the predicted class label
    def Test(self, test_instance):
        # we're trying to find the class label of the test instance parameter
        # test_instance is an array of test instance features
        # return predicted class label

        #initialize a min distance 
        minDistance = float('inf')
        predicted_class_label = None

        for i in range(len(self.training_data)):
            distance = 0
            for j in range(len(test_instance)):
                distance += (self.training_data[i][j] - test_instance[j]) ** 2
            distance = distance ** 0.5 # this is the square root

            if distance < minDistance:
                minDistance = distance
                predicted_class_label = self.training_labels[i]
        
        return predicted_class_label



# Euclidean distance measure to compute the distance between two points in an n-dimensional space (n is the number of features)