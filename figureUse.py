# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

from figureGenerate import figureGenerate
from DBinterface import DBInterface
import pandas as pd
from configuration import Config
from interpreter import Interpreter
def pic3_4(figGen):
    pass


def pic3_5(figGen):
    list_a = ["use_medicine=1","use_medicine=1"]
    list_d = ["use_medicine is not null","use_medicine is not null"]
    labels = ["女","男"]
    figGen.figureHelper.nfigsize = [6,4.8]
    figGen.drawDisease(78,list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    figGen.figureHelper.nfigsize = [8,4.8]
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
    figGen.drawDistrict(92,"(smoking=1)","smoking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["r"])
    figGen.drawDistrict(93,"(smoking=1)","smoking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["b"])

    list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
    list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
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

    figGen.drawYearDistrict(96,"(smoking=1)","smoking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict(97,"(smoking=1)","smoking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict(98,"(drinking=1 or drinking=2)","drinking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=[])
    figGen.drawDistrict(99,"(drinking=1 or drinking=3)","drinking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=[])

    figGen.drawYearDistrict(100,"(drinking=2)","drinking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict(101,"(drinking=3)","drinking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    text_q = 'pass'
    figGen.drawDistrict(102,"(pois_expoid is not null)","pois_expoid is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["b"])
    figGen.drawDistrict(103,"(pois_expoid is not null)","pois_expoid is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["r"])

    list_a = ["noise=1","catdog=1","new_decoration=1","high_temperature=1","radial=1","lead_hg=1","pesticide=1","shake=1"]
    list_d = ["noise is not null","catdog is not null","new_decoration is not null","high_temperature is not null",
              "radial is not null","lead_hg is not null","pesticide is not null","shake is not null"]
    labels = ["接触\n噪音","接触\n猫狗","接触有\n机溶剂","接触\n高温","接触\n放射线","接触\n重金属","接触\n农药","接触\n震动"]
    figGen.drawDisease(104,list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    list_a = ["noise=1","catdog=1","new_decoration=1","high_temperature=1","radial=1","lead_hg=1","pesticide=1","shake=1"]
    list_d = ["noise is not null","catdog is not null","new_decoration is not null","high_temperature is not null",
             "radial is not null","lead_hg is not null","pesticide is not null","shake is not null"]
    figGen.drawDisease(105,list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")

    list_a = ["(pressure=3 or pressure=4)","(pressure=3 or pressure=4)"]
    list_d = ["pressure is not null","pressure is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict(106,list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["(economic_pressure=3 or economic_pressure=4)","(economic_pressure=3 or economic_pressure=4)"]
    list_d = ["economic_pressure is not null","economic_pressure is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict(107,list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["(tense_relationship=3 or tense_relationship=4)","(tense_relationship=3 or tense_relationship=4)"]
    list_d = ["tense_relationship is not null","tense_relationship is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict(108,list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])


    figGen.drawYearDistrict(109,"(pressure=3 or pressure=4)","pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict(110,"(pressure=3 or pressure=4)","pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    figGen.drawYearDistrict(111,"(economic_pressure=3 or economic_pressure=4)","economic_pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict(112,"(economic_pressure=3 or economic_pressure=4)","economic_pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    figGen.drawYearDistrict(113,"(tense_relationship=3 or tense_relationship=4)","tense_relationship is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict(114,"(tense_relationship=3 or tense_relationship=4)","tense_relationship is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")


if __name__ == '__main__':
    config = Config()
    inter = Interpreter(config)
    figGen = figureGenerate(config,inter,[8,4.8])

    pic3_5(figGen)

    figGen.finish()
