from Classifier import NNClassifier
from DataHandler import load_data, normalize_data

class Validator:
    def __init__(self, classifier, data, feature_subset):
        self.classifier = classifier
        self.data = data
        self.feature_subset = feature_subset

    def calculate_classifier_accuracy(self):
        # leaves out ith instance so that it can perform k-cross validation
        correct = 0
        total = len(self.data)

        for i in range(total):
           
            # isolates ith instance
            training_data = []
            for idx, instance in enumerate(self.data):
                if idx != i:
                    training_data.append(instance)

            test_instance = self.data[i]

            # makes it so that the labels are separate from features
            training_labels = []
            for instance in training_data:
                training_labels.append(instance[0])


            #isolating features
            training_features = []
            for instance in training_data:
                selected_features = self._select_features(instance[1])
                training_features.append(selected_features)

            
            #isolate test instance features
            test_features = self._select_features(test_instance[1])

            #calls upon Train function from the classifier class to train the classifier using training_features and training_labels
            self.classifier.Train(training_features, training_labels)

            # tests classifier 
            predicted_label = self.classifier.Test(test_features)

            # Checks prediction
            if predicted_label == test_instance[0]:
                correct += 1

        accuracy = correct / total
        return accuracy

    def _select_features(self, feature_vector):
        # gets all the features, starts from 2nd column
        selected_features = []
        for f in self.feature_subset:
            selected_features.append(feature_vector[f - 1])
        return selected_features
    
