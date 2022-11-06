def format_table(benchmarks, algos, results):
    table = [['Benchmark'] + algos]
    for i in range(1, len(benchmarks)+1):
        table.append([benchmarks[i-1]] + results[i-1])

    column_len = [max(map(len, map(str, [table[i][j] for i in range(len(algos))])))for j in range(len(table)+1)]

    
    for i in range(len(table)):
        print('|', end='')
        for j in range(len(table[0])):
            print(f' {str(table[i][j]).center(column_len[j])} |', end='')

        if i == 0:
            print('\n|' + '-' * (sum(column_len) + 3 * (len(table[0])) - 1) + '|')
        else:
            print()
    
format_table(['best case', 'worst case'],
             ['quick sort', 'meeeeeeeeeeerge sort', 'bubble sort'],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 353145234532346236234624.9]])

print()

format_table(['best case', 'worst case'],
             ['quick sort', 'merge sort', 'bubble sort'],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])

#| Benchmark  | quick sort | meeeeeeeeeeerge sort |      bubble sort       |
#|-------------------------------------------------------------------------|
#| best case  |    1.23    |         1.56         |          2.0           |
#| worst case |    3.3     |         2.9          | 3.5314523453234624e+23 |
 
#| Benchmark  | quick sort | merge sort | bubble sort |
#|----------------------------------------------------|
#| best case  |    1.23    |    1.56    |     2.0     |
#| worst case |    3.3     |    2.9     |     3.9     |
