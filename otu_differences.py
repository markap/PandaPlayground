import pandas as pd

#abs(df['1-3']-df['2-3']).sum()
#>>> s.sort(ascending=False)
#>>> s[:10].sum()


def compute_similarity_matrix(df, column=3):
    sim_matrix = {}
    sim_matrix_values = {}

    for i in range(1,10):
        sim_matrix[i] = {}
        sim_matrix_values[i] = {}
        for j in range(1,10):
            new_column_a = str(i) + '-' + str(column)
            new_column_b = str(j) + '-' + str(column)
            column_diff = abs(df[new_column_a] - df[new_column_b])

            column_diff.sort(ascending=False)
            main_differences = column_diff[:15]

            sim_matrix[i][j] = column_diff.sum()#, "%.2f" % (main_differences.sum()/column_diff.sum())]
            sim_matrix_values[i][j] = main_differences

    return pd.DataFrame(sim_matrix), sim_matrix_values


def compute_main_diff_otus(data):

    main_differences = {}

    for i in range(1,10):
        for j in range(1,i):
            main_diff_otus = data[i][j]
            test_person = str(i) + '-' + str(j)

            for otu in main_diff_otus.index:
                val = main_diff_otus[otu]

                if otu in main_differences:
                    main_differences[otu]['persons'].append(test_person)
                    main_differences[otu]['count'] += val
                    main_differences[otu]['persons_count'][test_person] = val
                else:
                    main_differences[otu] = {'persons': [test_person],
                                             'persons_count': {test_person: val},
                                             'count': val}

    return pd.DataFrame(main_differences)



if __name__ == '__main__':
    df = pd.read_csv(, index_col=0)
    matrix, matrix_values = compute_similarity_matrix(df)
    print matrix
    df =  compute_main_diff_otus(matrix_values)


