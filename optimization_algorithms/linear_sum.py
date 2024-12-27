from scipy.optimize import linear_sum_assignment
import numpy as np

cost_matrix = [[38,53,61,36,66], [100,60,9,79,34], [30,37,36,72,24], [61,95,21,14,64], [89,90,4,5,79]]
row_ind, col_ind = linear_sum_assignment(cost_matrix)
assignments = []
for i in range (len(row_ind)):
    assignments.append((row_ind[i], col_ind[i]))
print (assignments)

profit_matrix = []
for i in range(len(cost_matrix)):
    profit_row = []
    for j in range(len(cost_matrix)):
        profit_row.append(-cost_matrix[i][j])
    profit_matrix.append(profit_row)
# profit_matrix = [[-cost_matrix[i][j] for j in range(len(cost_matrix))] for i in range(len(cost_matrix))]
row_ind, col_ind = linear_sum_assignment(profit_matrix)
assignments = []
for i in range (len(row_ind)):
    assignments.append((row_ind[i], col_ind[i]))
print (assignments)

# with numpy arrays
cost_np_array = np.array(cost_matrix)
row_ind2, col_ind2 = linear_sum_assignment(cost_matrix)
# Indexing using index arrays
assignment_list = cost_np_array[row_ind2, col_ind2]

print(1)
