class Validator:
    def __init__(self, feature_subset, classifier, dataset):
        self.feature_set = feature_subset
        self.classifier = classifier # NN classifier
        self.dataset = dataset # all the training data 

    def calculate_classifier_accuracry(self, feature_subset):
        pass
        # Return the accuracy of the classifier on the given dataset



# In this part, however, we are not concerned with feature search. We just want to calculate
# the accuracy of the NN-classifier given a specific feature subset (as input).
