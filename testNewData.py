#!/usr/bin/python
# -*- coding: UTF-8 -*- 

from src import *
import pandas as pd
import numpy as np
import os
from multidimensional import multi_dim

def DataProcessing(csv,Feature1,Feature2,Feature3):
    data = pd.read_csv(csv)
    time = np.max(data['ts'])-np.min(data['ts'])

    df1 = GetSameFeature("Classification_train_1.csv",data)
    df1 = harmonize_data(df1)
    Identify(df1, Feature1, 'aging_1.csv', 'crash_time_1.csv',"aging_1", "crash_time_1",time)

    df2 = GetSameFeature("Classification_train_2.csv",data)
    df2 = harmonize_data(df2)
    Identify(df2, Feature2, 'aging_2.csv', 'crash_time_2.csv', "aging_2", "crash_time_2",time)

    df3 = GetSameFeature("Classification_train_3.csv",data)
    df3 = harmonize_data(df3)
    Identify(df3, Feature3, 'aging_3.csv', 'crash_time_3.csv', "aging_3", "crash_time_3",time)

def TestModel():
    # folder = os.path.exists(f"./Testresult/{group}")
    # if not folder:
    #     os.makedirs(f"./Testresult/{group}")

    result_1_1 = TestClassification("aging_1.csv", "predicated_aging", "aging_1", "model_1_1.model", "./Testresult/result_1_1.csv")
    result_1_2 = TestClassification("aging_1.csv", "predicated_aging", "aging_1", "model_1_2.model", "./Testresult/result_1_2.csv")
    result_1_3 = TestClassification("aging_1.csv", "predicated_aging", "aging_1", "model_1_3.model", "./Testresult/result_1_3.csv")
    result_1_4 = TestClassification("aging_1.csv", "predicated_aging", "aging_1", "model_1_4.model", "./Testresult/result_1_4.csv")
    result_1_5 = TestClassification("aging_1.csv", "predicated_aging", "aging_1", "model_1_5.model", "./Testresult/result_1_5.csv")
    #result1 = (result_1_1+result_1_2+result_1_3+result_1_4+result_1_5)/5
    #print(result1
    # print('------')
    result_2_1 = TestClassification("aging_2.csv", "predicated_aging", "aging_2", "model_2_1.model", "./Testresult/result_2_1.csv")
    result_2_2 = TestClassification("aging_2.csv", "predicated_aging", "aging_2", "model_2_2.model", "./Testresult/result_2_2.csv")
    result_2_3 = TestClassification("aging_2.csv", "predicated_aging", "aging_2", "model_2_3.model", "./Testresult/result_2_3.csv")
    result_2_4 = TestClassification("aging_2.csv", "predicated_aging", "aging_2", "model_2_4.model", "./Testresult/result_2_4.csv")
    result_2_5 = TestClassification("aging_2.csv", "predicated_aging", "aging_2", "model_2_5.model", "./Testresult/result_2_5.csv")
    #result2 = (result_2_1+result_2_2+result_2_3+result_2_4+result_2_5)/5
    #print(result2)
    # print('------')
    result_3_1 = TestClassification("aging_3.csv", "predicated_aging", "aging_3", "model_3_1.model", "./Testresult/result_3_1.csv")
    result_3_2 = TestClassification("aging_3.csv", "predicated_aging", "aging_3", "model_3_2.model", "./Testresult/result_3_2.csv")
    result_3_3 = TestClassification("aging_3.csv", "predicated_aging", "aging_3", "model_3_3.model", "./Testresult/result_3_3.csv")
    result_3_4 = TestClassification("aging_3.csv", "predicated_aging", "aging_3", "model_3_4.model", "./Testresult/result_3_4.csv")
    result_3_5 = TestClassification("aging_3.csv", "predicated_aging", "aging_3", "model_3_5.model", "./Testresult/result_3_5.csv")
    #result3 = (result_3_1+result_3_2+result_3_3+result_3_4+result_3_5)/5
    #print(result3)

    print("Classification work is done")

    reg_result_1_1 = TestRegression("crash_time_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_1.model", "./Testresult/Regression_result_1_1.csv")
    reg_result_1_2 = TestRegression("crash_time_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_2.model", "./Testresult/Regression_result_1_2.csv")
    reg_result_1_3 = TestRegression("crash_time_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_3.model", "./Testresult/Regression_result_1_3.csv")
    reg_result_1_4 = TestRegression("crash_time_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_4.model", "./Testresult/Regression_result_1_4.csv")
    reg_result_1_5 = TestRegression("crash_time_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_5.model", "./Testresult/Regression_result_1_5.csv")
    # print('------')

    reg_result_2_1 = TestRegression("crash_time_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_1.model", "./Testresult/Regression_result_2_1.csv")
    reg_result_2_2 = TestRegression("crash_time_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_2.model", "./Testresult/Regression_result_2_2.csv")
    reg_result_2_3 = TestRegression("crash_time_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_3.model", "./Testresult/Regression_result_2_3.csv")
    reg_result_2_4 = TestRegression("crash_time_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_4.model", "./Testresult/Regression_result_2_4.csv")
    reg_result_2_5 = TestRegression("crash_time_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_5.model", "./Testresult/Regression_result_2_5.csv")
    # print('------')
    reg_result_3_1 = TestRegression("crash_time_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_1.model", "./Testresult/Regression_result_3_1.csv")
    reg_result_3_2 = TestRegression("crash_time_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_2.model", "./Testresult/Regression_result_3_2.csv")
    reg_result_3_3 = TestRegression("crash_time_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_3.model", "./Testresult/Regression_result_3_3.csv")
    reg_result_3_4 = TestRegression("crash_time_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_4.model", "./Testresult/Regression_result_3_4.csv")
    reg_result_3_5 = TestRegression("crash_time_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_5.model", "./Testresult/Regression_result_3_5.csv")
    
    # print("Regression work is done")
    multi_res, multi_RMSE = multi_dim()

    classification_data = {
    "Logistic": [result_1_1, result_2_1, result_3_1],
    "NaiveBayes": [result_1_2, result_2_2, result_3_2],
    "IBk": [result_1_3, result_2_3, result_3_3],
    "REPTree": [result_1_4, result_2_4, result_3_4],
    "SMO": [result_1_5, result_2_5, result_3_5],
    "Multi": [multi_res]
    }

    regression_data = {
    "Logistic": [reg_result_1_1, reg_result_2_1, reg_result_3_1],
    "NaiveBayes": [reg_result_1_2, reg_result_2_2, reg_result_3_2],
    "IBk": [reg_result_1_3, reg_result_2_3, reg_result_3_3],
    "REPTree": [reg_result_1_4, reg_result_2_4, reg_result_3_4],
    "SMO": [reg_result_1_5, reg_result_2_5, reg_result_3_5],
    "Multi": [multi_RMSE]
    }
    # print(f'Group: {group}'}')
    print(f"result of classification:{classification_data}")
    print(f"result of regression:{regression_data}")
    return classification_data, regression_data


def main():
    global groups
    groups = ['10app2', '30app', '1app']
    # DataProcessing('./data/30app.csv',"pgfault","mem_shared","slab")
    classification_data, regression_data = {}, {}
    jvm.start()
    for group in groups:
        DataProcessing(f'./data/device/huawei/{group}/tracing.csv',"pgfault","mem_shared","slab")
    
        single_classification_data, single_regression_data = TestModel()
        
        if (len(classification_data) == 0):
            classification_data, regression_data = single_classification_data, single_regression_data
        else:
            for key, value in single_classification_data.items():                
                classification_data[key].extend(value)
            for key, value in single_regression_data.items():                
                regression_data[key].extend(value)
    print(f"result of classification:{classification_data}")
    print(f"result of regression:{regression_data}")
    jvm.stop()


if __name__ == "__main__":
    main()
