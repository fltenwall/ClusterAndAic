# coding=utf-8
import random
import matplotlib.pylab as plt
import numpy as np
import math

import csv
import os, re

def k_means_clust(data,num_clust,num_iter,w=5):
    centroids=random.sample(data,num_clust) #从data（1列列表）中随机抽取num_clust个数
    counter=0
    for n in range(num_iter):
        counter+=1
        assignments={}
        #assign data points to clusters
        for ind,i in enumerate(data):
            #print('ind',ind,i)
            min_dist=float('inf')
            #print('min_dist',min_dist)
            closest_clust=None
            for c_ind,j in enumerate(centroids):
                if LB_Keogh(i,j,5)<min_dist:
                    cur_dist=DTWDistance(i,j,w)
                    if cur_dist<min_dist:
                        min_dist=cur_dist
                        closest_clust=c_ind
            if closest_clust in assignments:
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[ind]

        #recalculate centroids of clusters
        for key in assignments:
            clust_sum=0
            for k in assignments[key]:
                clust_sum=clust_sum+data[k]
            centroids[key]=[m/len(assignments[key]) for m in clust_sum]

    return centroids,data,assignments

def LB_Keogh(s1,s2,r):
    LB_sum=0
    for ind,i in enumerate(s1):

        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])

        if i>upper_bound:
            LB_sum=LB_sum+(i-upper_bound)**2
        elif i<lower_bound:
            LB_sum=LB_sum+(i-lower_bound)**2

    return np.sqrt(LB_sum)

def DTWDistance(s1, s2,w=None):
    DTW={}

    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return np.sqrt(DTW[len(s1)-1, len(s2)-1])

# 计算AIC
# centroids 分类结果的数据 拟合数据
# assignments 分类 {0: [0, 3, 5, 6, 7, 9, 10], 1: [1, 2, 4, 8]}
# data 要进行分类的线性数据
# cls 分类的类别数
# AIC = nln(SSR/n) + 2k
# SSR是残差平方和
def AIC(assignments,centroids,data,cls):
    ssr = 0
    aic = 0
    for i, (k, v) in enumerate(assignments.items()):
        print("assign------------------------------------------------",k,v)
        for (index,val) in enumerate(v):
            print("val",val)
            for (indexI,valI) in enumerate(centroids[k]):
                print("indexI",indexI,"valI",valI)
                ssr += pow(data[val][indexI] - valI,2)
                print('ssr',ssr)
    aic = 2 * cls + len(data) * math.log(ssr / len(data))
    return aic


# def findAllFile(base):
#     for root, ds, fs in os.walk(base):
#         for f in fs:
#             filepath = '../datasets/data/' + f
#             test = np.genfromtxt(filepath, delimiter='\t')
#             data = np.vstack(test[:, :-1])
#
#             res = list()
#             for cls in range(2,len(data)+1):
#                 centroids, data, assignments = k_means_clust(data, cls, 5, 2)
#                 aic = AIC(assignments,centroids,data,cls)
#                 res.append(aic)
#                 print(f, cls,aic,assignments)
#             resAIC = min(res)
#             print(f,cls,resAIC)
#
#             # 将结果写入文件
#             with open('C:/Users/Administrator/Desktop/R2022.3.12/aicResult.csv', mode='a') as filename:
#                 filename.write(f)
#                 filename.write('\t')
#                 filename.write(str(cls))
#                 filename.write('\t')
#                 filename.write(str(resAIC))
#                 filename.write('\t')
#                 filename.write('\n')

def findAllFile():
            filepath = 'D:/Isla/StudyinHK/paper/result/input/3t5_A.csv'
            test = np.genfromtxt(filepath, delimiter=',')
            data = np.vstack(test[:, :-1])

            res = list()
            for cls in range(2,len(data)):
                centroids, data, assignments = k_means_clust(data, cls, 5, 2)
                aic = AIC(assignments,centroids,data,cls)
                res.append(aic)
                print(cls,aic,assignments)
            resAIC = min(res)
            print(cls,resAIC)

            # 将结果写入文件
            with open('D:/Isla/StudyinHK/paper/result/input/aicResult.csv', mode='a') as filename:
                filename.write(str(cls))
                filename.write('\t')
                filename.write(str(resAIC))
                filename.write('\t')
                filename.write('\n')


findAllFile()
