# -*- coding: UTF-8 -*- 

from src import *
import pandas as pd
import numpy as np
import logging

def DataProcessing(csv,Feature1,Feature2,Feature3):
    data = pd.read_csv(csv)
    time = np.max(data['ts'])-np.min(data['ts'])

    df1 = GetFeature(Feature1,data)
    df1 = harmonize_data(df1)
    Identify(df1, Feature1, 'aging_1.csv', 'crash_time_1.csv',"aging_1", "crash_time_1", time)
    Split('aging_1.csv', "aging_1", "Classification_train_1.csv", "Classification_verify_1.csv", "Classification_test_1.csv")
    SimpleSplit('crash_time_1.csv', "Regression_train_1.csv", "Regression_verify_1.csv", "Regression_test_1.csv")

    df2 = GetFeature(Feature2,data)
    df2 = harmonize_data(df2)
    Identify(df2, Feature2, 'aging_2.csv', 'crash_time_2.csv', "aging_2", "crash_time_2", time)
    Split('aging_2.csv', "aging_2", "Classification_train_2.csv", "Classification_verify_2.csv", "Classification_test_2.csv")
    SimpleSplit('crash_time_2.csv', "Regression_train_2.csv", "Regression_verify_2.csv", "Regression_test_2.csv")

    df3 = GetFeature(Feature3,data)
    df3 = harmonize_data(df3)
    Identify(df3, Feature3, 'aging_3.csv', 'crash_time_3.csv', "aging_3", "crash_time_3", time)
    Split('aging_3.csv', "aging_3", "Classification_train_3.csv", "Classification_verify_3.csv", "Classification_test_3.csv")
    SimpleSplit('crash_time_3.csv', "Regression_train_3.csv", "Regression_verify_3.csv", "Regression_test_3.csv")

def Multi_DataProcessing(csv_list,Feature1,Feature2,Feature3):
    df1 = [preprocessing(f'./data/{group}.csv', Feature1) for group in csv_list]

    # Identify(df1, Feature1, 'aging_1.csv', 'crash_time_1.csv',"aging_1", "crash_time_1", time)
    Multi_Identify(df1, Feature1, 'aging_1.csv', 'crash_time_1.csv',"aging_1", "crash_time_1")
    Split('aging_1.csv', "aging_1", "Classification_train_1.csv", "Classification_verify_1.csv", "Classification_test_1.csv")
    SimpleSplit('crash_time_1.csv', "Regression_train_1.csv", "Regression_verify_1.csv", "Regression_test_1.csv")

    df2 = [preprocessing(f'./data/{group}.csv', Feature2) for group in csv_list]
    Multi_Identify(df2, Feature2, 'aging_2.csv', 'crash_time_2.csv', "aging_2", "crash_time_2")
    Split('aging_2.csv', "aging_2", "Classification_train_2.csv", "Classification_verify_2.csv", "Classification_test_2.csv")
    SimpleSplit('crash_time_2.csv', "Regression_train_2.csv", "Regression_verify_2.csv", "Regression_test_2.csv")

    df3 = [preprocessing(f'./data/{group}.csv', Feature3) for group in csv_list]
    Multi_Identify(df3, Feature3, 'aging_3.csv', 'crash_time_3.csv', "aging_3", "crash_time_3")
    Split('aging_3.csv', "aging_3", "Classification_train_3.csv", "Classification_verify_3.csv", "Classification_test_3.csv")
    SimpleSplit('crash_time_3.csv', "Regression_train_3.csv", "Regression_verify_3.csv", "Regression_test_3.csv")

def TrainModel():
    TrainingModel("Classification_train_1.csv", "model_1_1.model", "model_1_2.model", "model_1_3.model", "model_1_4.model", "model_1_5.model")
    TrainingModel("Classification_train_2.csv", "model_2_1.model", "model_2_2.model", "model_2_3.model", "model_2_4.model", "model_2_5.model")
    TrainingModel("Classification_train_3.csv", "model_3_1.model", "model_3_2.model", "model_3_3.model", "model_3_4.model", "model_3_5.model")
    
    TrainingRegressionModel("Regression_train_1.csv", "Regression_model_1_1.model", "Regression_model_1_2.model", "Regression_model_1_3.model", "Regression_model_1_4.model", "Regression_model_1_5.model")
    TrainingRegressionModel("Regression_train_2.csv", "Regression_model_2_1.model", "Regression_model_2_2.model", "Regression_model_2_3.model", "Regression_model_2_4.model", "Regression_model_2_5.model")
    TrainingRegressionModel("Regression_train_3.csv", "Regression_model_3_1.model", "Regression_model_3_2.model", "Regression_model_3_3.model", "Regression_model_3_4.model", "Regression_model_3_5.model")

