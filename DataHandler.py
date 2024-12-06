def load_data(filename):
    # opens given file name and reads it

    data = [] # empty list to store information from file
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split() # removes whitespace and splits line with list of strings
            class_label = int(float(parts[0]))  # Convert the class label to int
            features = []
            for x in parts[1:]:  # parts[1:] is everything after the first column
                features.append(float(x))
            data.append((class_label, features)) # appends a tuple

    return data

def normalize_data(data):
    # this function sets the dataset to have values between 0 and 1

    if not data:  # returns an empty list if there's nothing in the list
        return data

    num_features = len(data[0][1]) # holds the length of the list of features of the first entry
    min_vals = [float('inf')] * num_features # each index stores the min
    max_vals = [float('-inf')] * num_features # each index stores the max

    # Find min and max for each feature
    for _, features in data:  # _ ignores the class label and only focuses on features
        for i, value in enumerate(features): # iterates over each feature value and its index i in features list
            if value < min_vals[i]:
                min_vals[i] = value
            if value > max_vals[i]:
                max_vals[i] = value

    # Normalize features
    normalized_data = []
    for class_label, features in data:
        normalized_features = []
        for i, value in enumerate(features):
            if max_vals[i] - min_vals[i] == 0:
                normalized = 0.0  
            else:
                normalized = (value - min_vals[i]) / (max_vals[i] - min_vals[i]) #normalization formula
            normalized_features.append(normalized)
        normalized_data.append((class_label, normalized_features))

    return normalized_data # all features are either 0 or 1



