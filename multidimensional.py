#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import pandas as pd

# value = 0

def multi_dim():
    path = os.getcwd()
    path = path + "\\Testresult\\"

    data_1_1 = pd.read_csv(path + 'result_1_1.csv')
    data_1_2 = pd.read_csv(path + 'result_1_2.csv')
    data_1_3 = pd.read_csv(path + 'result_1_3.csv')
    data_1_4 = pd.read_csv(path + 'result_1_4.csv')
    data_1_5 = pd.read_csv(path + 'result_1_5.csv')
    data_2_1 = pd.read_csv(path + 'result_2_1.csv')
    data_2_2 = pd.read_csv(path + 'result_2_2.csv')
    data_2_3 = pd.read_csv(path + 'result_2_3.csv')
    data_2_4 = pd.read_csv(path + 'result_2_4.csv')
    data_2_5 = pd.read_csv(path + 'result_2_5.csv')
    data_3_1 = pd.read_csv(path + 'result_3_1.csv')
    data_3_2 = pd.read_csv(path + 'result_3_2.csv')
    data_3_3 = pd.read_csv(path + 'result_3_3.csv')
    data_3_4 = pd.read_csv(path + 'result_3_4.csv')
    data_3_5 = pd.read_csv(path + 'result_3_5.csv')

    total = data_1_1.index.stop
    count = 0

    for indexs in data_1_1.index:
        value = 0
        value = value + data_1_1.loc[indexs,'aging_1']
        value = value + data_1_2.loc[indexs,'aging_1']
        value = value + data_1_3.loc[indexs,'aging_1']
        value = value + data_1_4.loc[indexs,'aging_1']
        value = value + data_1_5.loc[indexs,'aging_1']
        value = value + data_2_1.loc[indexs,'aging_2']
        value = value + data_2_2.loc[indexs,'aging_2']
        value = value + data_2_3.loc[indexs,'aging_2']
        value = value + data_2_4.loc[indexs,'aging_2']
        value = value + data_2_5.loc[indexs,'aging_2']
        value = value + data_3_1.loc[indexs,'aging_3']
        value = value + data_3_2.loc[indexs,'aging_3']
        value = value + data_3_3.loc[indexs,'aging_3']
        value = value + data_3_4.loc[indexs,'aging_3']
        value = value + data_3_5.loc[indexs,'aging_3']

        if value >= 8:
            data_1_1.loc[indexs,'AGING']  = True
        else:
            data_1_1.loc[indexs,'AGING']  = False 
        
        value = 0
        value = value + data_1_1.loc[indexs,"predicated_aging"]
        value = value + data_1_2.loc[indexs,"predicated_aging"]
        value = value + data_1_3.loc[indexs,"predicated_aging"]
        value = value + data_1_4.loc[indexs,"predicated_aging"]
        value = value + data_1_5.loc[indexs,"predicated_aging"]
        value = value + data_2_1.loc[indexs,"predicated_aging"]
        value = value + data_2_2.loc[indexs,"predicated_aging"]
        value = value + data_2_3.loc[indexs,"predicated_aging"]
        value = value + data_2_4.loc[indexs,"predicated_aging"]
        value = value + data_2_5.loc[indexs,"predicated_aging"]
        value = value + data_3_1.loc[indexs,"predicated_aging"]
        value = value + data_3_2.loc[indexs,"predicated_aging"]
        value = value + data_3_3.loc[indexs,"predicated_aging"]
        value = value + data_3_4.loc[indexs,"predicated_aging"]
        value = value + data_3_5.loc[indexs,"predicated_aging"]

        if value >= 8:
            data_1_1.loc[indexs,'predictedAGING']  = True
        else:
            data_1_1.loc[indexs,'predictedAGING']  = False 
        
    count = 0

    for indexs in data_1_1.index:
        if data_1_1.loc[indexs,'AGING'] == data_1_1.loc[indexs,'predictedAGING']:
            count = count + 1

    result = count * 1.0 / total    


    data_1_1 = pd.read_csv(path + 'Regression_result_1_1.csv')
    data_1_2 = pd.read_csv(path + 'Regression_result_1_2.csv')
    data_1_3 = pd.read_csv(path + 'Regression_result_1_3.csv')
    data_1_4 = pd.read_csv(path + 'Regression_result_1_4.csv')
    data_1_5 = pd.read_csv(path + 'Regression_result_1_5.csv')
    data_2_1 = pd.read_csv(path + 'Regression_result_2_1.csv')
    data_2_2 = pd.read_csv(path + 'Regression_result_2_2.csv')
    data_2_3 = pd.read_csv(path + 'Regression_result_2_3.csv')
    data_2_4 = pd.read_csv(path + 'Regression_result_2_4.csv')
    data_2_5 = pd.read_csv(path + 'Regression_result_2_5.csv')
    data_3_1 = pd.read_csv(path + 'Regression_result_3_1.csv')
    data_3_2 = pd.read_csv(path + 'Regression_result_3_2.csv')
    data_3_3 = pd.read_csv(path + 'Regression_result_3_3.csv')
    data_3_4 = pd.read_csv(path + 'Regression_result_3_4.csv')
    data_3_5 = pd.read_csv(path + 'Regression_result_3_5.csv')

    total = data_1_1.index.stop
    count = 0

    for indexs in data_1_1.index:
        value = 0
        value = value + data_1_1.loc[indexs,'crash_time_1']
        value = value + data_1_2.loc[indexs,'crash_time_1']
        value = value + data_1_3.loc[indexs,'crash_time_1']
        value = value + data_1_4.loc[indexs,'crash_time_1']
        value = value + data_1_5.loc[indexs,'crash_time_1']
        value = value + data_2_1.loc[indexs,'crash_time_2']
        value = value + data_2_2.loc[indexs,'crash_time_2']
        value = value + data_2_3.loc[indexs,'crash_time_2']
        value = value + data_2_4.loc[indexs,'crash_time_2']
        value = value + data_2_5.loc[indexs,'crash_time_2']
        value = value + data_3_1.loc[indexs,'crash_time_3']
        value = value + data_3_2.loc[indexs,'crash_time_3']
        value = value + data_3_3.loc[indexs,'crash_time_3']
        value = value + data_3_4.loc[indexs,'crash_time_3']
        value = value + data_3_5.loc[indexs,'crash_time_3']

        data_1_1.loc[indexs,'crash_time']  = value / 15 
        
        value = 0
        value = value + data_1_1.loc[indexs,"predicated_time"]
        value = value + data_1_2.loc[indexs,"predicated_time"]
        value = value + data_1_3.loc[indexs,"predicated_time"]
        value = value + data_1_4.loc[indexs,"predicated_time"]
        value = value + data_1_5.loc[indexs,"predicated_time"]
        value = value + data_2_1.loc[indexs,"predicated_time"]
        value = value + data_2_2.loc[indexs,"predicated_time"]
        value = value + data_2_3.loc[indexs,"predicated_time"]
        value = value + data_2_4.loc[indexs,"predicated_time"]
        value = value + data_2_5.loc[indexs,"predicated_time"]
        value = value + data_3_1.loc[indexs,"predicated_time"]
        value = value + data_3_2.loc[indexs,"predicated_time"]
        value = value + data_3_3.loc[indexs,"predicated_time"]
        value = value + data_3_4.loc[indexs,"predicated_time"]
        value = value + data_3_5.loc[indexs,"predicated_time"]

        data_1_1.loc[indexs,'predictedcrash_time']  = value / 15
        
    MAE = 0
    RMSE = 0

    for indexs in data_1_1.index:
        MAE = MAE + abs(data_1_1.loc[indexs,'crash_time'] - data_1_1.loc[indexs,'predictedcrash_time'])
        RMSE = RMSE + abs(data_1_1.loc[indexs,'crash_time'] - data_1_1.loc[indexs,'predictedcrash_time']) ** 2

    MAE = MAE / total    
    RMSE = (RMSE / total) ** 0.5

    data_1_1.to_csv("result.csv",index =False ,sep = ',')

    result = result * 100;
    print(round(result,4))
    print(round(RMSE,4))

    return result, RMSE
    # print("work is done")