def TestModel():
    folder = os.path.exists("./result")
    if not folder:
        os.makedirs("./result")
        
    result_1_1 = TestClassification("Classification_test_1.csv", "predicated_aging", "aging_1", "model_1_1.model", "./result/result_1_1.csv")
    result_1_2 = TestClassification("Classification_test_1.csv", "predicated_aging", "aging_1", "model_1_2.model", "./result/result_1_2.csv")
    result_1_3 = TestClassification("Classification_test_1.csv", "predicated_aging", "aging_1", "model_1_3.model", "./result/result_1_3.csv")
    result_1_4 = TestClassification("Classification_test_1.csv", "predicated_aging", "aging_1", "model_1_4.model", "./result/result_1_4.csv")
    result_1_5 = TestClassification("Classification_test_1.csv", "predicated_aging", "aging_1", "model_1_5.model", "./result/result_1_5.csv")
    
    result_2_1 = TestClassification("Classification_test_2.csv", "predicated_aging", "aging_2", "model_2_1.model", "./result/result_2_1.csv")
    result_2_2 = TestClassification("Classification_test_2.csv", "predicated_aging", "aging_2", "model_2_2.model", "./result/result_2_2.csv")
    result_2_3 = TestClassification("Classification_test_2.csv", "predicated_aging", "aging_2", "model_2_3.model", "./result/result_2_3.csv")
    result_2_4 = TestClassification("Classification_test_2.csv", "predicated_aging", "aging_2", "model_2_4.model", "./result/result_2_4.csv")
    result_2_5 = TestClassification("Classification_test_2.csv", "predicated_aging", "aging_2", "model_2_5.model", "./result/result_2_5.csv")
    
    result_3_1 = TestClassification("Classification_test_3.csv", "predicated_aging", "aging_3", "model_3_1.model", "./result/result_3_1.csv")
    result_3_2 = TestClassification("Classification_test_3.csv", "predicated_aging", "aging_3", "model_3_2.model", "./result/result_3_2.csv")
    result_3_3 = TestClassification("Classification_test_3.csv", "predicated_aging", "aging_3", "model_3_3.model", "./result/result_3_3.csv")
    result_3_4 = TestClassification("Classification_test_3.csv", "predicated_aging", "aging_3", "model_3_4.model", "./result/result_3_4.csv")
    result_3_5 = TestClassification("Classification_test_3.csv", "predicated_aging", "aging_3", "model_3_5.model", "./result/result_3_5.csv")

    classification_data = {
    "Logistic": [result_1_1, result_2_1, result_3_1],
    "NaiveBayes": [result_1_2, result_2_2, result_3_2],
    "IBk": [result_1_3, result_2_3, result_3_3],
    "REPTree": [result_1_4, result_2_4, result_3_4],
    "SMO": [result_1_5, result_2_5, result_3_5]
    }

    reg_result_1_1 = TestRegression("Regression_test_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_1.model", "./result/Regression_result_1_1.csv")
    reg_result_1_2 = TestRegression("Regression_test_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_2.model", "./result/Regression_result_1_2.csv")
    reg_result_1_3 = TestRegression("Regression_test_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_3.model", "./result/Regression_result_1_3.csv")
    reg_result_1_4 = TestRegression("Regression_test_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_4.model", "./result/Regression_result_1_4.csv")
    reg_result_1_5 = TestRegression("Regression_test_1.csv", "predicated_time", "crash_time_1", "Regression_model_1_5.model", "./result/Regression_result_1_5.csv")
    
    reg_result_2_1 = TestRegression("Regression_test_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_1.model", "./result/Regression_result_2_1.csv")
    reg_result_2_2 = TestRegression("Regression_test_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_2.model", "./result/Regression_result_2_2.csv")
    reg_result_2_3 = TestRegression("Regression_test_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_3.model", "./result/Regression_result_2_3.csv")
    reg_result_2_4 = TestRegression("Regression_test_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_4.model", "./result/Regression_result_2_4.csv")
    reg_result_2_5 = TestRegression("Regression_test_2.csv", "predicated_time", "crash_time_2", "Regression_model_2_5.model", "./result/Regression_result_2_5.csv")

    reg_result_3_1 = TestRegression("Regression_test_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_1.model", "./result/Regression_result_3_1.csv")
    reg_result_3_2 = TestRegression("Regression_test_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_2.model", "./result/Regression_result_3_2.csv")
    reg_result_3_3 = TestRegression("Regression_test_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_3.model", "./result/Regression_result_3_3.csv")
    reg_result_3_4 = TestRegression("Regression_test_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_4.model", "./result/Regression_result_3_4.csv")
    reg_result_3_5 = TestRegression("Regression_test_3.csv", "predicated_time", "crash_time_3", "Regression_model_3_5.model", "./result/Regression_result_3_5.csv")

    regression_data = {
    "Logistic": [reg_result_1_1, reg_result_2_1, reg_result_3_1],
    "NaiveBayes": [reg_result_1_2, reg_result_2_2, reg_result_3_2],
    "IBk": [reg_result_1_3, reg_result_2_3, reg_result_3_3],
    "REPTree": [reg_result_1_4, reg_result_2_4, reg_result_3_4],
    "SMO": [reg_result_1_5, reg_result_2_5, reg_result_3_5]
    }

    print(f"result of classification:{classification_data}")
    print(f"result of regression:{regression_data}")


def main():
    DataProcessing('./data/device/mi/10app1/tracing.csv', "pgfault","mem_shared","slab")
    # Multi_DataProcessing(['1app', '10app1', '10app2', '30app'], "pgfault","mem_shared","slab")
    
    jvm.start(packages=True, class_path=['C:\\Users\\jxche\\miniconda3\\lib\\site-packages\\weka\\lib\\mtj.jar'])
    
    TrainModel()
    TestModel()
    
    jvm.stop()
    
    print("work is done!")



if __name__ == "__main__":
    main()
