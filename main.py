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


    myset = [1, 2, 3, 4]
    if num_of_algo == '1':
        forward_selection(myset)
    else:
        print("Code not implemented yet.") # add backward elimination function


if __name__ == "__main__":
    main()