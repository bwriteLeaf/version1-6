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
    # list_a = ["(complete=1)","(complete!=1)"]
    # list_d = ["",""]
    # labels = ["完成", "未完成"]
    # figGen.drawDiseaseDistrict('1', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=False, complete=False, picType="stbar",
    #                            yLable="档案数量", hline=False,
    #                            figureText="")
    #
    # list_a = ["(has_content=4)", "(has_content=3)", "(has_content=2)"]
    # list_d = ["has_content is not null","has_content is not null","has_content is not null"]
    # labels = ["双方签署", "男方签署", "女方签署"]
    # figGen.drawDiseaseDistrict('2', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=False, picType="spbar",
    #                            hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ["(has_content=2 or has_content=4)", "(has_content between 3 and 4)"]
    # list_d = ["", ""]
    # labels = ['女性', '男性']
    # figGen.drawDiseaseDistrict('3', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=False, complete=False, picType="stbar",
    #                            yLable="检查人数", hline=False,
    #                            figureText="")
    #
    # # TODO 4为外部数据导入
    # list_a = []
    # list_d = []
    # labels = ['计划怀孕夫妇数', '实际检查人数']
    # figGen.drawDiseaseDistrict('4', list_a, list_d, labels, "", config.year,
    #                            isPercent=False, complete=False, picType="bar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="pass", colorList=["r", "b"],
    #                            export=True)
    # TODO 5为饼柱结合图
    list_a1 = ["(dangr_obj between 1 and 3)", "(dangr_obj = 0)"]
    list_a2 = ["(dangr_obj=1)", "(dangr_obj = 2)", "(dangr_obj = 3)", "(dangr_obj=0)"]
    list_d1 = ["", ""]
    list_d2 = ["", "", "", ""]
    labels1 = ['风险人群', '一般人群']
    labels2 = ['女方风险', '男方风险', '双方风险','一般人群']
    list_a = [list_a1,list_a2]
    list_d = [list_d1, list_d2]
    labels = [labels1,labels2]
    figGen.drawTwoPie('5', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True)

    #
    # list_a = ["(dangr_obj=0)", "(dangr_obj = 1)","(dangr_obj = 2)","(dangr_obj=3)"]
    # list_d = ["", "", "", ""]
    # labels = ['无高危', '女方', '男方', '双方']
    # figGen.drawDiseaseDistrict('6-1', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False,figureText="", colorList=[])
    # text_q = '全市平均水平'
    # figGen.drawDistrict('6-2', "dangr_obj between 1 and 3", "complete=1", "exam", config.year,
    #                     isPercent=True, complete=True, figureText=text_q,
    #                     yLable="百分比（%）", colorList=["b"])
    #
    # list_a = ["live_birth_num = 0", "live_birth_num = 1", "live_birth_num >= 2"]
    # list_d = ["live_birth_num is not null", "live_birth_num is not null", "live_birth_num is not null"]
    # labels = ["头胎", "二胎", "三胎及以上"]
    # figGen.drawDiseaseYear('7-1', list_a, list_d, labels, "exam", config.year, 2,
    #                        isPercent=True, complete=True,
    #                        yLable="构成比（%）",isSort=False)
    #
    # figGen.drawDiseaseDistrict('7-2', list_a, list_d, labels, "exam", config.year,
    #                            isPercent=True, complete=False, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # #  early-follow-up time
    # list_a = ["(bresult=1 or hcg =1)", "(losefollowup=1)"]
    # list_d = ["yncomplete=1", "yncomplete=1"]
    # labels = ["已孕", "失访"]
    # figGen.drawDiseaseDistrict('8', list_a, list_d, labels, "early", config.year,
    #                            isPercent=True, complete=True, picType="sbar",
    #                            yLable="档案数量", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # # follow-up time
    # list_a = ["(follow_result='已分娩')", "(losefollowup=1)"]
    # list_d = ["yncomplete=1", "yncomplete=1"]
    # labels = ["已孕档案数", "失访档案数"]
    # figGen.drawDiseaseDistrict('9', list_a, list_d, labels, "outcome", config.year,
    #                            isPercent=True, complete=True, picType="sbar",
    #                            yLable="档案数量", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # text_q = '全市平均水平'
    # #  complete_date 表连接操作
    # figGen.drawDistrict('10-1', "early.service_code = exam.service_code and early.mens_time - exam.service_time between -30 and 365", "early.service_code = exam.service_code", "exam, early", config.year,
    #                     isPercent=True, complete=False, figureText=text_q,
    #                     yLable="百分比（%）", colorList=[])
    #
    # #  follow-up time
    # list_a = ["normalpre = 1", "normalpre != 1"]
    # list_d = ["", ""]
    # labels = ["正常活产","不良妊娠结局"]
    # figGen.drawDisease('11-1', list_a, list_d, labels, "outcome", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",
    #                    yLable="百分比（%）",textIn=True)
    #
    # #  follow-up time 、yncomplete = 1 ！！ 同步修改getTopK..
    # list_a = ['natrualpre=1', 'lower_weight=1', 'medicinepre=1', 'bornfault=1', 'earlypre=1', 'treatpre=1', 'differentpre=1',
    #             'deathpre=1', 'qitapre=1']
    # list_d = ['', '', '', '', '', '', '', '', '']
    # labels = ["自然\n流产", "低出生\n体重", "医学性\n人工流产", "出生\n缺陷", "早产","治疗性\n引产", "异位\n妊娠", "死胎\n死产", "其他"]
    # figGen.drawDisease('11-2', list_a, list_d, labels, "outcome", "all", config.year,
    #                    isPercent=True, complete=True, picType="bar",
    #                    yLable="百分比（%）",figureText="pass")

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
    list_a = ['((DATEDIFF(service_time,fbirthday) div 365) <= 20)',
             '((DATEDIFF(service_time,fbirthday) div 365) between 21 and 25)',
             '((DATEDIFF(service_time,fbirthday) div 365) between 26 and 30)',
             '((DATEDIFF(service_time,fbirthday) div 365) between 31 and 35)',
             '((DATEDIFF(service_time,fbirthday) div 365) >= 36)']
    list_d = ['fbirthday is not null', 'fbirthday is not null',
              'fbirthday is not null', 'fbirthday is not null', 'fbirthday is not null']
    labels = ['<=20', '21-25', '26-30', '31-35', '>=36']
    figGen.drawDisease('14', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",isSort=False)
    figGen.drawDiseaseDistrict('15', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[])

    list_a = ['((DATEDIFF(service_time,mbirthday) div 365) = (DATEDIFF(service_time,fbirthday) div 365))',
             '((DATEDIFF(service_time,mbirthday) div 365) < (DATEDIFF(service_time,fbirthday) div 365))',
             '((DATEDIFF(service_time,mbirthday) div 365) > (DATEDIFF(service_time,fbirthday) div 365))']
    list_d = ['fbirthday is not null and mbirthday is not null', 'fbirthday is not null and mbirthday is not null',
             'fbirthday is not null and mbirthday is not null']
    labels = ['同岁', '丈夫比妻子小', '丈夫比妻子大']
    figGen.drawDisease('16', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",isSort=False)


    list_a = ["medu_level=1", "medu_level=2", "medu_level=3", "medu_level=4", "medu_level=5", "medu_level=6"]
    list_d = ["medu_level is not null", "medu_level is not null", "medu_level is not null", "medu_level is not null",
            "medu_level is not null", "medu_level is not null"]
    labels = ["文盲", "小学", "初中", "高中/中专\n/中技", "大专/大本", "研究生及\n以上"]
    figGen.drawDisease('18', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)

    figGen.drawDiseaseDistrict('19', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))


    list_a = ["fedu_level=1", "fedu_level=2", "fedu_level=3", "fedu_level=4", "fedu_level=5", "fedu_level=6"]
    list_d = ["fedu_level is not null", "fedu_level is not null", "fedu_level is not null", "fedu_level is not null",
              "fedu_level is not null", "fedu_level is not null"]
    labels = ["文盲", "小学", "初中", "高中/中专\n/中技", "大专/大本", "研究生及\n以上"]
    figGen.drawDisease('20', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)
    figGen.drawDiseaseDistrict('21', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    list_a = ["mjob=1", "mjob=2", "mjob=3", "mjob=4", "mjob=5", "mjob=6", "mjob=7"]
    list_d = ["mjob is not null", "mjob is not null", "mjob is not null", "mjob is not null",
              "mjob is not null", "mjob is not null", "mjob is not null"]
    labels = ['农民','工人','服务业','经商','家务','教师/公务\n员/职员','其它']
    figGen.drawDisease('22', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)

    figGen.drawDiseaseDistrict('23', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="hspbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    list_a = ["fjob=1", "fjob=2", "fjob=3", "fjob=4", "fjob=5", "fjob=6", "fjob=7"]
    list_d = ["fjob is not null", "fjob is not null", "fjob is not null", "fjob is not null",
              "fjob is not null", "fjob is not null", "fjob is not null"]
    labels = ['农民', '工人', '服务业', '经商', '家务', '教师/公务\n员/职员', '其它']
    figGen.drawDisease('24', list_a, list_d, labels, "exam", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)

    figGen.drawDiseaseDistrict('25', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="hspbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    text_q = '全市平均水平'
    figGen.drawDistrict('26', "mnationality!='汉族'", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["b"])
    figGen.drawDistrict('27', "mnationality!='汉族'", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["r"])


    list_a1 = ['(has_content=2 or has_content=4) and faccount_location_city=address_city', '(has_content=2 or has_content=4) and faccount_location_city!=address_city']
    list_d1 = ['(has_content=2 or has_content=4) and faccount_location_city is not null and address_city is not null', '(has_content=2 or has_content=4) and faccount_location_city is not null and address_city is not null']
    list_a2 = ["has_content between 3 and 4 and maccount_location_city=address_city", "has_content between 3 and 4 and maccount_location_city!=address_city"]
    list_d2 = ["has_content between 3 and 4 and maccount_location_city is not null and address_city is not null", "has_content between 3 and 4 and maccount_location_city is not null and address_city is not null"]
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女方', '男方']
    xlabels = ['本地', '非本地']
    figGen.drawDisease2('28', list_a, list_d, labels, xlabels, "exam", config.year,
                        isSort=False,
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）")

    list_a = list_a2
    list_d = list_d2
    labels = xlabels
    figGen.drawDiseaseDistrict('29', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="百分比（%）", hline=False,
                               hasTable=False, figureText="", colorList=[])

    list_a = list_a1
    list_d = list_d1
    labels = xlabels
    figGen.drawDiseaseDistrict('30', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="百分比（%）", hline=False,
                               hasTable=False, figureText="", colorList=[])

def pic3_2(figGen):
    # TODO 38为饼柱结合图
    list_a1 = ["(pre_num>=1)", "(pre_num=0)"]
    list_a2 = ["(pre_num=1)", "(pre_num=2)", "(pre_num>=3)", "(pre_num=0)"]
    list_d1 = ["", ""]
    list_d2 = ["", "", "", ""]
    labels1 = ['怀孕1次及以上', '未曾怀孕']
    labels2 = ['怀孕1次', '怀孕2次', '怀孕3次及以上', '未曾怀孕']
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = [labels1, labels2]
    figGen.drawTwoPie('38', list_a, list_d, labels, "exam", config.year,
                      isPercent=True, complete=True)
#
#     text_q = '全市平均水平'
#     figGen.drawDistrict('39', "bad_pregnancy_result=1", "bad_pregnancy_result is not null", "exam", config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=["r"])
#     figGen.drawYearDistrict('40', "bad_pregnancy_result=1", "tsh is not null", "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#
#     text_q = '全市平均水平'
#     figGen.drawDistrict('41',
#                         # "(pubes=1 or breast=1 or vulva=1 or vagina=1 or secretions=1 or vervix=1 or uterus_bump=1 or uterus_size=1 or uterus_size=2 or uterus_act=1 or uterus_adnexa=1)",
#                         "(pubes!=0 or breast!=0 or vulva!=0 or vagina!=0 or secretions!=0 or vervix!=0 or uterus_bump!=0 or uterus_size!=0 or uterus_size!=0 or uterus_act!=0 or uterus_adnexa!=0)",
#                         "", "exam",
#                         config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#     figGen.drawDistrict('42',
#                         # "(orchis=1 or orchis=2 or orchis=3 or subclinical_varicocele=1 or prepuce=1 or prepuce=2 or pubes!=0 or buge_monggon!=0 or penis\
#                         #     !=0 or epididymis!=0 or seminal_duct!=0)",
#                         "(orchis!=0 or subclinical_varicocele!=0 or prepuce!=0 or prepuce=2 or pubes!=0 or buge_monggon!=0 or penis\
#                                                 #     !=0 or epididymis!=0 or seminal_duct!=0)",
#                         "", "exam", config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#
#     list_a = ["pubes!='0'", "breast!='0'", "vulva!='0'", "vagina!='0'", "secretions!='0'", "vervix!='0'",
#               "uterus_bump!='0'", "uterus_size!='0'", "uterus_act!='0'", "uterus_adnexa!='0'"]
#     # list_a = ["pubes=1", "breast=1", "vulva=1", "vagina=1", "secretions=1", "vervix=1",
#     #           "uterus_bump=1", "uterus_size=1 or uterus_size=2", "uterus_act=1", "uterus_adnexa=1"]
#     list_d = ["", "", "", "", "", "", "", "", "", ""]
#     labels = ["阴毛","乳房","外阴","阴道","分泌物","宫颈","子宫\n包块","子宫\n大小","子宫活\n动能力","子宫双\n侧附件"]
#     figGen.drawDisease('43', list_a, list_d, labels, "exam", "all", config.year,
#                        isPercent=True, complete=True, picType="bar",
#                        yLable="百分比（%）",figureText="pass")
#
#     # list_a = ["orchis=1 or orchis=2 or orchis=3","subclinical_varicocele=1","prepuce=1 or prepuce=2","pubes!=0","buge_monggon!=0","penis\
#     #             !=0","epididymis!=0","seminal_duct!=0"]
#     list_a = ["orchis!='0'","subclinical_varicocele!='0'","prepuce!='0'","pubes!=0","buge_monggon!=0","penis\
#                 !=0","epididymis!=0","seminal_duct!=0"]
#     list_d = ["", "", "", "", "", "", "", ""]
#     labels = ["睾丸","精索静\n脉曲张","包皮","阴毛","喉结","阴茎","附睾","输精管"]
#     figGen.drawDisease('44', list_a, list_d, labels, "exam", "all", config.year,
#                        isPercent=True, complete=True, picType="bar",
#                        yLable="百分比（%）",figureText="pass")
#
#     text_q = '全市平均水平'
#     figGen.drawDistrict('45',
#                         "(intrauterine_device=1 or subcutaneous_implants=1 or topical_contraceptives=1 or topical_contraceptives=1)",
#                         "", "exam",
#                         config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#
# def pic3_3(figGen):
#     text_q = '全市平均水平'
#     figGen.drawDistrict('46', "(hypertension=1 or heart_disease=1 or diabetes=1 or epilepsy=1 or thyroid_disease=1 or chronic_nephritis=1 or swelling=1)", "is_ill is not null", "exam",
#                         config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#     figGen.drawDistrict('47', "(hypertension=1 or heart_disease=1 or diabetes=1 or epilepsy=1 or thyroid_disease=1 or chronic_nephritis=1 or swelling=1)", "is_ill is not null", "exam", config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#
#     list_a = ['hypertension=1', 'heart_disease=1', 'diabetes=1', 'epilepsy=1', 'thyroid_disease=1', 'chronic_nephritis=1', 'swelling=1']
#     list_d = ['is_ill is not null','is_ill is not null','is_ill is not null','is_ill is not null','is_ill is not null','is_ill is not null','is_ill is not null']
#     labels = ["高血压", "心脏病", "糖尿病", "癫痫", "甲状腺疾病", "慢性肾炎", "肿瘤"]
#     figGen.drawDisease('48',list_a, list_d, labels,"exam", "all",config.year,
#                            isPercent=True, complete=True,picType="hbar",
#                            xLable="百分比（%）",upSort=False,colorList=['r'])
#
#     list_a = ['hypertension=1', 'heart_disease=1', 'diabetes=1', 'epilepsy=1', 'thyroid_disease=1',
#               'chronic_nephritis=1', 'swelling=1']
#     list_d = ['is_ill is not null', 'is_ill is not null', 'is_ill is not null', 'is_ill is not null',
#               'is_ill is not null', 'is_ill is not null', 'is_ill is not null']
#     figGen.drawDisease('49', list_a, list_d, labels, "exam", "all", config.year,
#                        isPercent=True, complete=True, picType="hbar",
#                        xLable="百分比（%）",upSort=False,colorList=['b'])
#     #TODO 目前是手动找出前3然后调用
#     list_a = ['hypertension=1', 'thyroid_disease=1','swelling=1']
#     list_d = ['is_ill is not null','is_ill is not null', 'is_ill is not null']
#     labels = ["高血压","甲状腺疾病", "肿瘤"]
#     figGen.drawDiseaseYear('50', list_a, list_d, labels, "exam", config.year, 2,
#                            isPercent=True, complete=True,
#                            yLable="百分比（%）")
#
#     list_a = ['hypertension=1', 'thyroid_disease=1', 'diabetes=1']
#     list_d = ['is_ill is not null', 'is_ill is not null', 'is_ill is not null']
#     labels = ["高血压", "甲状腺疾病", "糖尿病"]
#     figGen.drawDiseaseYear('51', list_a, list_d, labels, "exam", config.year, 2,
#                            isPercent=True, complete=True,
#                            yLable="百分比（%）")
#
#     list_a = ["(hight_blood_pressure >= 140 or low_blood_pressure >= 90)", "(hight_blood_pressure >= 140 or low_blood_pressure >= 90)"]
#     list_d = ["hight_blood_pressure is not null or low_blood_pressure is not null", "hight_blood_pressure is not null or low_blood_pressure is not null"]
#     labels = ["女方", "男方"]
#     figGen.drawDiseaseDistrict('52', list_a, list_d, labels, "exam", config.year,
#                                isPercent=True, complete=True, picType="bar",
#                                yLable="百分比（%）", hline=False,
#                                hasTable=True, figureText="", colorList=[])
#     figGen.drawYearDistrict('53', list_a[0], list_d[0], "exam",config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#     figGen.drawYearDistrict('54', list_a[1], list_d[1], "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#
#     text_q = '全市平均水平'
#     figGen.drawDistrict('55-1',"(blood_sugar >= 6.10)","blood_sugar is not null", "exam",
#                         config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#     figGen.drawDistrict('55-2',
#                         "(blood_sugar>=7.0 or diabetes1=1)",
#                         "(blood_sugar is not null or diabetes1 is not null)", "exam", config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#
#     figGen.drawYearDistrict('56-1', "(blood_sugar >= 6.10)","blood_sugar is not null", "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#     figGen.drawYearDistrict('56-2', "(blood_sugar>=7.0 or diabetes1=1)",
#                         "(blood_sugar is not null or diabetes1 is not null)", "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#
#     text_q = '全市平均水平'
#     figGen.drawDistrict('57', "(tsh<0.44 or tsh>3.45)", "tsh is not null", "exam",
#                         config.year,
#                         isPercent=True, complete=True, figureText=text_q,
#                         yLable="百分比（%）", colorList=[])
#     figGen.drawYearDistrict('58', "(tsh<0.44 or tsh>3.45)", "tsh is not null", "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#
#     list_a = ["alt>45", "alt>45"]
#     list_d = ["alt is not null", "alt is not null"]
#     labels = ['女性', '男性']
#     figGen.drawDiseaseDistrict('59', list_a, list_d, labels, "exam", config.year,
#                                isPercent=True, complete=True, picType="bar",
#                                yLable="百分比（%）", hline=False,
#                                hasTable=True, figureText="", colorList=['r', 'b'])
#     figGen.drawYearDistrict('60', list_a[0], list_d[0], "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#     figGen.drawYearDistrict('61', list_a[1], list_d[1], "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#
#     list_a = ["(cr>73 or cr<41)", "(cr > 97 or cr<57)"]
#     list_d = ["cr is not null", "cr is not null"]
#     labels = ['女性', '男性']
#     figGen.drawDiseaseDistrict('62', list_a, list_d, labels, "exam", config.year,
#                                isPercent=True, complete=True, picType="bar",
#                                yLable="百分比（%）", hline=False,
#                                hasTable=True, figureText="", colorList=['r', 'b'])
#     figGen.drawYearDistrict('63', list_a[0], list_d[0], "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")
#     figGen.drawYearDistrict('64', list_a[1], list_d[1], "exam", config.year, 2,
#                             isPercent=True, complete=True, yLable="百分比（%）")

def pic3_4(figGen):
    text_q = '全市平均水平'
    figGen.drawDistrict('65', "(nodule=1 or hb=1 or sexually_infect=1)", "is_ill is not null", "exam",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('66', "(nodule=1 or hb=1 or sexually_infect=1)", "is_ill is not null", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawYearDistrict('67', "(nodule=1 or hb=1 or sexually_infect=1)", "is_ill is not null", "exam",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('68', "(nodule=1 or hb=1 or sexually_infect=1)", "is_ill is not null", "exam",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a1 = ['nodule=1', 'hb=1', 'sexually_infect=1']
    list_a2 = ['nodule=1', 'hb=1', 'sexually_infect=1']
    list_d1 = ["is_ill is not null", "is_ill is not null", "is_ill is not null"]
    list_d2 = ["is_ill is not null", "is_ill is not null", "is_ill is not null"]
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女性', '男性']
    xlabels = ['结核', '乙肝', "性病"]
    figGen.drawDisease2('69', list_a, list_d, labels, xlabels, "exam", config.year, isSort=True,
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）",figureText="pass")

    figGen.drawDistrict('70', "(cv_igm=1)", "", "exam",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('71', "(tg_igm=1)", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('72', "(rv_igg=1)", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    list_a = ["hbs_ag=1", "hbs_ag=1"]
    list_d = ["", ""]
    labels = ['女性', '男性']
    figGen.drawDiseaseDistrict('73', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=True,
                               hasTable=False, figureText="case", colorList=['r', 'b'])

    text_q = '全市平均水平'
    figGen.drawDistrict('74', "(tpha=1)", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=['b'])
    figGen.drawDistrict('75', "(micro_sp=1)", "", "exam", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=['r'])

    figGen.drawYearDistrict('76', "(micro_sp=1)", "", "exam",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('77', "(tpha=1)", "", "exam", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")



def pic3_5(figGen):
    list_a = ["use_medicine=1","use_medicine=1"]
    list_d = ["use_medicine is not null","use_medicine is not null"]
    labels = ["女","男"]
    figGen.figureHelper.nfigsize = [6,4.8]
    figGen.drawDisease('78',list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    figGen.figureHelper.nfigsize = [8,4.8]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict('79',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    labels = ["女","男"]
    figGen.drawDiseaseYear('80',list_a, list_d, labels,"exam",config.year,2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")


    text_q = '全市平均水平'
    figGen.drawDistrict('92',"(smoking=1)","smoking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["r"])
    figGen.drawDistrict('93',"(smoking=1)","smoking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["b"])

    list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
    list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
    labels = ["经常","偶尔"]
    figGen.drawDiseaseDistrict('94',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="sbar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
    list_d = ["second_hand_smoking is not null","second_hand_smoking is not null"]
    figGen.drawDiseaseDistrict('95',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="sbar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    figGen.drawYearDistrict('96',"(smoking=1)","smoking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict('97',"(smoking=1)","smoking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict('98',"(drinking=1 or drinking=2)","drinking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=[])
    figGen.drawDistrict('99',"(drinking=1 or drinking=3)","drinking is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=[])

    figGen.drawYearDistrict('100',"(drinking=2)","drinking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict('101',"(drinking=2)","drinking is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict('102',"(pois_expoid is not null)","pois_expoid is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["b"])
    figGen.drawDistrict('103',"(pois_expoid is not null)","pois_expoid is not null","exam",config.year,
                           isPercent=True,  complete= True,figureText=text_q,
                            yLable="百分比（%）",colorList=["r"])

    list_a = ["noise=1","catdog=1","new_decoration=1","high_temperature=1","radial=1","lead_hg=1","pesticide=1","shake=1"]
    list_d = ["noise is not null","catdog is not null","new_decoration is not null","high_temperature is not null",
              "radial is not null","lead_hg is not null","pesticide is not null","shake is not null"]
    labels = ["接触\n噪音","接触\n猫狗","接触有\n机溶剂","接触\n高温","接触\n放射线","接触\n重金属","接触\n农药","接触\n震动"]
    figGen.drawDisease('104',list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    list_a = ["noise=1","catdog=1","new_decoration=1","high_temperature=1","radial=1","lead_hg=1","pesticide=1","shake=1"]
    list_d = ["noise is not null","catdog is not null","new_decoration is not null","high_temperature is not null",
             "radial is not null","lead_hg is not null","pesticide is not null","shake is not null"]
    figGen.drawDisease('105',list_a, list_d, labels,"exam", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")

    list_a = ["(pressure=3 or pressure=4)","(pressure=3 or pressure=4)"]
    list_d = ["pressure is not null","pressure is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict('106',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["(economic_pressure=3 or economic_pressure=4)","(economic_pressure=3 or economic_pressure=4)"]
    list_d = ["economic_pressure is not null","economic_pressure is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict('107',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["(tense_relationship=3 or tense_relationship=4)","(tense_relationship=3 or tense_relationship=4)"]
    list_d = ["tense_relationship is not null","tense_relationship is not null"]
    labels = ["女方","男方"]
    figGen.drawDiseaseDistrict('108',list_a, list_d, labels,"exam",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])


    figGen.drawYearDistrict('109',"(pressure=3 or pressure=4)","pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict('110',"(pressure=3 or pressure=4)","pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    figGen.drawYearDistrict('111',"(economic_pressure=3 or economic_pressure=4)","economic_pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict('112',"(economic_pressure=3 or economic_pressure=4)","economic_pressure is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

    figGen.drawYearDistrict('113',"(tense_relationship=3 or tense_relationship=4)","tense_relationship is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")
    figGen.drawYearDistrict('114',"(tense_relationship=3 or tense_relationship=4)","tense_relationship is not null","exam",config.year,2,
                           isPercent=True, complete=True,yLable="百分比（%）")

def pic3_1(figGen):
    text_q = '全市平均水平'
    a1 = "(is_born_ill=1 or thalassaemia =1 or down_syndrome=1 or albinism=1 or diabetes1=1 or blood_sick=1 or  dysgnosia=1 or favism=1 or congenital_heart_disease=1 or hearing_disorder=1 or seeing_disorder=1 or infant_mortality=1 or sterility=1 or intermarry=1)"
    d1 = "(is_born_ill is not null or thalassaemia is not null or down_syndrome is not null or albinism is not null or diabetes1 is not null or blood_sick is not null or  dysgnosia is not null or favism is not null or congenital_heart_disease is not null or hearing_disorder is not null or seeing_disorder is not null or infant_mortality is not null or sterility is not null or intermarry is not null)"
    a2 = "(is_born_ill=1 or thalassaemia =1 or down_syndrome=1 or albinism=1 or diabetes1=1 or blood_sick=1 or  dysgnosia=1 or favism=1 or congenital_heart_disease=1 or hearing_disorder=1 or seeing_disorder=1 or infant_mortality=1 or sterility=1 or intermarry=1)"
    d2 = "(is_born_ill is not null or thalassaemia is not null or down_syndrome is not null or albinism is not null or diabetes1 is not null or blood_sick is not null or  dysgnosia is not null or favism is not null or congenital_heart_disease is not null or hearing_disorder is not null or seeing_disorder is not null or infant_mortality is not null or sterility is not null or intermarry is not null)"
    figGen.drawDistrict('31',a1,d1, "exam",config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('32',a2,d2, "exam",config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    figGen.drawYearDistrict('33', a1, d1, "exam", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('34', a2, d2, "exam", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a1 = ['blood_sick =1', 'favism =1', 'congenital_heart_disease=1',
               'infant_mortality=1','(hearing_disorder=1 or seeing_disorder=1)','dysgnosia=1']
    list_a2 = ['blood_sick =1', 'favism =1', 'congenital_heart_disease=1',
               'infant_mortality=1','(hearing_disorder=1 or seeing_disorder=1)','dysgnosia=1']
    list_d1 = ['blood_sick  is not null', 'favism  is not null', 'congenital_heart_disease is not null',
               'infant_mortality is not null','(hearing_disorder is not null or seeing_disorder is not null)','dysgnosia is not null']
    list_d2 = ['blood_sick  is not null', 'favism  is not null', 'congenital_heart_disease is not null',
               'infant_mortality is not null','(hearing_disorder is not null or seeing_disorder is not null)','dysgnosia is not null']
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女方', '男方']
    xlabels = ['地中海贫血', 'G6PD缺乏症', "先天性心脏病", '新生儿或婴\n幼儿死亡史', "内生障碍", '先天性智\n力低下']
    figGen.drawDisease2('35', list_a, list_d, labels, xlabels, "exam", config.year, isSort=True,
                        isPercent=True, complete=True, picType="hbar",
                        xLable="百分比（%）")

    a1 = '(SEA_f like "杂合性突变" or (Alpha37_f like "杂合性突变" or Alpha37_f like "纯合型突变") or (Alpha42_f like "杂合性突变" or Alpha42_f like "纯合型突变") or aCS_f like "杂合性突变" or aWS_f like "杂合性突变" or aOhter_f like "%突变%")'
    a2 = '(SEA_m like "杂合性突变" or (Alpha37_m like "杂合性突变" or Alpha37_m like "纯合型突变") or (Alpha42_m like "杂合性突变" or Alpha42_m like "纯合型突变") or aCS_m like "杂合性突变" or aWS_m like "杂合性突变" or aOhter_m like "%突变%")'
    b1 = '(CD14_15_f like "杂合性突变" or CD17_f like "杂合性突变" or CD27_28_f like "杂合性突变" or CD_28_f like "杂合性突变" or CD_29_f like "杂合性突变" or CD_31_f like "杂合性突变" or CD_41_42_f like "杂合性突变" or CD_71_72_f like "杂合性突变" or CAP_f like "杂合性突变" or IntM_f like "杂合性突变" or IVS_5_f like "杂合性突变" or IVS_654_f like "杂合性突变" or Beta_E_f like "杂合性突变" or Beta_Other_f like "%突变%")'
    b2 = '(CD14_15_m like "杂合性突变" or CD17_m like "杂合性突变" or CD27_28_m like "杂合性突变" or CD_28_m like "杂合性突变" or CD_29_m like "杂合性突变" or CD_31_m like "杂合性突变" or CD_41_42_m like "杂合性突变" or CD_71_72_m like "杂合性突变" or CAP_m like "杂合性突变" or IntM_m like "杂合性突变" or IVS_5_m like "杂合性突变" or IVS_654_m like "杂合性突变" or Beta_E_m like "杂合性突变" or Beta_Other_m like "%突变%")'
    # list_a1 = ['MCV_f<82', 'MCH_f<27',a1, b1]
    # list_a2 = ['MCV_m<82', 'MCH_m<27',a2, b2]
    list_a1 = ['','','','']
    list_a2 = ['', '', '', '']
    list_d1 = ['','','','']
    list_d2 = ['','','','']
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女方', '男方']
    xlabels = ['MCV', 'MCH', "α地贫", 'β地贫']
    figGen.drawDisease2('36', list_a, list_d, labels, xlabels, "exam", config.year, isSort=False,
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）",figureText='pass',colorList=['r','b'])

    figGen.figureHelper.nfigsize = [8, 5.8]
    # list_a = [a1,b1,a2,b2]
    list_a = ['', '', '', '']
    list_d = ['','','','']
    labels = ["女性α地贫", '女性β地贫', "男性α地贫", '男性β地贫']
    figGen.drawDiseaseDistrict('37', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))
    figGen.figureHelper.nfigsize = [8, 4.8]

def pic3_6(figGen):

    list_a = ['(meategg=0)', '(hate_veg=1)', '(raw_meat=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseDistrict('81', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))

    list_a = ['(meategg=0)', '(hate_veg=1)', '(raw_meat=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseDistrict('82', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))
    
    list_a = ['(meategg=0)', '(hate_veg=1)', '(raw_meat=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseYear('83', list_a, list_d, labels, "exam", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ['(meategg=0)', '(hate_veg=1)', '(raw_meat=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseYear('84', list_a, list_d, labels, "exam", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ['(bmi < 18.5)', '(bmi >= 24 and bmi < 28)', '(bmi >= 28)']
    list_d = ['', '', '', '']
    labels = ["低体重", '超重', "肥胖"]
    figGen.drawDiseaseYear('85', list_a, list_d, labels, "exam", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）",isSort = False)

    list_a = ['(bmi < 18.5)', '(bmi >= 24 and bmi < 28)', '(bmi >= 28)']
    list_d = ['', '', '', '']
    labels = ["低体重", '超重', "肥胖"]
    figGen.drawDiseaseYear('86', list_a, list_d, labels, "exam", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）",isSort = False)

    figGen.figureHelper.nfigsize = [8, 5.8]
    list_a = ["(bmi >= 28)", "(bmi >= 24 and bmi < 28)", "(bmi >= 18.5 and bmi < 24)", "(bmi < 18.5)"]
    list_d = ["bmi is not null", "bmi is not null", "bmi is not null", "bmi is not null"]
    labels = ["肥胖","偏重","正常","偏瘦"]
    figGen.drawDiseaseDistrict('87', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])

    list_a = ["(bmi >= 28)", "(bmi >= 24 and bmi < 28)", "(bmi >= 18.5 and bmi < 24)", "(bmi < 18.5)"]
    list_d = ["bmi is not null", "bmi is not null", "bmi is not null", "bmi is not null"]
    labels = ["肥胖","偏重","正常","偏瘦"]
    figGen.drawDiseaseDistrict('88', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])
    figGen.figureHelper.nfigsize = [8, 4.8]

    list_a = ["(anemia=1)", "(bhb<110)"]
    list_d = ["(is_ill_A is not null and (bhb<110))",'bhb is not null']
    labels = ["自报患病率", "检出率"]
    figGen.drawDiseaseDistrict('89', list_a, list_d, labels, "exam", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])

    figGen.drawYearDistrict('90', list_a[0], list_d[0], "exam", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('91', list_a[1], list_d[1], "exam", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")



if __name__ == '__main__':
    config = Config()
    inter = Interpreter(config)
    figGen = figureGenerate(config,inter,[8,4.8])

    # pic3_5(figGen)
    pic3_2(figGen)

    # pic1(figGen)
    # pic2(figGen)


    figGen.finish()
