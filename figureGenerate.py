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
import traceback

class figureGenerate:
    def __init__(self, conf, inter):
        self.config = conf
        self.inter = inter
        self.dbInf = DBInterface(self.config, self.inter)
        self.figureHelper = FigureHelper([8, 4.8])



    def drawDistrict(self,fid,attrExpr,divideExpr,dbName,year,isPercent,complete,
                     figureText,yLable=None,picType = "bar", colorList=[]):
        try:
            dataRaw = self.dbInf.getDistrictData(attrExpr,divideExpr,"",dbName,"district",year,isPercent,complete)
            dataRaw = self.dbInf.sortList(dataRaw)
            data = [[x[1] for x in dataRaw]]
            labels = [""]
            xlables = [x[0][0:2] for x in dataRaw]
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=True, hasTable=False, figureText=figureText,colorList=colorList)  # 不带横线
            f = plt.figure(id)
            f.savefig(str(fid)+'.png')
        except Exception as e:
            print(traceback.print_exc())

    def drawDisease(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,
                    mainType,year, isPercent, complete,yLable=None,picType = "bar"):
        try:
            if mainType == "all":
                dataRaw = self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
                                                         dbName,"all",year,isPercent,complete)
                dataRaw = [x[0] for x in dataRaw]
                dataRaw = self.dbInf.sortList(dataRaw)
                data = [[x[1] for x in dataRaw]]
                labels = diseaseNameList
                xlables = [x[0] for x in dataRaw]
                id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                    hline=False, hasTable=False, figureText="")  # 不带横线
                f = plt.figure(id)
                f.savefig(str(fid)+'.png')
            else:
                pass
        except Exception as e:
            print(traceback.print_exc())


    def drawDiseaseYear(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,year,
                        n, isPercent, complete,yLable=None,picType = "bar"):
        try:
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
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=False, hasTable=False, figureText="pass")  # 不带横线
            f = plt.figure(id)
            f.savefig(str(fid)+'.png')
        except Exception as e:
            print(traceback.print_exc())

    def drawDiseaseDistrict(self, fid, attrExprList, divideExprList, diseaseNameList, dbName, year, isPercent,
                            complete,picType = "sbar",yLable=None,hline=True, hasTable=False, figureText="", colorList=[]):
        try:
            dataRaw = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                     dbName, "district", year, isPercent, complete)
            dataRaw = self.dbInf.sortArray(dataRaw)
            data = []
            for i in range(0, len(attrExprList)):
                data.append([x[i+1] for x in dataRaw])

            xlables = [x[0][0:2] for x in dataRaw]
            id = self.basicDraw(picType, data, diseaseNameList, xlables, yLable=yLable,
                                hline=hline, hasTable=hasTable, figureText=figureText, colorList=colorList)  # 不带横线
            f = plt.figure(id)
            f.savefig(str(fid) + '.png')
        except Exception as e:
            print(traceback.print_exc())


    def drawYearDistrict(self, fid, attrExpr, divideExpr, dbName, year, n, isPercent,
                            complete,picType = "bar",yLable=None):
        try:
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
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=False, hasTable=True, figureText="")  # 不带横线
            f = plt.figure(id)
            f.savefig(str(fid) + '.png')
        except Exception as e:
            print(traceback.print_exc())

		#drawDisease2() [[男病1，男病2，男病3],[女病1，女病2，女病3]] 逐个调用单个的函数
        # labels = [男,女] xlables = [病1，病2，病3]
		#添加到List

    def drawDisease2(self, fid, attrExprList, divideExprList, labels, xlables, dbName, year, isSort, isPercent,
                         complete,picType = "bar"):
        try:
            dataRawList = []
            n = len(labels)

            for i in range(0, n):
                dataNow = self.dbInf.getDiffDistrictData(attrExprList[i], divideExprList[i], xlables,
                                                         dbName, "all", year, isPercent, complete)
                dataRawList.append(dataNow)

            dataRaw = self.dbInf.timeArray(dataRawList)
            if isSort:
                dataRaw = self.dbInf.sortArray(dataRaw)
            else:
                dataRaw = self.dbInf.noSortArray(dataRaw)

            data = []
            for i in range(0, n):
                data.append([x[i + 1] for x in dataRaw])

            xlables = [x[0] for x in dataRaw]
            id = self.basicDraw(picType,data, labels, xlables,
                                hline=False, hasTable=False, figureText="")  # 不带横线
            f = plt.figure(id)
            f.savefig(str(fid) + '.png')
        except Exception as e:
            print(traceback.print_exc())

    def basicDraw(self,mainType,dataList, dataLabelList, xAxisLabelList, xLable=None, yLable=None,
                    hline=False, hasTable=False, figureText="",colorList = []):
        try:
            p = None
            if mainType == "bar":
                p = self.figureHelper.compoundBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable,
                        hline, hasTable, figureText, colorList)
            elif mainType == "sbar":
                p = self.figureHelper.stackedBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "spbar":
                p = self.figureHelper.stackedBarPlotWithPercentage(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "stbar":
                p = self.figureHelper.stackedBarPlotWithTable(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "hbar":
                p = self.figureHelper.horizontalBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "hsbar":
                p = self.figureHelper.stackedHorizontalBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "hspbar":
                p = self.figureHelper.stackedHorizontalBarPlotWithPercentage(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "line":
                p = self.figureHelper.lineChartPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "pie":
                p = self.figureHelper.pieChartPlot(dataList[0], dataLabelList)
            elif mainType == "pyd":
                p = self.figureHelper.pyramidBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            else:
                pass

            return p

        except Exception as e:
            print(traceback.print_exc())

    def finish(self):
        self.figureHelper.finish()




