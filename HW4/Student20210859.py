import sys
from os import listdir
import numpy as np
import operator

def createDataSet(dirname):
    labels = []
    trainingFileList = listdir(dirname)
    m = len(trainingFileList)
    matrix = np.zeros((m, 1024)) # 반환된 vector를 담을 곳

    for i in range(m): # 파일의 개수만큼 반복
        fileNameStr = trainingFileList[i]
        answer = int(fileNameStr.split('_')[0]) # 정답 저장 
        labels.append(answer)
        matrix[i, :] = getVector(dirname + '/' + fileNameStr)
    return matrix, labels 

def getVector(filename):
    vector = np.zeros((1, 1024), dtype=int)  # 32 * 32 = 1024
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
    return vector
    
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffmat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffmat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}    
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    train = sys.argv[1]
    test = sys.argv[2]

    testList = listdir(test)
    length = len(testList)

    mat, labels = createDataSet(train)

    for k in range(1, 20):
        count = 0
        error = 0

        for i in range(length):
            answer = int(testList[i].split('_')[0])
            testData = getVector(test + '/' + testList[i])
            classfyRs = classify0(testData, mat, labels, k)

            count += 1
            if answer != classfyRs:
                error += 1

        print(int(error / count * 100))