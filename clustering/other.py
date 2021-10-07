import os
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('../datasets/test.csv',delimiter=' ')

def kmeans(data, k):
    # 计算样本的个数
    numSamples = data.shape[0]  # 80

    # clusterData样本的属性，行是代表各个样本，第一列保存样本属于哪个簇，第二列保存样本跟它所属簇的距离
    clusterData = np.zeros((numSamples, 2)) # 80 * 2

    # 决定质心是否要改变
    clusterChanged = True
    # 初始化质心
    centroids = initCentroids(data, k)  # k 个初始质心
    while clusterChanged: # 死循环   迭代次数不确定
        clusterChanged = False  # 质心改变 后面会再改过来
        # 循环每一个样本
        for i in range(numSamples):  # 80,对所有的样本点
            # 最小距离
            minDist = 100000.0  # 最小值 定义成 一个超大值
            # 定义样本所属的簇
            minIndex = 0
            # 循环计算每一个质心和样本的距离
            for j in range(k):     # 4，和4个质心的距离
                # 计算距离
                distance = euclDistance(centroids[j ,:] ,data[i ,:])
                if distance < minDist:  # 类似 冒泡排序
                    # 更新最小距离
                    minDist = distance
                    # 更新样本所属的簇
                    minIndex = j
                    # 更新样本保存的最小距离
                    clusterData[i ,1] = distance

            # 如果有一个样本所属的簇发生改变
            if clusterData[i ,0] != minIndex:
                # 质心发生改变
                clusterChanged = True
                # 更新样本的簇
                clusterData[i ,0] = minIndex
            # 当if为假,质心不发生改变,下面两行不运行,带着开头的clusterChanged = False 回到 while 结束循环

        # 更新质心
        for j in range(k):
            # 获取第j个簇所有的样本所在的 索引
            cluster_index = np.nonzero(clusterData[: ,0 ]= =j) # np.nonzero()  返回非零元素的索引
            # 第j个簇所有的样本点
            pointsInCluster = data[cluster_index]
            # 计算质心
            centroids[j ,:] = np.mean(pointsInCluster ,axis=0)

    return centroids, clusterData



centroids,clusterData = kmeans(data, k)