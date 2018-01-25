# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

from figureGenerate import figureGenerate
from DBinterface import DBInterface
import pandas as pd
from configuration import Config
from interpreter import Interpreter

config = Config()
inter = Interpreter(config)
figGen = figureGenerate(config,inter)

list_a = ["use_medicine_A=1","use_medicine=1"]
list_d = ["use_medicine_A is not null","use_medicine is not null"]
labels = ["女","男"]
figGen.drawDisease(78,list_a, list_d, labels,"exam", "all",config.year,
                       isPercent=True, complete=True,picType="bar",
                       yLable="百分比（%）")

labels = ["女方","男方"]
figGen.drawDiseaseDistrict(79,list_a, list_d, labels,"exam",config.year,
                       isPercent=True, complete=True,picType="bar",
                       yLable="百分比（%）",hline=False,
                       hasTable=True, figureText="", colorList=[])

labels = ["女","男"]
figGen.drawDiseaseYear(80,list_a, list_d, labels,"exam",config.year,2,
                       isPercent=True, complete=True,
                       yLable="百分比（%）")


text_q = 'pass'
figGen.drawDistrict(92,"(smoking_A=1)","smoking_A is not null","exam",config.year,
                       isPercent=True,  complete= True,figureText=text_q,
                        yLable="百分比（%）",colorList=["r"])
figGen.drawDistrict(93,"(smoking=1)","smoking is not null","exam",config.year,
                       isPercent=True,  complete= True,figureText=text_q,
                        yLable="百分比（%）",colorList=["b"])

list_a = ["second_hand_smoking_A=1","second_hand_smoking_A=2"]
list_d = ["second_hand_smoking_A is not null","second_hand_smoking_A is not null"]
labels = ["经常","偶尔"]
figGen.drawDiseaseDistrict(94,list_a, list_d, labels,"exam",config.year,
                       isPercent=True, complete=True,picType="sbar",
                       yLable="百分比（%）",hline=False,
                       hasTable=True, figureText="", colorList=[])

list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
figGen.drawDiseaseDistrict(95,list_a, list_d, labels,"exam",config.year,
                       isPercent=True, complete=True,picType="sbar",
                       yLable="百分比（%）",hline=False,
                       hasTable=True, figureText="", colorList=[])

figGen.drawYearDistrict(96,"(smoking_A=1)","smoking_A is not null","exam",config.year,2,
                       isPercent=True, complete=True,yLable="百分比（%）")
figGen.drawYearDistrict(97,"(smoking=1)","smoking is not null","exam",config.year,2,
                       isPercent=True, complete=True,yLable="百分比（%）")




# figGen.drawDistrict(99,"(drinking=1 or drinking=2)","drinking is not null","exam",config.year,
#                        isPercent=True,  complete= True,figureText=text1)
# figGen.drawDistrict(75,"(micro_sp=1)", "", "exam", config.year,
#                        isPercent=True, complete=True, figureText=text1)


#
# list_a1 = [list_a,list_a]
# list_d1 = [list_d,list_d]
# labels = ['男', '女']
# xlabels = [ '经常','偶尔']
# figGen.drawDisease2(60,list_a1, list_d1, labels,xlabels,"exam",config.year,isSort=True,
#                        isPercent=True, complete=True,picType = "hsbar")
# figGen.drawDisease2(61,list_a1, list_d1, labels,xlabels,"exam",config.year,isSort=False,
#                        isPercent=True, complete=True,picType = "hbar")

figGen.finish()
