# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from FiguresHelper import FigureHelper
from DBinterface import DBInterface
import pandas as pd
from configuration import Config
from interpreter import Interpreter

class figureGenerate:
    def __init__(self, conf, inter):
        self.config = conf
        self.inter = inter
        self.dbInf = DBInterface(self.config, self.inter)
        self.figureHelper = FigureHelper([8, 4.8])



    def drawDistrict(self,fid,attrExpr,divideExpr,dbName,year,isPercent,complete,figureText):
        dataRaw = self.dbInf.getDistrictData(attrExpr,divideExpr,"",dbName,"district",year,isPercent,complete)
        dataRaw = self.dbInf.sortList(dataRaw)
        data = [[x[1] for x in dataRaw]]
        labels = [""]
        xlables = [x[0][0:2] for x in dataRaw]
        id =self.figureHelper.compoundBarPlot(data, labels, xlables,True,False,figureText)
        f = plt.figure(id)
        f.savefig('图'+str(fid)+'.png')

    def drawDisease(self,fid, attrExprList, divideExprList,diseaseNameList, dbName, mainType,year, isPercent, complete):
        if mainType == "all":
            dataRaw = self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
                                                     dbName,"all",year,isPercent,complete)
            dataRaw = [x[0] for x in dataRaw]
            dataRaw = self.dbInf.sortList(dataRaw)
            data = [[x[1] for x in dataRaw]]
            labels = diseaseNameList
            xlables = [x[0] for x in dataRaw]
            id =self.figureHelper.compoundBarPlot(data, labels, xlables,False,False,"") #不带横线
            f = plt.figure(id)
            f.savefig('图'+str(fid)+'.png')
        elif mainType == "district":
            dataRaw = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                     dbName, "district", year, isPercent, complete)
            dataRaw = self.dbInf.sortArray(dataRaw)
            data = [[x[1] for x in dataRaw], [x[2] for x in dataRaw]]
            xlables = [x[0][0:2] for x in dataRaw]
            labels = diseaseNameList
            id = self.figureHelper.compoundBarPlot(data, labels, xlables, False, True, "")  # 不带横线
            f = plt.figure(id)
            f.savefig('图' + str(fid) + '.png')
        else:
            pass

    def drawDiseaseYear(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,year,n, isPercent, complete):

        dataRawList = []

        for i in range(0,n):
            # dataNow = self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
            #                                          dbName,"all",year-(n-1-i),isPercent,complete)
            dataNow = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                     dbName, "all", year, isPercent, complete)
            dataRawList.append(dataNow)

        dataRaw = self.dbInf.timeArray(dataRawList)
        dataRaw = self.dbInf.sortArray(dataRaw)

        data = []
        labels = []
        for i in range(0, n):
            data.append([x[i+1] for x in dataRaw])
            labels.append(str(year-(n-1-i)))

        xlables = [x[0] for x in dataRaw]
        id =self.figureHelper.compoundBarPlot(data, labels, xlables,False,False,"") #不带横线
        f = plt.figure(id)
        f.savefig('图'+str(fid)+'.png')

    def drawDiseaseDistrict(self, fid, attrExprList, divideExprList, diseaseNameList, dbName, year, isPercent,
                            complete):

        dataRaw = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                 dbName, "district", year, isPercent, complete)
        dataRaw = self.dbInf.sortArray(dataRaw)
        data = []
        for i in range(0, len(attrExprList)):
            data.append([x[i+1] for x in dataRaw])

        xlables = [x[0][0:2] for x in dataRaw]
        id = self.figureHelper.stackedBarPlotWithTable(data, diseaseNameList, xlables, "百分比%")
        f = plt.figure(id)
        f.savefig('图' + str(fid) + '.png')


    def drawYearDistrict(self, fid, attrExpr, divideExpr, dbName, year, n, isPercent,
                            complete):

        dataRawList = []

        for i in range(0, n):
            # dataNow = self.dbInf.getDistrictData(attrExpr, divideExpr, "", dbName, "district", year - (n - 1 - i), isPercent,
            #                                      complete)
            dataNow = self.dbInf.getDistrictData(attrExpr, divideExpr, "", dbName, "district", year, isPercent,
                                                 complete)

            dataRawList.append(dataNow)

        dataRaw = self.dbInf.sortArray(dataRawList)

        data = []
        labels = []
        for i in range(0, n):
            data.append([x[i + 1] for x in dataRaw])
            labels.append(str(year - (n - 1 - i)))

        xlables = [x[0][0:2] for x in dataRaw]
        id = self.figureHelper.compoundBarPlot(data, labels, xlables, False, False, "")  # 不带横线
        f = plt.figure(id)
        f.savefig('图' + str(fid) + '.png')
		
		#drawDisease2() [[男病1，男病2，男病3],[女病1，女病2，女病3]] 逐个调用单个的函数
		#添加到List

    def finish(self):
        self.figureHelper.finish()




