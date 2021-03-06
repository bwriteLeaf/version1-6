# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

import matplotlib.pyplot as plt
from FiguresHelper import FigureHelper
from DBinterfaceDraw import DBInterfaceDraw
import traceback
from pyecharts import Pie
from pyecharts_snapshot.main import make_a_snapshot

class figureGenerate:
    def __init__(self, conf,nfigzise):
        self.config = conf
        self.dbInf = DBInterfaceDraw(self.config)
        self.figureHelper = FigureHelper(nfigzise)



    def drawDistrict(self,fid,attrExpr,divideExpr,dbName,year,isPercent,complete,
                     figureText,yLable=None,picType = "bar", colorList=[]):
        try:
            dataRaw = self.dbInf.getDistrictData(attrExpr,divideExpr,"",dbName,"district",year,isPercent,complete)
            dataRaw = self.dbInf.sortList(dataRaw)
            data = [[x[1] for x in dataRaw]]
            avgRaw = self.dbInf.getDistrictData(attrExpr,divideExpr,"",dbName,"all",year,isPercent,complete)
            avg = avgRaw[0][1]
            avglist=[]
            avglist.append(avg)
            labels = [""]
            xlables = [x[0][0:2] for x in dataRaw]
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=True, hasTable=False, figureText=figureText,colorList=colorList,avg=avglist)  # 不带横线
            f = plt.figure(id)
            f.savefig(fid+'.png')
            print("图片生成完成："+fid)
        except Exception as e:
            print(traceback.print_exc())

    def drawDisease(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,
                    mainType,year, isPercent, complete,xLable=None,yLable=None,picType = "bar",
                    figureText="pass",isSort = True,textIn=False,upSort = True, colorList=[]):
        try:
            if mainType == "all":
                dataRaw = self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
                                                         dbName,"all",year,isPercent,complete)
                dataRaw = [x[0] for x in dataRaw]
                if isSort:
                    if upSort:
                        dataRaw = self.dbInf.sortList(dataRaw)
                    else:
                        dataRaw = self.dbInf.sortList(dataRaw,sortType=False)
                data = [[x[1] for x in dataRaw]]

                labels = [x[0] for x in dataRaw] #仅在画饼图时使用，含义为排序后病的名称
                xlables = [x[0] for x in dataRaw]
                id = self.basicDraw(picType, data, labels, xlables,xLable=xLable, yLable=yLable,
                                    hline=False, hasTable=False, figureText=figureText,textIn=textIn,
                                    colorList=colorList)  # 不带横线
                f = plt.figure(id)
                f.savefig(fid+'.png')
                print("图片生成完成：" + fid)
            else:
                pass
        except Exception as e:
            print(traceback.print_exc())


    def drawDiseaseYear(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,year,
                        n, isPercent, complete,yLable=None,picType = "bar",isSort = True):
        try:
            dataRawList = []

            for i in range(0,n):
                yearNow = year - (n - 1 - i)
                dbNameNow = dbName[0:len(dbName) - 4] + str(yearNow)
                dataNow = self.dbInf.getDiffDistrictData(attrExprList,divideExprList,diseaseNameList,
                                                         dbNameNow,"all",yearNow,isPercent,complete)

                dataRawList.append(dataNow)

            dataRaw = self.dbInf.timeArray(dataRawList)

            if isSort:
                dataRaw = self.dbInf.sortArray(dataRaw)
            else:
                dataRaw = self.dbInf.noSortArray(dataRaw)

            data = []
            labels = []
            for i in range(0, n):
                data.append([x[i+1] for x in dataRaw])
                labels.append(str(year-(n-1-i)))

            xlables = [x[0] for x in dataRaw]
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=False, hasTable=False, figureText="pass")  # 不带横线
            f = plt.figure(id)
            f.savefig(fid+'.png')
            print("图片生成完成：" + fid)
        except Exception as e:
            print(traceback.print_exc())

    def drawDiseaseDistrict(self, fid, attrExprList, divideExprList, diseaseNameList, dbName, year, isPercent,
                            complete,picType = "sbar",yLable=None,hline=True, hasTable=False,
                            figureText="", colorList=[],gridcol=(12,11),export=False):
        try:
            if export:
                dataRaw = [['福田区',21000,23241],['宝安区',16000, 20955],['龙岗区',12400, 11904],
                          ['南山区',7500,13708],['龙华新区',5372, 7072],['罗湖区',3500, 7278],
                          ['坪山新区',1660,2788],['光明新区',1500, 2000],['盐田区',500, 1066],
                          ['大鹏新区',468, 706]]
                dataRaw = sorted(dataRaw, key=lambda dataRaw: dataRaw[1], reverse=1)
            else:
                dataRaw = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                         dbName, "district", year, isPercent, complete)
                dataRaw = self.dbInf.sortArray(dataRaw)
            data = []
            avglist = []
            for i in range(0, len(diseaseNameList)):
                data.append([x[i+1] for x in dataRaw])
                avgRaw = self.dbInf.getDistrictData(attrExprList[i], divideExprList[i], "", dbName, "all", year,
                                                    isPercent, complete)
                avg = avgRaw[0][1]
                avglist.append(avg)

            xlables = [x[0][0:2] for x in dataRaw]
            id = self.basicDraw(picType, data, diseaseNameList, xlables, yLable=yLable,
                                hline=hline, hasTable=hasTable, figureText=figureText,
                                colorList=colorList,gridcol=gridcol,isPercent=isPercent,
                                avg=avglist)  # 不带横线
            f = plt.figure(id)
            f.savefig(fid + '.png')
            print("图片生成完成：" + fid)
        except Exception as e:
            print(traceback.print_exc())


    def drawYearDistrict(self, fid, attrExpr, divideExpr, dbName, year, n, isPercent,
                            complete,picType = "bar",yLable=None,hline=False, figureText="",
                         colorList=[],hasTable=True):
        try:
            dataRawList = []
            avgList = []

            for i in range(0, n):
                yearNow = year - (n - 1 - i)
                dbNameNow = dbName.replace(str(year),str(yearNow))
                attrExprNow = attrExpr.replace(str(year),str(yearNow))
                divideExprNow = divideExpr.replace(str(year),str(yearNow))
                dataNow = self.dbInf.getDistrictData(attrExprNow, divideExprNow, "", dbNameNow, "district", yearNow, isPercent,
                                                     complete)
                dataRawList.append(dataNow)

                avgRaw = self.dbInf.getDistrictData(attrExprNow, divideExprNow, "", dbNameNow, "all", yearNow, isPercent,
                                                     complete)
                avg = avgRaw[0][1]
                avgList.append(avg)


            dataRaw = self.dbInf.sortArray(dataRawList)

            data = []
            labels = []
            for i in range(0, n):
                data.append([x[i + 1] for x in dataRaw])
                if figureText =="case":
                    labels.append(str(year - (n - 1 - i))+"年")
                else:
                    labels.append(str(year - (n - 1 - i)))

            xlables = [x[0][0:2] for x in dataRaw]
            id = self.basicDraw(picType, data, labels, xlables, yLable=yLable,
                                hline=hline, hasTable=hasTable, figureText=figureText,
                                colorList=colorList,avg=avgList)  # 不带横线
            f = plt.figure(id)
            f.savefig(fid + '.png')
            print("图片生成完成：" + fid)
        except Exception as e:
            print(traceback.print_exc())

		#drawDisease2() attrExprList=[[男病1，男病2，男病3],[女病1，女病2，女病3]] 逐个调用单个的函数
        # labels = [男,女] xlables = [病1，病2，病3]
		#添加到List

    def drawDisease2(self, fid, attrExprList, divideExprList, labels, xlables, dbName, year, isSort, isPercent,
                         complete,picType = "bar",yLable=None,xLable=None,figureText="",
                     colorList=[]):
        try:
            dataRawList = []
            n = len(labels)

            for i in range(0, n):
                dataNow = self.dbInf.getDiffDistrictData(attrExprList[i], divideExprList[i], xlables,
                                                         dbName, "all", year, isPercent, complete)
                dataRawList.append(dataNow)

            dataRaw = self.dbInf.timeArray(dataRawList)
            if isSort:
                if picType =='hbar':
                    dataRaw = self.dbInf.sortArray(dataRaw,sortType=False)
                else:
                    dataRaw = self.dbInf.sortArray(dataRaw)
            else:
                dataRaw = self.dbInf.noSortArray(dataRaw)

            data = []
            for i in range(0, n):
                data.append([x[i + 1] for x in dataRaw])

            xlables = [x[0] for x in dataRaw]
            id = self.basicDraw(picType,data, labels, xlables, yLable=yLable, xLable=xLable,
                                hline=False, hasTable=False, figureText=figureText,colorList=colorList)  # 不带横线
            f = plt.figure(id)
            f.savefig(fid + '.png')
            print("图片生成完成：" + fid)
        except Exception as e:
            print(traceback.print_exc())

    # diseaseNameList=[内环['风险人群', '一般人群'],外环['女方风险', '男方风险', '双方风险', '一般人群']]
    # attrExprList=[内环表达式[],外环表达式[]]
    # data=[内环值[],外环值[]]
    def drawTwoPie(self,fid, attrExprList, divideExprList,diseaseNameList, dbName,
                    year, isPercent, complete):
        try:
            innerLabel = diseaseNameList[0]
            outerLabel = diseaseNameList[1]

            dataList = []
            n = len(diseaseNameList)

            for i in range(0, n):
                dataNow = self.dbInf.getDiffDistrictData(attrExprList[i], divideExprList[i], diseaseNameList[i],
                                                         dbName, "all", year, isPercent, complete)
                dataNow = [x[0] for x in dataNow]
                data = [x[1] for x in dataNow]
                dataList.append(data)


            large = 1.3
            size = 0.8
            pie = Pie("", title_pos='center', width=800*size, height=480*size)
            pie.add("", outerLabel, dataList[1],
                    radius=[40 * large, 55 * large], is_label_show=True, legend_pos='left')
            pie.add("", innerLabel, dataList[0], radius=[0 * large, 30 * large], legend_orient='vertical',
                    legend_pos='left', is_label_show=True, label_formatter='{d}%', label_pos='inside')
            pie.render()
            make_a_snapshot('render.html', fid+'.png')
            print("图片生成完成：" + fid)

        except Exception as e:
            print(traceback.print_exc())


            # diseaseNameList=[内环['风险人群', '一般人群'],外环['女方风险', '男方风险', '双方风险', '一般人群']]

        # attrExprList=[内环表达式[],外环表达式[]]
        # data=[内环值[],外环值[]]
        def drawTwoPie(self, fid, attrExprList, divideExprList, diseaseNameList, dbName,
                       year, isPercent, complete):
            try:
                innerLabel = diseaseNameList[0]
                outerLabel = diseaseNameList[1]

                dataList = []
                n = len(diseaseNameList)

                for i in range(0, n):
                    dataNow = self.dbInf.getDiffDistrictData(attrExprList[i], divideExprList[i], diseaseNameList[i],
                                                             dbName, "all", year, isPercent, complete)
                    dataNow = [x[0] for x in dataNow]
                    data = [x[1] for x in dataNow]
                    dataList.append(data)

                large = 1.3
                size = 0.8
                pie = Pie("", title_pos='center', width=800 * size, height=480 * size)
                pie.add("", outerLabel, dataList[1],
                        radius=[40 * large, 55 * large], is_label_show=True, legend_pos='left')
                pie.add("", innerLabel, dataList[0], radius=[0 * large, 30 * large], legend_orient='vertical',
                        legend_pos='left', is_label_show=True, label_formatter='{d}%', label_pos='inside')
                pie.render()
                make_a_snapshot('render.html', fid + '.png')
                print("图片生成完成：" + fid)

            except Exception as e:
                print(traceback.print_exc())


        # diseaseNameList=['女方风险', '男方风险', '双方风险', '一般人群']
        # attrExprList=表达式[]
        # data=值[]
    def drawOnePie(self, fid, attrExprList, divideExprList, diseaseNameList, dbName,
                       year, isPercent, complete):
        try:

            dataList = []


            dataNow = self.dbInf.getDiffDistrictData(attrExprList, divideExprList, diseaseNameList,
                                                         dbName, "all", year, isPercent, complete)
            dataNow = [x[0] for x in dataNow]
            data = [x[1] for x in dataNow]
            dataList.append(data)

            large = 1.3
            size = 0.8
            pie = Pie("", title_pos='center', width=800 * size, height=480 * size)
            pie.add("", diseaseNameList, dataList[0], radius=[0 * large, 45 * large], legend_orient='vertical',
                    is_label_show=True, legend_pos='left', label_formatter='{d}%', label_pos='left')
            pie.render()
            make_a_snapshot('render.html', fid + '.png')
            print("图片生成完成：" + fid)

        except Exception as e:
            print(traceback.print_exc())

    def basicDraw(self,mainType,dataList, dataLabelList, xAxisLabelList, xLable=None, yLable=None,
                    hline=False, hasTable=False, figureText="",colorList = [],textIn=False,gridcol=(12,11),
                  isPercent=True,avg=[]):
        try:
            p = None
            if mainType == "bar":
                p = self.figureHelper.compoundBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable,
                        hline, hasTable, figureText, colorList,isPercent,gridcol=gridcol,avg=avg)
            elif mainType == "sbar":
                p = self.figureHelper.stackedBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable,gridcol)
            elif mainType == "spbar":
                p = self.figureHelper.stackedBarPlotWithPercentage(dataList, dataLabelList, xAxisLabelList, xLable,
                                                                   yLable,gridcol,hasTable=hasTable,isPercent=isPercent)
            elif mainType == "stbar":
                p = self.figureHelper.stackedBarPlotWithTable(dataList, dataLabelList, xAxisLabelList, xLable,
                                                              yLable,gridcol,isPercent=isPercent)
            elif mainType == "hbar":
                p = self.figureHelper.horizontalBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable, colorList)
            elif mainType == "hsbar":
                p = self.figureHelper.stackedHorizontalBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable,gridcol)
            elif mainType == "hspbar":
                p = self.figureHelper.stackedHorizontalBarPlotWithPercentage(dataList, dataLabelList, xAxisLabelList, xLable, yLable,gridcol)
            elif mainType == "line":
                p = self.figureHelper.lineChartPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            elif mainType == "pie":
                p = self.figureHelper.pieChartPlot(dataList[0], dataLabelList,textIn)
            elif mainType == "pyd":
                p = self.figureHelper.pyramidBarPlot(dataList, dataLabelList, xAxisLabelList, xLable, yLable)
            else:
                pass

            return p

        except Exception as e:
            print(traceback.print_exc())

    def finish(self):
        self.figureHelper.finish()




