import random

def evaluation_function(feature_subset): # feature subset is a node in a graph
    return random.uniform(0.0, 100.0)

def forward_selection(features):
    feature_set = []
    best_overall_score = evaluation_function(feature_set)
    hold_overall_set = []
    print("Beginning Search.\n")

    # while loop remains looping until set of features is greater than given parameter features
    while len(feature_set) < len(features):
        best_feature = None # will hold the best feature
        best_feature_score = -1 # holds the lowest value so the best score can be added
        
        # testing each feature that has not been selected
        for f in features:
            if f not in feature_set:
                new_set = feature_set + [f] # 
                score = evaluation_function(new_set) # random score using evaluation function

                print(f"\t Using feature(s) {new_set} accuracy is {score:.1f}%")

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
                print(f"\nFeature set {feature_set} was best, accuracry is {best_feature_score:.1f}%")
            elif best_feature_score < best_overall_score:
                print("\n(Warning, Accuracy was decreased !)")
                break
        else:
            break

    print(f"\nFinished search!! The best feature subset is {hold_overall_set}, which has an accuracry of {best_overall_score:.1f}%")
    
    return feature_set


    
def main():
    print("Welcome to Sneha's and Anna's Feature Selection Algorithm.\n")
    num_of_features = int(input("Please enter total number of features: "))
    print("\n")
    print("Type the number of alogorithm you want to run.\n")
    
    print("\t 1. Forward Selection")
    print("\t 2. Backward Elimination")
    print("\t 3. Our Special Alogirthm \n\n")

    num_of_algo = input("\t\t\t\t\t\t\t\t") # lol

    base_accuracy = evaluation_function([])
    print(f"\nUsing no features and 'random' evaluation, I get an accuracy of {base_accuracy:.1f} %\n")

    myset = []
    for i in range(1, num_of_features + 1):
        myset.append(i)
        print(i)

    if num_of_algo == '1':
        forward_selection(myset)
    else:
        print("Code not implemented yet.") # add backward elimination function


if __name__ == "__main__":
    main()