def choose_multi_dim(path, algo_chosen, metric_chosen):

    data_1_1 = pd.read_csv(path + 'result_1_1.csv')
    data_1_2 = pd.read_csv(path + 'result_1_2.csv')
    data_1_3 = pd.read_csv(path + 'result_1_3.csv')
    data_1_4 = pd.read_csv(path + 'result_1_4.csv')
    data_1_5 = pd.read_csv(path + 'result_1_5.csv')
    data_2_1 = pd.read_csv(path + 'result_2_1.csv')
    data_2_2 = pd.read_csv(path + 'result_2_2.csv')
    data_2_3 = pd.read_csv(path + 'result_2_3.csv')
    data_2_4 = pd.read_csv(path + 'result_2_4.csv')
    data_2_5 = pd.read_csv(path + 'result_2_5.csv')
    data_3_1 = pd.read_csv(path + 'result_3_1.csv')
    data_3_2 = pd.read_csv(path + 'result_3_2.csv')
    data_3_3 = pd.read_csv(path + 'result_3_3.csv')
    data_3_4 = pd.read_csv(path + 'result_3_4.csv')
    data_3_5 = pd.read_csv(path + 'result_3_5.csv')

    total = data_1_1.index.stop
    count = 0

    for indexs in data_1_1.index:
        value = 0
        value = value + data_1_1.loc[indexs,'aging_1']
        value = value + data_1_2.loc[indexs,'aging_1']
        value = value + data_1_3.loc[indexs,'aging_1']
        value = value + data_1_4.loc[indexs,'aging_1']
        value = value + data_1_5.loc[indexs,'aging_1']
        value = value + data_2_1.loc[indexs,'aging_2']
        value = value + data_2_2.loc[indexs,'aging_2']
        value = value + data_2_3.loc[indexs,'aging_2']
        value = value + data_2_4.loc[indexs,'aging_2']
        value = value + data_2_5.loc[indexs,'aging_2']
        value = value + data_3_1.loc[indexs,'aging_3']
        value = value + data_3_2.loc[indexs,'aging_3']
        value = value + data_3_3.loc[indexs,'aging_3']
        value = value + data_3_4.loc[indexs,'aging_3']
        value = value + data_3_5.loc[indexs,'aging_3']

        if value >= 8:
            data_1_1.loc[indexs,'AGING']  = True
        else:
            data_1_1.loc[indexs,'AGING']  = False 
        
        value = 0
        for i in algo_chosen:
            for j in metric_chosen:
                exec(f'res = data_{j}_{i}.loc[indexs, "predicated_aging"]')
                value += locals()['res']
        # value = value + data_1_1.loc[indexs,"predicated_aging"]
        # value = value + data_1_2.loc[indexs,"predicated_aging"]
        # value = value + data_1_3.loc[indexs,"predicated_aging"]
        # value = value + data_1_4.loc[indexs,"predicated_aging"]
        # value = value + data_1_5.loc[indexs,"predicated_aging"]
        # value = value + data_2_1.loc[indexs,"predicated_aging"]
        # value = value + data_2_2.loc[indexs,"predicated_aging"]
        # value = value + data_2_3.loc[indexs,"predicated_aging"]
        # value = value + data_2_4.loc[indexs,"predicated_aging"]
        # value = value + data_2_5.loc[indexs,"predicated_aging"]
        # value = value + data_3_1.loc[indexs,"predicated_aging"]
        # value = value + data_3_2.loc[indexs,"predicated_aging"]
        # value = value + data_3_3.loc[indexs,"predicated_aging"]
        # value = value + data_3_4.loc[indexs,"predicated_aging"]
        # value = value + data_3_5.loc[indexs,"predicated_aging"]

        if value >= (len(algo_chosen)*len(metric_chosen)//2+1):
            data_1_1.loc[indexs,'predictedAGING']  = True
        else:
            data_1_1.loc[indexs,'predictedAGING']  = False 
        
    count = 0

    for indexs in data_1_1.index:
        if data_1_1.loc[indexs,'AGING'] == data_1_1.loc[indexs,'predictedAGING']:
            count = count + 1

    result = count * 1.0 / total    


    data_1_1 = pd.read_csv(path + 'Regression_result_1_1.csv')
    data_1_2 = pd.read_csv(path + 'Regression_result_1_2.csv')
    data_1_3 = pd.read_csv(path + 'Regression_result_1_3.csv')
    data_1_4 = pd.read_csv(path + 'Regression_result_1_4.csv')
    data_1_5 = pd.read_csv(path + 'Regression_result_1_5.csv')
    data_2_1 = pd.read_csv(path + 'Regression_result_2_1.csv')
    data_2_2 = pd.read_csv(path + 'Regression_result_2_2.csv')
    data_2_3 = pd.read_csv(path + 'Regression_result_2_3.csv')
    data_2_4 = pd.read_csv(path + 'Regression_result_2_4.csv')
    data_2_5 = pd.read_csv(path + 'Regression_result_2_5.csv')
    data_3_1 = pd.read_csv(path + 'Regression_result_3_1.csv')
    data_3_2 = pd.read_csv(path + 'Regression_result_3_2.csv')
    data_3_3 = pd.read_csv(path + 'Regression_result_3_3.csv')
    data_3_4 = pd.read_csv(path + 'Regression_result_3_4.csv')
    data_3_5 = pd.read_csv(path + 'Regression_result_3_5.csv')

    total = data_1_1.index.stop
    count = 0

    for indexs in data_1_1.index:
        value = 0
        value = value + data_1_1.loc[indexs,'crash_time_1']
        value = value + data_1_2.loc[indexs,'crash_time_1']
        value = value + data_1_3.loc[indexs,'crash_time_1']
        value = value + data_1_4.loc[indexs,'crash_time_1']
        value = value + data_1_5.loc[indexs,'crash_time_1']
        value = value + data_2_1.loc[indexs,'crash_time_2']
        value = value + data_2_2.loc[indexs,'crash_time_2']
        value = value + data_2_3.loc[indexs,'crash_time_2']
        value = value + data_2_4.loc[indexs,'crash_time_2']
        value = value + data_2_5.loc[indexs,'crash_time_2']
        value = value + data_3_1.loc[indexs,'crash_time_3']
        value = value + data_3_2.loc[indexs,'crash_time_3']
        value = value + data_3_3.loc[indexs,'crash_time_3']
        value = value + data_3_4.loc[indexs,'crash_time_3']
        value = value + data_3_5.loc[indexs,'crash_time_3']

        data_1_1.loc[indexs,'crash_time']  = value / 15 
        
        value = 0
        for i in algo_chosen:
            for j in metric_chosen:
                exec(f'res = data_{j}_{i}.loc[indexs, "predicated_time"]')
                value += locals()['res']
        # value = value + data_1_1.loc[indexs,"predicated_time"]
        # value = value + data_1_2.loc[indexs,"predicated_time"]
        # value = value + data_1_3.loc[indexs,"predicated_time"]
        # value = value + data_1_4.loc[indexs,"predicated_time"]
        # value = value + data_1_5.loc[indexs,"predicated_time"]
        # value = value + data_2_1.loc[indexs,"predicated_time"]
        # value = value + data_2_2.loc[indexs,"predicated_time"]
        # value = value + data_2_3.loc[indexs,"predicated_time"]
        # value = value + data_2_4.loc[indexs,"predicated_time"]
        # value = value + data_2_5.loc[indexs,"predicated_time"]
        # value = value + data_3_1.loc[indexs,"predicated_time"]
        # value = value + data_3_2.loc[indexs,"predicated_time"]
        # value = value + data_3_3.loc[indexs,"predicated_time"]
        # value = value + data_3_4.loc[indexs,"predicated_time"]
        # value = value + data_3_5.loc[indexs,"predicated_time"]

        data_1_1.loc[indexs,'predictedcrash_time']  = value / (len(algo_chosen)*len(metric_chosen))
        
    MAE = 0
    RMSE = 0

    for indexs in data_1_1.index:
        MAE = MAE + abs(data_1_1.loc[indexs,'crash_time'] - data_1_1.loc[indexs,'predictedcrash_time'])
        RMSE = RMSE + abs(data_1_1.loc[indexs,'crash_time'] - data_1_1.loc[indexs,'predictedcrash_time']) ** 2

    MAE = MAE / total    
    RMSE = (RMSE / total) ** 0.5

    data_1_1.to_csv("result.csv",index =False ,sep = ',')

    result = result * 100
    print(round(result,4))
    print(round(RMSE,4))

    print("work is done")
    return result, RMSE

# multi_dim()
# choose_multi_dim([2,3,4,5], [1,2,3])
def compare_multi_dim():
    from itertools import combinations
    algos = [1,2,3,4,5]
    metrics = [1,2,3]
    algos_comb = list(combinations(algos, 5))+list(combinations(algos, 4))+list(combinations(algos, 3))+list(combinations(algos, 2))+list(combinations(algos, 1))
    metrics_comb = list(combinations(metrics, 3)) + list(combinations(metrics, 2)) + list(combinations(metrics, 1))
    for group in ['10app_1', '10app_2', '1app', '30app']:
        df = pd.DataFrame(columns=algos_comb, index=metrics_comb)
        path = os.getcwd() + f"\\Testresult\\{group}\\"  
        for i in algos_comb:
            for j in metrics_comb:
                print(i, j)
                result, RMSE = choose_multi_dim(path, list(i), list(j))
                df[i][j] = {'accu': result, 'RMSE': RMSE}
                print('------------------')
        df.to_csv(f'{group}_result.csv', index=True, sep=',')

# multi_dim()