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
# text1 = '全市平均水平'
# figGen.drawDistrict(92,"(smoking=1)","smoking is not null","exam",config.year,
#                        isPercent=True,  complete= True,figureText=text1)
# figGen.drawDistrict(93,"(smoking=1)","smoking is not null","exam",config.year,
#                        isPercent=True,  complete= True,figureText=text1)
# figGen.drawDistrict(99,"(drinking=1 or drinking=2)","drinking is not null","exam",config.year,
#                        isPercent=True,  complete= True,figureText=text1)
# figGen.drawDistrict(75,"(micro_sp=1)", "", "exam", config.year,
#                        isPercent=True, complete=True, figureText=text1)

list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
labels = ['偶尔', '经常']

# figGen.drawDisease(78,list_a, list_d, labels,"exam", "all",config.year,
#                        isPercent=True, complete=True)
# figGen.drawDisease(79,list_a, list_d, labels,"exam", "district",config.year,
#                        isPercent=True, complete=True)
# figGen.drawDiseaseYear(80,list_a, list_d, labels,"exam",config.year,2,
#                        isPercent=True, complete=True)

figGen.drawDiseaseDistrict(94,list_a, list_d, labels,"exam",config.year,
                       isPercent=True, complete=True)

figGen.drawYearDistrict(96,list_a[0], list_d[0],"exam",config.year,2,
                       isPercent=True, complete=True)

figGen.finish()
