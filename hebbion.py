import numpy as np

# ANSI color codes for formatted output
class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Input Validation
def get_input(prompt, dtype=float):
    while True:
        try:
            return dtype(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function
def main():
    learning_rate = get_input("\nEnter learning constant C: ")
    num_datasets = get_input("Enter number of datasets: ", int)
    
    # Initial weight
    weights = [np.array(list(map(float, input("Enter initial weights W1: ").split()))).reshape(-1, 1)]
    
    # Input vectors
    inputs = []
    for i in range(num_datasets):
        vector = np.array(list(map(float, input(f"Enter values for X{i+1}: ").split()))).reshape(-1, 1)
        inputs.append(vector)
    
    print(f"\n{bcolors.FAIL}{bcolors.UNDERLINE}Solution:{bcolors.ENDC}\n")

    # Weight Update Loop
    for i, input_vector in enumerate(inputs):
        net = np.dot(weights[-1].transpose(), input_vector)
        output = 1 if net > 0 else -1 if net < 0 else 0
        
        delta_weight = learning_rate * output * input_vector
        new_weight = weights[-1] + delta_weight
        weights.append(new_weight)
        
        print(f"{bcolors.FAIL}{bcolors.BOLD}W{i+2}{bcolors.ENDC} is:\n{new_weight}\n")

if __name__ == "__main__":
    main()
