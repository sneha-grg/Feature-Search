from DataHandler import load_data, normalize_data
from Classifier import NNClassifier
from Validator import Validator


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
    print("Welcome to Sneha's and Anna's Feature Selection Algorithm.\n")
    
    # Load and normalize data
    filename = int(input("Please enter 1 for small-test-dataset.txt, 2 for large-test-dataset.txt, and 3 for titanic-clean.txt: "))
    if filename == 1:
        data = load_data('small-test-dataset.txt')
        data = normalize_data(data)
    elif filename == 2:
        data = load_data('large-test-dataset.txt')
        data = normalize_data(data)
    elif filename == 3:
        data = load_data('titanic-clean.txt')
        data = normalize_data(data)
    else:
        print("Invalid input. Exiting.")
        return

    print("\n")
    print("Type the number of algorithm you want to run.\n")

    print("\t1. Forward Selection")
    print("\t2. Backward Elimination")
    print("\t3. Our Special Algorithm \n\n")

    num_of_algo = input("\t\t\t\t\t\t\t\t")  # lol

    num_features = len(data[0][1])
    instances = len(data)
    print(f"\nThis dataset has {num_features} features (not including the class attribute), with {instances} instances\n")

    print("Please wait while I normalize the data... Done!\n")

    feature_subset = list(range(1, len(data[0][1]) + 1))
    evaluated = evaluation_function(feature_subset, data)

    print(f"Running nearest neighbor with no features (default rate), using leaving-one-out evaluation, I get an accuracy of {str(evaluated)}\n\n") 



    if num_of_algo == '1':
        forward_selection(feature_subset, data)
    elif num_of_algo == '2':
        back_elimination(feature_subset, data)
    else:
        print("Code not implemented yet.")

    """
    - Group: Sneha Gurung - sguru004 - Session 23, Anna Lee - alee531 - Session 23
    - DatasetID: the best feature output
    - Small Dataset Results:
            - Forward: Feature Subset: {3, 5}, Acc: 92%
            - Backward: Feature Subset: {2, 3, 4, 5}, Acc: 83%
    - Large Dataset Results:
            - Forward: Feature Subset: {1, 27}, Acc: 95.5%
            - Backward: Feature Subset: {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
            15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
            33, 34, 35, 36, 37, 38, 39, 40}, Acc:71.1%
    - Titanic Dataset Results:
            - Forward: Feature Subset: {2}, Acc: 78%
            - Backward: Feature Subset: {2}, Acc: 78%
    """


if __name__ == "__main__":
    main()