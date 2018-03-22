# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pdb
import os
from pyecharts import Pie
from pyecharts_snapshot.main import make_a_snapshot

class FigureHelper:

    def __init__(self, nfigsize):
        # 保存当前工作目录
        self.cwd = os.getcwd()
        # 切换工作目录至模板文件所在目录
        os.chdir('DrawReal')
        self.nfigsize = nfigsize
        self.gernerateFigure = self.gernerateFigureWrapper()
        matplotlib.rcParams['font.sans-serif'] = 'Microsoft YaHei'

    def finish(self):
        os.chdir(self.cwd)

    # 生成一个图表，返回其ID
    def gernerateFigureWrapper(self):  # 第一个参数为用户指定的图片大小,如 [8, 4.8]
        figureID = 0

        def func():
            nonlocal figureID
            '''   
            if len(args2) ==2:
                userFigsize = args2[0]
                nfigsize = userFigsize
            else:                        
            '''
            # nfigsize = [8, 25]

            plt.figure(str(figureID), figsize=self.nfigsize)
            figureID += 1
            return str(figureID - 1)

        return func


    # 基础的累积条图
    # dataList: 待绘制的数据集
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴标签
    # yLabel: y轴标签，可为空
    def stackedBarPlot(self,dataList, dataLabelList, xAxisLabelList,
                       xLable=None,yLabel=None,gridcol=(12,11)):

        case_cnt = len(dataList)  # 颜色组

        figureId = self.gernerateFigure()
        if len(dataList) == 0:
            return None
        legends = []
        xIndexes = np.arange(len(dataList[0]))
        yOffset = np.zeros(len(dataList[0]))

        if case_cnt >=4:
            c0 = gridcol[0]
            c1 = gridcol[1]
            plt.subplot2grid((1, c0), (0, 0), colspan=c1, rowspan=1)

        for i in range(0, len(dataList)):
            l = plt.bar(xIndexes, dataList[i], bottom=yOffset, width=0.35)
            legends.append(l)
            yOffset = yOffset + dataList[i]

        if yLabel is not None:
            plt.ylabel(yLabel)
        plt.xticks(xIndexes, xAxisLabelList)

        bbox_to_anchor = (0.25, 1.02, 0.5, .102)
        if case_cnt >=4:
            bbox_to_anchor = (1.05, 0.65)
            plt.legend(legends, dataLabelList, bbox_to_anchor=bbox_to_anchor, loc=2,
                        borderaxespad=0.)
        else:
            plt.legend(legends, dataLabelList, bbox_to_anchor=bbox_to_anchor, loc=3,
                       ncol=len(dataLabelList), mode="expand", borderaxespad=0.)


        # plt.legend(legends, dataLabelList, bbox_to_anchor=(0.25, -.1, 0.5, -.1), loc=3,
        #           ncol=4, mode="expand", borderaxespad=0.)

        return figureId


    # 带表格的累积条图
    # 表格的条目为dataLabelList中的值
    # dataList: 待绘制的数据集
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴标签
    # yLabel: y轴标签，可为空
    # TODO: 调整字体大小
    def stackedBarPlotWithTable(self,dataList, dataLabelList, xAxisLabelList,
                                xLable=None,yLabel=None,gridcol=(12,11),isPercent=True):
        figureId = self.stackedBarPlot(dataList, dataLabelList, xAxisLabelList,
                                       xLable=xLable, yLabel=yLabel, gridcol=gridcol)

        case_cnt = len(dataList)  # 颜色组
        cellText = []
        for i in range(0, case_cnt):
            if isPercent:
                cellApp = [("%.2f" % x) for x in dataList[i]]
            else:
                cellApp = [("%d" % x) for x in dataList[i]]
            cellText.append(cellApp)
        table = plt.table(cellText=cellText,
                          rowLabels=dataLabelList,
                          colLabels=xAxisLabelList,
                          loc='bottom')
        plt.subplots_adjust(left=0.2, bottom=0.2)

        plt.xticks([])
        return figureId


    # 绘制百分条图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴标签
    def stackedBarPlotWithPercentage(self,dataList, dataLabelList, xAxisLabelList,
                                     xLable=None,yLabel=None,gridcol=(12,11),hasTable=False,isPercent=True):
        figureId = self.stackedBarPlot(dataList, dataLabelList, xAxisLabelList,
                                       xLable=xLable, yLabel=yLabel, gridcol=gridcol)
        plt.figure(figureId)
        yIndex = np.arange(0, 110, 10)
        plt.yticks(yIndex, list(map(lambda x: "%d%%" % x, yIndex)))
        if hasTable:
            case_cnt = len(dataList)  # 颜色组
            cellText = []
            for i in range(0, case_cnt):
                if isPercent:
                    cellApp = [("%.2f" % x) for x in dataList[i]]
                else:
                    cellApp = [("%d" % x) for x in dataList[i]]
                cellText.append(cellApp)
            table = plt.table(cellText=cellText,
                              rowLabels=dataLabelList,
                              colLabels=xAxisLabelList,
                              loc='bottom')
            plt.subplots_adjust(left=0.2, bottom=0.2)

            plt.xticks([])

        return figureId


    # 水平的基础累积条图
    # dataList: 待绘制的数据集
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: y轴标签
    # yLabel: y轴标签，可为空
    def stackedHorizontalBarPlot(self,dataList, dataLabelList, yAxisLabelList,
                                 xLable=None,yLabel=None,gridcol=(12,11)):
        matplotlib.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        figureId = self.gernerateFigure()
        if len(dataList) == 0:
            return None
        legends = []

        case_cnt = len(dataList)  # 颜色组
        n_groups = len(dataList[0])  # y轴标签个数

        yAxisLabelListr = list(reversed(yAxisLabelList))

        yIndexes = np.arange(n_groups)
        xOffset = np.zeros(n_groups)

        if case_cnt >=4:
            c0 = gridcol[0]
            c1 = gridcol[1]
            plt.subplot2grid((1, c0), (0, 0), colspan=c1, rowspan=1)

        for i in range(0, case_cnt):
            dataListIr = list(reversed(dataList[i]))
            l = plt.barh(yIndexes, dataListIr, 0.35, left=xOffset,
                         label=dataLabelList[i])
            legends.append(l)
            xOffset = xOffset + dataListIr

        if yLabel is not None:
            plt.ylabel(yLabel)
        plt.yticks(yIndexes, yAxisLabelListr)

        bbox_to_anchor = (0.25, 1.02, 0.5, .102)
        if case_cnt >= 4:
            bbox_to_anchor = (1.05, 0.65)
            plt.legend(legends, dataLabelList, bbox_to_anchor=bbox_to_anchor, loc=2,
                       borderaxespad=0.)
        else:
            plt.legend(legends, dataLabelList, bbox_to_anchor=bbox_to_anchor, loc=3,
                       ncol=len(dataLabelList), mode="expand", borderaxespad=0.)

        return figureId


    # 绘制水平百分条图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴标签
    def stackedHorizontalBarPlotWithPercentage(self,dataList, dataLabelList, yAxisLabelList,
                                               xLable=None,yLabel=None,gridcol=(12,11)):
        figureId = self.stackedHorizontalBarPlot(dataList, dataLabelList, yAxisLabelList,
                                                 xLable=xLable,yLabel=yLabel,gridcol=gridcol)
        plt.figure(figureId)
        xIndex = np.arange(0, 110, 10)
        plt.xticks(xIndex, list(map(lambda x: "%d%%" % x, xIndex)))

        return figureId


    # TODO 修改图例位置到不重合

    # 水平的金字塔条图
    # dataList: 待绘制的数据集
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # yAxisLabelList: y轴标签
    # yLabel: y轴标签，可为空
    def pyramidBarPlot(self,dataList, dataLabelList, yAxisLabelList,xLable=None,yLabel=None):
        matplotlib.rcParams['font.sans-serif'] = 'Microsoft YaHei'
        figureId = self.gernerateFigure()
        if len(dataList) == 0:
            return None
        legends = []

        case_cnt = len(dataList)  # 颜色组
        n_groups = len(dataList[0])  # y轴标签个数

        yAxisLabelListr = list(reversed(yAxisLabelList))

        yIndexes = np.arange(n_groups)
        xOffset = np.zeros(n_groups)
        dataListMinus = list(reversed(dataList[1]))

        for i in range(0, case_cnt):
            dataListIr = list(reversed(dataList[i]))
            if i == 0:
                l = plt.barh(yIndexes, dataListIr, 0.35, left=xOffset,
                             label=dataLabelList[i])
                legends.append(l)
            if i == 1:
                xOffset = xOffset - dataListIr
                l = plt.barh(yIndexes, dataListIr, 0.35, left=xOffset,
                             label=dataLabelList[i])
                legends.append(l)

        if yLabel is not None:
            plt.ylabel(yLabel)
        plt.yticks(yIndexes, yAxisLabelListr)
        xIndex = [-100, -80,
                  -60, -40, -20, 0, 20, 40, 60, 80, 100]
        plt.xticks(xIndex, [100, 80, 60, 40, 20, 0, 20, 40, 60, 80, 100])
        plt.legend(legends, dataLabelList, bbox_to_anchor=(0.25, 1.02, 0.5, .102), loc=3,
                   ncol=len(dataLabelList), mode="expand", borderaxespad=0.)
        return figureId


    # 绘制带横线的复式条图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴标签
    # vline 是否带横线，TRUE表示带均值横线，包括两条
    # hasTable 是否带表格，TRUE表示带表格
    # figureText: 长度为0表示不添加文字 ，否则添加“：数值”
    # isPercent 用于表示显示的数字是否为小数 包括矩形上面的和表格中的，表格中保留2位小数点
    def compoundBarPlot(self,dataList, dataLabelList, xAxisLabelList, xLable=None, yLable='百分比（%）',
                        hline = False, hasTable = False,figureText = "",colorList = [],
                        isPercent=True,indent = False,gridcol=(12,11),avg=[]):
        case_cnt = len(dataList)
        n_groups = len(dataList[0])
        legends = []
        bar_width = 0.35
        indent_width = 0.1
        opacity = 0.9
        if figureText == "case":
            opacity = 0.8
        xIndexes = np.arange(n_groups)

        figureId = self.gernerateFigure()

        if n_groups <= 3 and case_cnt==1:
            bar_width = 0.25
            xIndexes = np.arange(1,3) * 0.4
            print(xIndexes)

        if case_cnt >= 3:
            if case_cnt == 3:
                bar_width = 0.2
            elif case_cnt == 4:
                bar_width = 0.18
            c0 = gridcol[0]
            c1 = gridcol[1]
            plt.subplot2grid((1, c0), (0, 0), colspan=c1, rowspan=1)


        if len(dataList) == 0:
            return None

        # xIndexes = xIndexes - (case_cnt - 1)*bar_width/2 +1

        for i in range(0, case_cnt):
            index = xIndexes + i * bar_width
            if indent:
                index = index + i * indent_width
            if len(colorList) == 0:
               l = plt.bar(index, dataList[i], bar_width, alpha=opacity,
                            label=dataLabelList[i])
            else:
                use_color = colorList[i]
                l = plt.bar(index, dataList[i], bar_width, alpha=opacity,
                            label=dataLabelList[i], color=use_color)
            legends.append(l)

            if figureText:
                rect_labels = []
                j = 0
                for rect in l:
                    # Rectangle widths are already integer-valued but are floating
                    # type, so it helps to remove the trailing decimal point and 0 by
                    # converting width to int type

                    width = rect.get_width()
                    xloc = rect.get_x() + width / 2.0
                    if isPercent:
                        showStr = '%.2f' % dataList[i][j]
                    else:
                        showStr = '%d' % dataList[i][j]

                    # Center the text vertically in the bar
                    yloc = rect.get_height()*1.02
                    label = plt.text(xloc, yloc, showStr, horizontalalignment='center',
                                     verticalalignment='center',
                                     clip_on=True)
                    rect_labels.append(label)

                    j = j + 1

            plt.ylabel(yLable)
            # ax.set_title('Scores by group and gender')

        if case_cnt >= 2:
            if case_cnt >= 3:
                bbox_to_anchor = (1.05, 0.65)
                plt.legend(legends, dataLabelList, bbox_to_anchor=bbox_to_anchor, loc=2,
                           borderaxespad=0.)
            else:
                plt.legend(legends, dataLabelList, bbox_to_anchor=(0.25, 1.02, 0.5, .102), loc=3,
                       ncol=len(dataLabelList), mode="expand", borderaxespad=0.)

        if hasTable:
            cellText=[]
            for i in range(0, case_cnt):
                if isPercent:
                    cellApp = [("%.2f" % x) for x in dataList[i]]
                else:
                    cellApp = [("%d" % x) for x in dataList[i]]
                cellText.append(cellApp)


            table = plt.table(cellText=cellText,
                              rowLabels=dataLabelList,
                              colLabels=xAxisLabelList,
                              loc='bottom',
                              fontsize=0.6)
            plt.subplots_adjust(left=0.2, bottom=0.2)
            plt.xticks([])
        else:
            if indent:
                plt.xticks(xIndexes + (bar_width + indent_width) * (case_cnt - 1) / case_cnt, xAxisLabelList)
            else:
                plt.xticks(xIndexes + bar_width * (case_cnt - 1) / case_cnt, xAxisLabelList)
        if hline:
            for i in range(0, len(dataList)):
                if len(colorList) == 0:
                    use_color = '#d62728'
                else:
                    use_color = colorList[i]
                plt.axhline(avg[i],linewidth=3, color=use_color)
                if figureText == "case":
                    plt.text(n_groups * 0.7, (avg[i]) * 1.05, dataLabelList[i]+"平均水平" + '：%.2f' % (avg[i]))
                elif len(figureText) > 0 and figureText != "pass":
                    plt.text(n_groups*0.7, (avg[i])*1.05, figureText+'：%.2f' % (avg[i]))
                # TODO 修改颜色与柱颜色统一
        return figureId


    # 绘制水平复式条图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # yAxisLabelList: y轴标签
    def horizontalBarPlot(self,dataList, dataLabelList, yAxisLabelList,
                          xLable='百分比',yLabel=None, colorList=[]):
        case_cnt = len(dataList)
        n_groups = len(dataList[0])
        legends = []

        yAxisLabelListr = list(reversed(yAxisLabelList))

        bar_width = 0.35  # TODO 修改宽度适合于制定图像
        opacity = 0.9

        figureId = self.gernerateFigure()
        if len(dataList) == 0:
            return None

        yIndexes = np.arange(n_groups)
        for i in range(0, case_cnt):
            dataListIr = list(reversed(dataList[i]))
            index = yIndexes + i * bar_width
            if len(colorList) == 0:
                rects = plt.barh(index, dataListIr, bar_width, alpha=opacity,
                            label=dataLabelList[i])
            else:
                use_color = colorList[i]
                rects = plt.barh(index, dataListIr, bar_width, alpha=opacity,
                            label=dataLabelList[i], color=use_color)

            rect_labels = []
            j = 0
            for rect in rects:
                # Rectangle widths are already integer-valued but are floating
                # type, so it helps to remove the trailing decimal point and 0 by
                # converting width to int type

                width = rect.get_width()
                xloc = width
                showStr = '%.2f' % dataListIr[j]

                # Center the text vertically in the bar
                yloc = rect.get_y() + rect.get_height() / 2.0
                label = plt.text(xloc, yloc, showStr, horizontalalignment='left',
                                 verticalalignment='center',
                                 clip_on=True)
                rect_labels.append(label)

                j = j + 1

            legends.append(rects)

            plt.xlabel(xLable)
            if case_cnt >= 2:
                plt.legend(legends, dataLabelList, bbox_to_anchor=(0.25, 1.02, 0.5, .102), loc=3,
                           ncol=len(dataLabelList), mode="expand", borderaxespad=0.)

            plt.yticks(yIndexes + bar_width * (case_cnt - 1) / case_cnt, yAxisLabelListr)

        return figureId


    # 绘制饼图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    def pieChartPlot(self,dataList, dataLabelList,textIn=False):
        case_cnt = len(dataLabelList)
        figureId = self.gernerateFigure()
        legends = []
        if len(dataList) == 0:
            return None

        # if case_cnt >=4:
        #     c0 = gridcol[0]
        #     c1 = gridcol[1]
        #     plt.subplot2grid((1, c0), (0, 0), colspan=c1, rowspan=1)

        # 饼图的数字重叠问题
        # explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        if textIn:
            l = plt.pie(dataList, labels=dataLabelList, autopct='%1.2f%%',
                    shadow=False, startangle=90, counterclock=False, pctdistance = 0.8, labeldistance = 5)
        else:
            l = plt.pie(dataList, labels=dataLabelList, autopct='%1.2f%%',
                        shadow=False, startangle=90, counterclock=False, pctdistance=1.2, labeldistance = 5)
        #
        legends.append(l)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.legend()
        return figureId


    # 绘制分组线图
    # dataList: 待绘制的数据集，为小数
    # dataLabelList: 与dataList相对应的标签，被用作图例
    # xAxisLabelList: x轴数据标签
    # xLable x轴标签
    # yLable y轴标签
    def lineChartPlot(self,dataList, dataLabelList, xAxisLabelList, xLable=None, yLable=None):
        legends = []
        figureId = self.gernerateFigure()
        if len(dataList) == 0:
            return None

        case_cnt = len(dataList)

        for i in range(0, case_cnt):
            xs = xAxisLabelList
            ys = dataList[i]
            l = plt.plot(xs, ys, label=dataLabelList[i])
            legends.append(l)
            for x, y in zip(xs, ys):
                plt.plot((x,), (y,), 'ko', markersize=3)  # TODO 修改点颜色与线条颜色统一
                plt.text(x, y, '%.2f' % (y))

        if case_cnt >= 2:
            plt.legend(legends, dataLabelList, bbox_to_anchor=(0.25, 1.02, 0.5, .102), loc=3,
                       ncol=len(dataLabelList), mode="expand", borderaxespad=0.)

        if yLable is not None:
            plt.ylabel(yLable)
        if xLable is not None:
            plt.xlabel(xLable)
        return figureId

    # 按元素求和
    def arraySum(self,l, s):
        # 保证l的长度大于等于s的长度
        # pdb.set_trace()
        if len(s) > len(l):
            temp = s
            s = l
            l = temp
        ret = []
        for x, y in zip(l[:len(s)], s):
            ret.append(x + y)
        for i in range(len(s), len(l)):
            ret.append(l[i])
        return ret


    # 根据所给长度随机生成数组
    # 用于测试
    def randomList(self,l):
        s = list(np.random.random(l))
        s = list(map(lambda x: int(x * 100), s))
        return s[:l]


