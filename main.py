from DataHandler import load_data, normalize_data
from Classifier import NNClassifier
from Validator import Validator
import time, random

def evaluation_function(feature_subset, data):
    # this is where we call the Validator that evaluates the accuracy of the NN classifier
    classifier = NNClassifier()
    validator = Validator(classifier, data, feature_subset)
    accuracy = validator.calculate_classifier_accuracy()
    return accuracy * 100  # Convert to percentage

def forward_selection(features, data):
    feature_set = []
    best_overall_score = 0.0
    hold_overall_set = []
    print("Beginning Search.\n")

    # while loop remains looping until set of features is greater than given parameter features
    while len(feature_set) < len(features):
        best_feature = None # will hold the best feature
        best_feature_score = -1 # holds the lowest value so the best score can be added
        
        # testing each feature that has not been selected
        for f in features:
            if f not in feature_set:
                new_set = feature_set + [f]
                score = evaluation_function(new_set, data) # evaluation function calls Validator class now

                print(f"\tUsing feature(s) {set(new_set)} accuracy is {score:.1f}%")

                if score > best_feature_score:
                    best_feature_score = score
                    best_feature = f

        # stop search if adding a feature doesn't improve the score
        if best_feature is not None:
            # append for add and pop for remove
            feature_set.append(best_feature)
            if best_feature_score > best_overall_score:
                best_overall_score = best_feature_score
                hold_overall_set = feature_set.copy()
                print(f"\nFeature set {set(feature_set)} was best, accuracy is {best_feature_score:.1f}%")
            elif best_feature_score < best_overall_score:
                print("\n(Warning, Accuracy was decreased !)")
                break
        else:
            break

    print(f"\nFinished search!! The best feature subset is {set(hold_overall_set)}, which has an accuracy of {best_overall_score:.1f}%\n")
    return hold_overall_set


def back_elimination(features, data):
    feature_set = features.copy()
    best_overall_score = evaluation_function(feature_set, data)
    hold_overall_set = feature_set.copy()
    print("Beginning Search.\n")
    print(f"Initial feature set {set(hold_overall_set)} has an accuracy of {best_overall_score:.1f}%\n")

    # loop until no more features
    while len(feature_set) > 0:
        #tracks the subset with the highest accuracy
        feature_to_remove = None
        best_score = -float('inf')
        best_subset = None

        # iterate over current subset
        for f in feature_set:
            subset = feature_set.copy()
            subset.remove(f)
            score = evaluation_function(subset, data)
            print(f"\tUsing feature(s) {set(subset)} accuracy is {score:.1f}%")

            #keeps track of the best_score of current subset
            if score > best_score:
                best_score = score
                feature_to_remove = f
                best_subset = subset.copy()

         # if the best score from current iteration is better than the overal best_overall_score
        if best_score > best_overall_score:
            #update best_overall_score
            best_overall_score = best_score
            feature_set.remove(feature_to_remove)
            hold_overall_set = best_subset.copy()
            print(f"\nFeature set {set(hold_overall_set)} was best, accuracy is {best_overall_score:.1f}%\n")
        else:
            # no improvement from current iteration, means algo should stop here
            print("\n(Warning, Accuracy has decreased! Stopping elimination.)\n")
            break

    print(f"Finished search!! The best feature subset is {set(hold_overall_set)}, which has an accuracy of {best_overall_score:.1f}%\n")
    return hold_overall_set


def main():
    print("Welcome to the Feature Selection and Testing Algorithm.\n")
    start_time = time.time()

    # two choices of data sets
    print("Please Select Which Dataset to Use: (Input number)")
    print("1. Small Dataset")
    print("2. Large Dataset")
    filename = int(input("Choice: "))

    if filename == 1:
        parse_dataset_start = time.time()
        data = load_data('small-test-dataset.txt')
        parse_dataset_end = time.time()
        normalization_start = time.time()
        data = normalize_data(data)
        normalization_end = time.time()
        print("Run through entire dataset or one given feature?") # gives options to run all data set or one feature
        print("1. Entire dataset")
        print("2. Feature {3, 5, 7}")
        feature_choice = input("Choice: ")
        if feature_choice == "2":
            feature_subset = [3, 5, 7]  # Use features 3, 5, and 7
        else:
            feature_subset = list(range(1, len(data[0][1]) + 1))  # Use all features
    elif filename == 2:
        parse_dataset_start = time.time()
        data = load_data('large-test-dataset.txt')
        parse_dataset_end = time.time()
        normalization_start = time.time()
        data = normalize_data(data)
        normalization_end = time.time()
        print("Run through entire dataset or one given feature?") # gives options to run all data set or one feature
        print("1. Entire dataset")
        print("2. Feature {1, 15, 27}")
        feature_choice = input("Choice: ")
        if feature_choice == "2":
            feature_subset = [1, 15, 27]
        else:
            feature_subset = list(range(1, len(data[0][1]) + 1))  # Use all features

    print(f"\nLoaded and normalized data from {filename}.\n")

    validation_start = time.time()

    classifier = NNClassifier()
    validator = Validator(classifier, data, feature_subset)
    # calculate accuracy
    accuracy = validator.calculate_classifier_accuracy()
    
    print("\nProcessing Leave-One-Out Validation...\n")
    results = []
    correct = 0

    for i in range(len(data)):
        actual_label = data[i][0]
        feature_vector = data[i][1]

        # test_features
        test_features = []
        for f in feature_subset:
            test_features.append(feature_vector[f - 1])

        # training data without test instance
        training_data = []
        for j in range(len(data)):
            if j != i:  # add everything except test instance
                training_data.append(data[j])

        # labels and features
        training_labels = []
        training_features = []
        for instance in training_data:
            training_labels.append(instance[0]) #add labels
            features = []
            for f in feature_subset:
                features.append(instance[1][f - 1])   #add features
            training_features.append(features)

        #train classifier
        classifier.Train(training_features, training_labels)

        #prediction of classifier
        predicted_label = classifier.Test(test_features)

        # check if prediction is right
        is_correct = predicted_label == actual_label
        if is_correct:
            correct += 1

        # append to results array
        results.append((i + 1, predicted_label, actual_label, is_correct))

    validation_end = time.time()
    # formating the output of our code
    print("\nResults:\n")
    for instance_id, predicted, actual, is_correct in results:
        correctness = "correct" if is_correct else "wrong"
        print(
            f"Instance:{instance_id:3d}, Predicted: {predicted:1d}, Actual: {actual:1d} ({correctness})"
        )

    print(f"\nResults: {correct} / {len(data)}")
    print(f"Accuracy: {accuracy * 100:.1f}%\n")

    # Calculate and display timings
    print("\nTime Spent on Each Step:")
    print(f"Dataset Parsing: {parse_dataset_end - parse_dataset_start:.4f} seconds")
    print(f"Normalization: {normalization_end - normalization_start:.4f} seconds")
    print(f"Leave-One-Out Validation: {validation_end - validation_start:.4f} seconds")
    print(f"Total Time: {time.time() - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()