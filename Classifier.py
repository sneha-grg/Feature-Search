
class Classifier:
    # Constructor
    def __init__(self):
        self.training_data = None # array of training feature vectors
        self.training_labels = None # array of traning class labels
    
    # Train method does not output anything
    def Train(self, training_data, training_labels):
        #stores training data and training labels
        self.training_data = training_data
        self.training_labels = training_labels

    # Test method : the output is the predicted class label
    def Test(self, test_instance):

        # Add more code here
        return test_instance



# Euclidean distance measure to compute the distance between two points in an n-dimensional space (n is the number of features)

# New object/instance
# nn_classifier = Classifier()