import numpy as np
import sys


def topsis(data, weights, impacts):
    data = data.astype(float)
    normalized_data = data / np.sqrt(np.sum(data ** 2, axis=0))
    normalized_data = np.where(normalized_data == 0, 1e-9, normalized_data)
    weighted_data = normalized_data * weights
    weighted_data = np.where(weighted_data == 0, 1e-9, weighted_data)
    ideal_solution = np.where(impacts == 1, np.max(weighted_data, axis=0), np.min(weighted_data, axis=0))
    distances = np.sqrt(np.sum((weighted_data - ideal_solution) ** 2, axis=1))
    return distances

def main(input_file, weights, impacts, result_file):
    try:
        with open(input_file) as f:
            data = f.readlines()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    data = [line.strip().split(',') for line in data]

    if not is_number(data[0][1]):
        data = data[1:]

    for i in range(len(data)):
        for j in range(1, len(data[i])):
            try:
                data[i][j] = float(data[i][j])
            except ValueError:
                print(f"Error: could not convert string to float: '{data[i][j]}'")
                return
    data = np.array(data)

    if data.shape[1] < 6:
        print("Error: Input file must contain at least six columns.")
        return
    if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
        print(len(weights),len(impacts),data.shape[1])
        print("Error: Number of weights, impacts, and columns must be the same.")
        return
    for i in impacts:
        if i != 1 and i != -1:
            print("Error: Impacts must be either 1 or -1.")
            return

    scores = topsis(data[:, 1:], weights, impacts)
    ranks = np.argsort(-scores) + 1
    try:
        with open(result_file, 'w') as f:
            f.write(",".join(data[0]) + ", Topsis Score, Rank\n")
            for i, score in enumerate(scores):
                f.write(",".join([str(x) for x in data[i]]) + f", {score}, {ranks[i]}\n")
    except:
        print("Error: Could not write to result file.")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters. Usage: python topsis.py input_file weights impacts result_file")
    else:
        input_file = sys.argv[1]
        weights = list(map(float, sys.argv[2].split(',')))
        impacts_string= sys.argv[3]
        impacts = [1 if ch == "+" else -1 for ch in impacts_string.split(",")]
        result_file = sys.argv[4]
        main(input_file,weights,impacts,result_file)
        print(input_file,weights,impacts,result_file)

