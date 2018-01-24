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

    def drawTwoDistrict(self):
        list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
        list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
        labels = ['偶尔', '经常']
        dataRaw = self.dbInf.getDiffDistrictData(list_a,list_d,"exam",self.config.year,True)
        dataRaw = self.dbInf.sortArray(dataRaw)
        data = [[x[1] for x in dataRaw], [x[2] for x in dataRaw]]
        xlables = [x[0][0:2] for x in dataRaw]
        id = self.figureHelper.stackedBarPlotWithTable(data, labels, xlables,"百分比%")
        f = plt.figure(id)
        f.savefig('图96.png')

    def drawOneDistrict(self,fid,attrExpr,divideExpr,dbName,year,isPercent,complete,figureText):
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

    def drawDiseaseYear(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,year, isPercent, complete):

        dataRawList =[self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
                                                     dbName,"all",year-0,isPercent,complete),
                      self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                     dbName, "all", year, isPercent, complete)
                    ]
        dataRaw = self.dbInf.timeArray(dataRawList)
        dataRaw = self.dbInf.sortArray(dataRaw)
        data = [[x[1] for x in dataRaw], [x[2] for x in dataRaw]]
        xlables = [x[0] for x in dataRaw]
        labels = [str(year-1),str(year)]
        id =self.figureHelper.compoundBarPlot(data, labels, xlables,False,False,"") #不带横线
        f = plt.figure(id)
        f.savefig('图'+str(fid)+'.png')

    def finish(self):
        self.figureHelper.finish()




