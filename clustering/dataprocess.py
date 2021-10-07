import pandas as pd
import os

csv_path = "D:/Isla/StudyinHK/paper/result" # 当前目录
csv_list = os.listdir(csv_path)

target_csv_filename = "3t5_A.csv"
target_path = "D:/Isla/StudyinHK/paper/result/input/"
done_csv=os.path.join(target_path, target_csv_filename)



for filename in csv_list:
    if ('A_result.csv' in filename)  and ('3t5' in filename):
        current_csv=os.path.join(csv_path, filename)
        df = pd.read_csv(current_csv,error_bad_lines=False)
        df_obs=df['obs']
        df1 = pd.DataFrame(data=df_obs)
        df_obs_T=df1.T
        df_obs_T.to_csv(done_csv,mode='a',header=None,index=False)