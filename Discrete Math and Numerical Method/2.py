A = {1, 2, 3}
B = {1, 2}

# Initialize relation R
R = []

# Find elements in R
for a in A:
    for b in B:
        if a > b:
            R.append((a, b))

# Print relation R
print("Relation R:")
for pair in R:
    print(pair)

# Represent relation R in matrix form
a_values = sorted(list(A))
b_values = sorted(list(B))
matrix = [[0 for _ in range(len(b_values))] for _ in range(len(a_values))]

for i, a in enumerate(a_values):
    for j, b in enumerate(b_values):
        if a > b:
            matrix[i][j] = 1

# Print matrix form of relation R
print("\nMatrix form of relation R:")
for row in matrix:
    print(row)
