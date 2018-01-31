# -*- coding: utf-8 -*-

'''
    工具包：图表绘制函数
'''

from figureGenerate import figureGenerate
from DBinterface import DBInterface
import pandas as pd
from configuration import Config
from interpreter import Interpreter
def pic1(figGen):
    list_a = ["(complete=1)","(complete!=1)"]
    list_d = ["",""]
    labels = ["完成", "未完成"]
    figGen.drawDiseaseDistrict('1', list_a, list_d, labels, "exam", config.year,
                               isPercent=False, complete=False, picType="stbar",
                               yLable="档案数量", hline=False,
                               figureText="")

    list_a = ["(has_content=4)", "(has_content=3)", "(has_content=2)"]
    list_d = ["has_content is not null","has_content is not null","has_content is not null"]
    labels = ["双方签署", "男方签署", "女方签署"]
    figGen.drawDiseaseDistrict('2', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=False, picType="spbar",
                               hline=False,
                               hasTable=False, figureText="", colorList=[])

    list_a = ["(has_content=2 or has_content=4)", "(has_content between 3 and 4)"]
    list_d = ["", ""]
    labels = ['女性', '男性']
    figGen.drawDiseaseDistrict('3', list_a, list_d, labels, "exam", config.year,
                               isPercent=False, complete=False, picType="stbar",
                               yLable="检查人数", hline=False,
                               figureText="")

    # TODO 4为外部数据导入
    # list_a = ["(has_content=2 or has_content=4)", "(has_content between 3 and 4)"]
    # list_d = ["", ""]
    # labels = ['女性', '男性']
    # figGen.drawDiseaseDistrict(4, list_a, list_d, labels, "exam", config.year,
    #                            isPercent=False, complete=False, picType="sbar",
    #                            yLable="检查人数", hline=False,
    #                            hasTable=True, figureText="", colorList=["r", "b"])
    # TODO 5为饼柱结合图

    list_a = ["(dangr_obj=0)", "(dangr_obj = 1)","(dangr_obj = 2)","(dangr_obj=3)"]
    list_d = ["", "", "", ""]
    labels = ['无高危', '女方', '男方', '双方']
    figGen.drawDiseaseDistrict('6-1', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="百分比（%）", hline=False,
                               hasTable=False,figureText="", colorList=[])
    text_q = 'pass'
    figGen.drawDistrict('6-2', "dangr_obj between 1 and 3", "complete=1", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["b"])

    list_a = ["live_birth_num = 0", "live_birth_num = 1", "live_birth_num >= 2"]
    list_d = ["live_birth_num is not null", "live_birth_num is not null", "live_birth_num is not null"]
    labels = ["头胎", "二胎", "三胎及以上"]
    figGen.drawDiseaseYear('7-1', list_a, list_d, labels, "exam", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="构成比（%）",isSort=False)

    figGen.drawDiseaseDistrict('7-2', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=False, picType="spbar",
                               yLable="百分比（%）", hline=False,
                               hasTable=False, figureText="", colorList=[])

    #  early-follow-up time
    list_a = ["(bresult=1 or hcg =1)", "(earlylosefollowup=1)"]
    list_d = ["earlyyncomplete=1", "earlyyncomplete=1"]
    labels = ["已孕", "失访"]
    figGen.drawDiseaseDistrict('8', list_a, list_d, labels, "early", config.year,
                               isPercent=True, complete=True, picType="sbar",
                               yLable="档案数量", hline=False,
                               hasTable=False, figureText="", colorList=[])

    # follow-up time
    list_a = ["(follow_result=已分娩)", "(losefollowup=1)"]
    list_d = ["yncomplete=1", "yncomplete=1"]
    labels = ["已孕档案数", "失访档案数"]
    figGen.drawDiseaseDistrict('9', list_a, list_d, labels, "outcome", config.year,
                               isPercent=True, complete=True, picType="sbar",
                               yLable="档案数量", hline=False,
                               hasTable=False, figureText="", colorList=[])

    text_q = '全市平均水平'
    #  complete_date 表连接操作
    figGen.drawDistrict('10-1', "early.service_code = exam.service_code and early.mens_time - exam.service_time between -30 and 365", "early.service_code = exam.service_code", "exam, early", config.year,
                        isPercent=True, complete=False, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    #  follow-up time
    list_a = ["normalpre != 1", "normalpre = 1"]
    list_d = ["", ""]
    labels = ["不良妊娠结局","正常活产"]
    figGen.drawDisease('11-1', list_a, list_d, labels, "outcome", "all", config.year,
                       isPercent=True, complete=True, picType="pie",
                       yLable="百分比（%）")

    #  follow-up time 、yncomplete = 1 ！！ 同步修改getTopK..
    list_a = ['natrualpre=1', 'lower_weight=1', 'medicinepre=1', 'bornfault=1', 'earlypre=1', 'treatpre=1', 'differentpre=1',
                'deathpre=1', 'qitapre=1']
    list_d = ['', '', '', '', '', '', '', '', '']
    labels = ["自然\n流产", "低出生\n体重", "医学性\n人工流产", "出生\n缺陷", "早产","治疗性\n引产", "异位\n妊娠", "死胎\n死产", "其他"]
    figGen.drawDisease('11-2', list_a, list_d, labels, "outcome", "all", config.year,
                       isPercent=True, complete=True, picType="bar",
                       yLable="百分比（%）",figureText="pass")

def pic2(figGen):
    list_a = ['((DATEDIFF(service_time,mbirthday) div 365) <= 20)',
     '((DATEDIFF(service_time,mbirthday) div 365) between 21 and 25)',
     '((DATEDIFF(service_time,mbirthday) div 365) between 26 and 30)',
     '((DATEDIFF(service_time,mbirthday) div 365) between 31 and 35)',
     '((DATEDIFF(service_time,mbirthday) div 365) >= 36)']
    list_d = ['mbirthday is not null', 'mbirthday is not null',
              'mbirthday is not null', 'mbirthday is not null', 'mbirthday is not null']
    labels = ['<=20', '21-25', '26-30', '31-35', '>=36']
    figGen.drawDisease('12', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",isSort=False)
    figGen.drawDiseaseDistrict('13', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[])
    #TODO  饼图篡改标签、标签重合，百分堆积不是百分百、标签重合
    # list_a = ['((DATEDIFF(service_time,fbirthday) div 365) <= 20)',
    #          '((DATEDIFF(service_time,fbirthday) div 365) between 21 and 25)',
    #          '((DATEDIFF(service_time,fbirthday) div 365) between 26 and 30)',
    #          '((DATEDIFF(service_time,fbirthday) div 365) between 31 and 35)',
    #          '((DATEDIFF(service_time,fbirthday) div 365) >= 36)']
    # list_d = ['fbirthday is not null', 'fbirthday is not null',
    #           'fbirthday is not null', 'fbirthday is not null', 'fbirthday is not null']
    # labels = ['<=20', '21-25', '26-30', '31-35', '>=36']
    # figGen.drawDisease('14', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")
    # figGen.drawDiseaseDistrict('15', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ['((DATEDIFF(service_time,mbirthday) div 365) = (DATEDIFF(service_time,fbirthday) div 365))',
    #          '((DATEDIFF(service_time,mbirthday) div 365) < (DATEDIFF(service_time,fbirthday) div 365))',
    #          '((DATEDIFF(service_time,mbirthday) div 365) > (DATEDIFF(service_time,fbirthday) div 365))']
    # list_d = ['fbirthday is not null and mbirthday is not null', 'fbirthday is not null and mbirthday is not null',
    #          'fbirthday is not null and mbirthday is not null']
    # labels = ['同岁', '丈夫比妻子小', '丈夫比妻子大']
    # figGen.drawDisease('16', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")

    #
    # list_a = ["medu_level=1", "medu_level=2", "medu_level=3", "medu_level=4", "medu_level=5", "medu_level=6"]
    # list_d = ["medu_level is not null", "medu_level is not null", "medu_level is not null", "medu_level is not null",
    #         "medu_level is not null", "medu_level is not null"]
    # labels = ["文盲", "小学", "初中", "高中\n/中专\n/中技", "大专\n/大本", "研究生\n及以上"]
    # figGen.drawDisease('18', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")
    #
    # figGen.drawDiseaseDistrict('19', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    #
    # list_a = ["fedu_level=1", "fedu_level=2", "fedu_level=3", "fedu_level=4", "fedu_level=5", "fedu_level=6"]
    # list_d = ["fedu_level is not null", "fedu_level is not null", "fedu_level is not null", "fedu_level is not null",
    #           "fedu_level is not null", "fedu_level is not null"]
    # labels = ["文盲", "小学", "初中", "高中/中专/中技", "大专/大本", "研究生及以上"]
    # figGen.drawDisease('20', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")
    # figGen.drawDiseaseDistrict('21', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ["mjob=1", "mjob=2", "mjob=3", "mjob=4", "mjob=5", "mjob=6", "mjob=7"]
    # list_d = ["mjob is not null", "mjob is not null", "mjob is not null", "mjob is not null",
    #           "mjob is not null", "mjob is not null", "mjob is not null"]
    # labels = ['农民','工人','服务业','经商','家务','教师\n/公务员\n/职员','其它']
    # figGen.drawDisease('22', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")
    #
    # figGen.drawDiseaseDistrict('23', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="hspbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ["fjob=1", "fjob=2", "fjob=3", "fjob=4", "fjob=5", "fjob=6", "fjob=7"]
    # list_d = ["fjob is not null", "fjob is not null", "fjob is not null", "fjob is not null",
    #           "fjob is not null", "fjob is not null", "fjob is not null"]
    # labels = ['农民', '工人', '服务业', '经商', '家务', '教师/公务员/职员', '其它']
    # figGen.drawDisease('24', list_a, list_d, labels, "exam", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie")
    #
    # figGen.drawDiseaseDistrict('25', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="hspbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # text_q = ''
    # figGen.drawDistrict('26', "mnationality!='汉族'", "", "exam", config.year,
    #                     isPercent=True, complete=True, figureText=text_q,
    #                     yLable="百分比（%）", colorList=["b"])
    # figGen.drawDistrict('27', "fnationality!='汉族'", "", "exam", config.year,
    #                     isPercent=True, complete=True, figureText=text_q,
    #                     yLable="百分比（%）", colorList=["r"])
    #
    #
    # list_a1 = ['(has_content=2 or has_content=4) and faccount_location_city=address_city', '(has_content=2 or has_content=4) and faccount_location_city!=address_city']
    # list_d1 = ['(has_content=2 or has_content=4) and faccount_location_city is not null and address_city is not null', '(has_content=2 or has_content=4) and faccount_location_city is not null and address_city is not null']
    # list_a2 = ["has_content between 3 and 4 and maccount_location_city=address_city", "has_content between 3 and 4 and maccount_location_city!=address_city"]
    # list_d2 = ["has_content between 3 and 4 and maccount_location_city is not null and address_city is not null", "has_content between 3 and 4 and maccount_location_city is not null and address_city is not null"]
    # list_a = [list_a1, list_a2]
    # list_d = [list_d1, list_d2]
    # labels = ['女方', '男方']
    # xlabels = ['本地', '非本地']
    # figGen.drawDisease2('28', list_a, list_d, labels, xlabels, "exam", config.year,
    #                     isSort=False,
    #                     isPercent=True, complete=True, picType="bar",
    #                     yLable="百分比（%）")
    #
    # list_a = list_a2
    # list_d = list_d2
    # labels = xlabels
    # figGen.drawDiseaseDistrict('29', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = list_a1
    # list_d = list_d1
    # labels = xlabels
    # figGen.drawDiseaseDistrict('30', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])


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

    pic2(figGen)

    figGen.finish()
