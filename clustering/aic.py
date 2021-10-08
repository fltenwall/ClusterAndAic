# 计算AIC
# centroids 分类结果的数据 拟合数据 [[...],[...]]
# assignments 分类 {0: [0, 3, 5, 6, 7, 9, 10], 1: [1, 2, 4, 8]}
# data 要进行分类的线性数据
# cls 分类的类别数
# AIC = nln(SSR/n) + 2k
# SSR是残差平方和
def AIC(assignments,centroids,data,cls):
    ssr = 0
    aic = 0
    for i, (k, v) in enumerate(assignments.items()):
        for (index,val) in enumerate(v):
            print("val",val)
            for (indexI,valI) in enumerate(centroids[k]):
                print("indexI",indexI,"valI",valI)
                ssr += pow(data[val][indexI] - valI,2)
                print('ssr',ssr)
    aic = 2 * cls + len(data) * math.log(ssr / len(data))
    return aic