if __name__ == '__main__':

    figureHelper = FigureHelper([8, 4.8])


    data = [figureHelper.randomList(8), figureHelper.randomList(8), figureHelper.randomList(8),
            figureHelper.randomList(8), figureHelper.randomList(8), figureHelper.randomList(8), figureHelper.randomList(8)]
    for d in data:
        print(d)

    labels = ['农民','工人','服务业','经商','家务','教师/公务员/职员','其它']
    xlables = ["噪音","猫狗","溶剂","高温","放射线","重金属","农药","震动","农药","震动"]
    # 累计条图
    # id1 = figureHelper.stackedHorizontalBarPlot(data, labels, xlables, 'test',gridcol=(24,19))
    # f = plt.figure(id1)
    # f.savefig('test3.png')
    #

    # 饼图
    pieChartData = [0.31, 16.3, 7.82, 0.02, 69.08, 3.47, 3.00]
    pieLabels = ['农民','工人','服务业','经商','家务','教师/公\n务员/职员','其它']
    # id4 = figureHelper.pieChartPlot(pieChartData, pieLabels,textIn=True)  # TODO: piechart 单独设计
    # f = plt.figure(id4)
    # f.savefig('test4.png')

    #pyecharts
    # large = 1.3
    # pie = Pie("", title_pos='center', width=800, height=480)
    # pie.add("", ['女方风险', '男方风险', '双方风险','一般人群'], [16.35,3.25,4.7,75.7],
    #         radius=[40*large, 55*large], is_label_show=True, legend_pos='left')
    # pie.add("", ['风险人群', '一般人群'], [24.3,75.7], radius=[0*large, 30*large], legend_orient='vertical',
    #         legend_pos='left', is_label_show=True,label_formatter='{d}%',label_pos='inside')
    # pie.show_config()
    # pie.render()
    # # print(os.getcwd()+'\\render.html')
    # make_a_snapshot('render.html', 'snapshot.png')


    # pieChartData = [0.31, 16.3, 7.82, 0.02, 69.08, 3.47, 3.00]
    # pieLabels = ['农民','工人','服务业','经商','家务','教师/公\n务员/职员','其它']
    # id4 = figureHelper.pieChartPlot(pieChartData, pieLabels,textIn=True)  # TODO: piechart 单独设计
    # f = plt.figure(id4)
    # f.savefig('test4.png')

    #百分累计条图
    # id2 = figureHelper.stackedBarPlotWithPercentage([[40, 30, 30], [50, 20, 30], [10, 50, 40]], ['1', '2', '3'],
    #                                    ['abc', 'def', '423'])
    # f = plt.figure(id2)
    # f.savefig('1.png')
    #带表格的累计条图

    # id3 = figureHelper.stackedBarPlotWithTable(data, labels, xlables)
    # f = plt.figure(id3)
    # f.savefig('2.png')


    #复式条图
    compBarData = [figureHelper.randomList(10),figureHelper.randomList(10)]
    compBarlabels = ['prapared','prapared']
    id5 = figureHelper.compoundBarPlot(compBarData, compBarlabels, xlables,
                        xLable="", yLable="百分比（%）",hline=True,
                        hasTable=True, figureText="",colorList=["r",'y','b'],indent=False )
    f = plt.figure(id5)
    f.savefig('test5.png')

    compBarData = [[0.31, 16.3, 7.82, 0.02, 69.08, 3.47, 3.00,0,2,4,5],[0.31, 16.3, 7.82, 0.02, 69.08, 3.47, 3.00,0,2,4,5]]
    compBarlabels = ['prapared', 'prapared']
    id5 = figureHelper.compoundBarPlot(compBarData, compBarlabels, xlables,
                                       xLable="", yLable="百分比（%）", hline=True,
                                       hasTable=True, figureText="", colorList=["r", 'y', 'b'], indent=False)
    f = plt.figure(id5)
    f.savefig('test5-1.png')

    #普通条图 带水平线
    # simpBarData = [figureHelper.randomList(10)]
    # simpBarlabels = ['meaning']
    # id6 = figureHelper.compoundBarPlot(simpBarData, simpBarlabels, xlables,
    #                     xLable="", yLable="百分比（%）",hline=True,
    #                     hasTable=False, figureText="全市平均水平",colorList=["b"])
    # f = plt.figure(id6)
    # f.savefig('6.png')

    # 复式水平条图1
    # horiBarData = [[0.11, 0.26, 0.13, 0.32, 0.44, 1.16], [0.11, 0.23, 0.13, 0.24, 0.31, 0.7]]
    # horiBarlabels = ['women', 'men']
    # horiLineXlabels = ['>=35', '30-34', '25-29', '20-24', '<20', '<15']
    # id9 = figureHelper.horizontalBarPlot(horiBarData, horiBarlabels, horiLineXlabels)
    # f = plt.figure(id9)
    # f.savefig('9.png')

    # 水平百分累积条图
    # stahoriBarData = [[40, 30, 30, 10, 20], [50, 20, 30, 60, 60], [10, 50, 40, 30, 20]]
    # stahoriBarlabels = ['lable1', 'lable2', 'lable3']
    # stahoriLineXlabels = ['area1', 'area2', 'area3', 'area4', 'area5']
    # id11 = figureHelper.stackedHorizontalBarPlotWithPercentage(stahoriBarData, stahoriBarlabels, stahoriLineXlabels)
    # f = plt.figure(id11)
    # f.savefig('11.png')


    # 复式线图
    # compLineData = [[37.27, 39.62, 60.17, 83.62, 90.65], [32.59, 17.25, 31.2, 79.3, 90.65]]
    # compLinelabels = ['country', 'city']
    # compLineXlabels = ['20-', '20-24', '25-29', '30-34', '35+']  # 一定要保证是按照字典序排列的，否则会先排序
    # id7 = figureHelper.lineChartPlot(compLineData, compLinelabels, compLineXlabels, 'age', 'percentage of second child')
    # f = plt.figure(id7)
    # f.savefig('7.png')

    # 简单线图
    # compLineData = [[26, 11, 7.4, 6.9, 6.6, 6.2, 5.25, 4.87, 4.13, 3.48, 3.09, 2.67, 11.33]]
    # compLinelabels = ['null']
    # compLineXlabels = [0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]  # 一定要保证是按照字典序排列的，否则会先排序
    # id8 = figureHelper.lineChartPlot(compLineData, compLinelabels, compLineXlabels, 'year of marriage', 'percentage')
    # f = plt.figure(id8)
    # f.savefig('8.png')


    # 金字塔条图
    # priBarData = [list(reversed([40, 30, 30, 20, 10, 15, 8, 5, 3, 3, 1])),
    #               list(reversed([50, 40, 40, 20, 20, 10, 7, 3, 2, 1, 0.8]))]
    # priBarlabels = ['lable1', 'lable2']
    # priXlabels = ['0 years', '1 years', '2 years', '3 years', '4 years'
    #     , '5 years', '6 years', '7 years', '8 years', '9 years', '>=10 years']
    # id12 = figureHelper.pyramidBarPlot(priBarData, priBarlabels, list(reversed(priXlabels)))
    # f = plt.figure(id12)
    # f.savefig('12.png')

    figureHelper.finish()