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
    # list_a = ["(iscomplete_ea=2)","(iscomplete_ea!=2)"]
    # list_d = ["",""]
    # labels = ["完成", "未完成"]
    # figGen.drawDiseaseDistrict('1', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=False, complete=False, picType="stbar",
    #                            yLable="档案数量", hline=False,
    #                            figureText="")
    #
    # list_a = ["(informed_consent_signed=0)", "(informed_consent_signed=2)", "(informed_consent_signed=1)"]
    # list_d = ["informed_consent_signed is not null","informed_consent_signed is not null","informed_consent_signed is not null"]
    # labels = ["双方签署", "男方签署", "女方签署"]
    # figGen.drawDiseaseDistrict('2', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=False, picType="spbar",
    #                            hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ["(informed_consent_signed=0 or informed_consent_signed=2)", "(informed_consent_signed between 0 and 1)"]
    # list_d = ["", ""]
    # labels = ['女性', '男性']
    # figGen.drawDiseaseDistrict('3', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
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
    # # 5为饼柱结合图
    # list_a1 = ["(risk_population between 0 and 2)", "(risk_population is null)"]
    # list_a2 = ["(risk_population=2)", "(risk_population=1)", "(risk_population=0)", "(risk_population is null)"]
    # list_d1 = ["", ""]
    # list_d2 = ["", "", "", ""]
    # labels1 = ['风险人群', '一般人群']
    # labels2 = ['女方风险', '男方风险', '双方风险','一般人群']
    # list_a = [list_a1,list_a2]
    # list_d = [list_d1, list_d2]
    # labels = [labels1,labels2]
    # figGen.drawTwoPie('5', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True)


    list_a = ["(risk_population is null)", "(risk_population=2)","(risk_population=1)","(risk_population=0)"]
    list_d = ["", "", "", ""]
    labels = ['无高危', '女方', '男方', '双方']
    figGen.drawDiseaseDistrict('6-1', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="百分比（%）", hline=False,
                               hasTable=False,figureText="", colorList=[])
    text_q = '全市平均水平'
    figGen.drawDistrict('6-2', "risk_population between 0 and 2", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["b"])
    #
    # list_a = ["live_birth_number_w = 0", "live_birth_number_w = 1", "live_birth_number_w >= 2"]
    # list_d = ["live_birth_number_w is not null", "live_birth_number_w is not null", "live_birth_number_w is not null"]
    # labels = ["头胎", "二胎", "三胎及以上"]
    # figGen.drawDiseaseYear('7-1', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
    #                        isPercent=True, complete=True,
    #                        yLable="构成比（%）",isSort=False)
    #
    # figGen.drawDiseaseDistrict('7-2', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=False, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])

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
    # figGen.drawDistrict('10-1', "early.service_code = guangdong_yunqianjianchabiao_2017.service_code and early.mens_time - guangdong_yunqianjianchabiao_2017.input_date_archive_ymd between -30 and 365", "early.service_code = guangdong_yunqianjianchabiao_2017.service_code", "guangdong_yunqianjianchabiao_2017, early", config.year,
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
    # list_a = ['((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) <= 20)',
    #  '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) between 21 and 25)',
    #  '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) between 26 and 30)',
    #  '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) between 31 and 35)',
    #  '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) >= 36)']
    # list_d = ['birthday_h is not null', 'birthday_h is not null',
    #           'birthday_h is not null', 'birthday_h is not null', 'birthday_h is not null']
    # labels = ['<=20', '21-25', '26-30', '31-35', '>=36']
    # figGen.drawDisease('12', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",isSort=False)
    # figGen.drawDiseaseDistrict('13', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    # #TODO  饼图篡改标签、标签重合，百分堆积不是百分百、标签重合
    # list_a = ['((DATEDIFF(input_date_archive_ymd,birthday_w) div 365) <= 20)',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_w) div 365) between 21 and 25)',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_w) div 365) between 26 and 30)',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_w) div 365) between 31 and 35)',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_w) div 365) >= 36)']
    # list_d = ['birthday_w is not null', 'birthday_w is not null',
    #           'birthday_w is not null', 'birthday_w is not null', 'birthday_w is not null']
    # labels = ['<=20', '21-25', '26-30', '31-35', '>=36']
    # figGen.drawDisease('14', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",isSort=False)
    # figGen.drawDiseaseDistrict('15', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = ['((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) = (DATEDIFF(input_date_archive_ymd,birthday_w) div 365))',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) < (DATEDIFF(input_date_archive_ymd,birthday_w) div 365))',
    #          '((DATEDIFF(input_date_archive_ymd,birthday_h) div 365) > (DATEDIFF(input_date_archive_ymd,birthday_w) div 365))']
    # list_d = ['birthday_w is not null and birthday_h is not null', 'birthday_w is not null and birthday_h is not null',
    #          'birthday_w is not null and birthday_h is not null']
    # labels = ['同岁', '丈夫比妻子小', '丈夫比妻子大']
    # figGen.drawDisease('16', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",isSort=False)


    list_a = ["(education_h=1 or education_h='文盲')", "(education_h=2 or education_h='小学')",
              "(education_h=3 or education_h='初中')", "(education_h=4 or education_h='高中/中专/中技')",
              "((education_h between 5 and 6) or education_h='大专/大本')", "((education_h between 7 and 8) or education_h='研究生及以上')"]
    list_d = ["education_h is not null", "education_h is not null", "education_h is not null", "education_h is not null",
            "education_h is not null", "education_h is not null"]
    labels = ["文盲", "小学", "初中", "高中/中专\n/中技", "大专/大本", "研究生\n及以上"]
    figGen.drawDisease('18', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)

    figGen.drawDiseaseDistrict('19', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    list_a = ["(education_w=1 or education_w='文盲')", "(education_w=2 or education_w='小学')",
              "(education_w=3 or education_w='初中')", "(education_w=4 or education_w='高中/中专/中技')",
              "((education_w between 5 and 6) or education_w='大专/大本')",
              "((education_w between 7 and 8) or education_w='研究生及以上')"]

    list_d = ["education_w is not null", "education_w is not null", "education_w is not null", "education_w is not null",
              "education_w is not null", "education_w is not null"]
    labels = ["文盲", "小学", "初中", "高中/中专\n/中技", "大专/大本", "研究生\n及以上"]
    figGen.drawDisease('20', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
                       isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)
    figGen.drawDiseaseDistrict('21', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="", hline=False,
                               hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    # list_a = ["occupation_h=1", "occupation_h=2", "occupation_h=3", "occupation_h=4", "occupation_h=5", "occupation_h=6", "occupation_h=7"]
    # list_d = ["occupation_h is not null", "occupation_h is not null", "occupation_h is not null", "occupation_h is not null",
    #           "occupation_h is not null", "occupation_h is not null", "occupation_h is not null"]
    # labels = ['农民','工人','服务业','经商','家务','教师/公务\n员/职员','其它']
    # figGen.drawDisease('22', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)
    #
    # figGen.drawDiseaseDistrict('23', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="hspbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[],gridcol=(24,21))
    #
    # list_a = ["occupation_w=1", "occupation_w=2", "occupation_w=3", "occupation_w=4", "occupation_w=5", "occupation_w=6", "occupation_w=7"]
    # list_d = ["occupation_w is not null", "occupation_w is not null", "occupation_w is not null", "occupation_w is not null",
    #           "occupation_w is not null", "occupation_w is not null", "occupation_w is not null"]
    # labels = ['农民', '工人', '服务业', '经商', '家务', '教师/公务\n员/职员', '其它']
    # figGen.drawDisease('24', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
    #                    isPercent=True, complete=True, picType="pie",textIn=True,isSort=False)
    #
    # figGen.drawDiseaseDistrict('25', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="hspbar",
    #                            yLable="", hline=False,
    #                            hasTable=False, figureText="", colorList=[],gridcol=(24,21))

    text_q = '全市平均水平'
    figGen.drawDistrict('26', "nation_h!=1", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["b"])
    figGen.drawDistrict('27', "nation_w!=1", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["r"])


    list_a1 = ['(informed_consent_signed=0 or informed_consent_signed=2) and account_city_w=address_city_w', '(informed_consent_signed=0 or informed_consent_signed=2) and account_city_w!=address_city_w']
    list_d1 = ['(informed_consent_signed=0 or informed_consent_signed=2) and account_city_w is not null and address_city_w is not null', '(informed_consent_signed=0 or informed_consent_signed=2) and account_city_w is not null and address_city_w is not null']
    list_a2 = ["informed_consent_signed between 0 and 1 and account_city_h=address_city_w", "informed_consent_signed between 0 and 1 and account_city_h!=address_city_w"]
    list_d2 = ["informed_consent_signed between 0 and 1 and account_city_h is not null and address_city_w is not null", "informed_consent_signed between 0 and 1 and account_city_h is not null and address_city_w is not null"]
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女方', '男方']
    xlabels = ['本地', '非本地']
    figGen.drawDisease2('28', list_a, list_d, labels, xlabels, "guangdong_yunqianjianchabiao_2017", config.year,
                        isSort=False,figureText="pass",
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）")
    #
    # list_a = list_a2
    # list_d = list_d2
    # labels = xlabels
    # figGen.drawDiseaseDistrict('29', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])
    #
    # list_a = list_a1
    # list_d = list_d1
    # labels = xlabels
    # figGen.drawDiseaseDistrict('30', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
    #                            isPercent=True, complete=True, picType="spbar",
    #                            yLable="百分比（%）", hline=False,
    #                            hasTable=False, figureText="", colorList=[])

def pic3_2(figGen):
    # TODO 38为饼柱结合图
    list_a1 = ["(pregnancy_number_w>=1)", "(pregnancy_number_w=0)"]
    list_a2 = ["(pregnancy_number_w=1)", "(pregnancy_number_w=2)", "(pregnancy_number_w>=3)", "(pregnancy_number_w=0)"]
    list_d1 = ["", ""]
    list_d2 = ["", "", "", ""]
    labels1 = ['怀孕1次及以上', '未曾怀孕']
    labels2 = ['怀孕1次', '怀孕2次', '怀孕3次及以上', '未曾怀孕']
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = [labels1, labels2]
    figGen.drawTwoPie('38', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                      isPercent=True, complete=True)

    text_q = '全市平均水平'
    figGen.drawDistrict('39', "had_adverse_pregnancy_outcome_w=1", "had_adverse_pregnancy_outcome_w is not null", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=["r"])
    figGen.drawYearDistrict('40', "had_adverse_pregnancy_outcome_w=1", "had_adverse_pregnancy_outcome_w is not null", "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict('41',
                        "(pubes_w=1 or bubby_w=1 or vulva_w=1 or vagina_w=1 or secretion_w=1 or cervix_w=1 or uterine_mass_w=1 or (uterine_size_w between 1 and 2) or uterine_activity_w=1 or bilateral_annex_w=1)",
                        "", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('42',
                        "((testis_h between 1 and 3) or varicocele_h=1 or (prepuce_h between 1 and 2) or pubes_h!=0 or adam_s_apple_h!=0 or penis_h\
                            !=0 or epididymis_h!=0 or spermaduct_h!=0)",
                        "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])


    list_a = ["pubes_w=1", "bubby_w=1", "vulva_w=1", "vagina_w=1", "secretion_w=1", "cervix_w=1",
              "uterine_mass_w=1", "uterine_size_w between 1 and 2", "uterine_activity_w=1", "bilateral_annex_w=1"]
    list_d = ["", "", "", "", "", "", "", "", "", ""]
    labels = ["阴毛","乳房","外阴","阴道","分泌物","宫颈","子宫\n包块","子宫\n大小","子宫活\n动能力","子宫双\n侧附件"]
    figGen.drawDisease('43', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
                       isPercent=True, complete=True, picType="bar",
                       yLable="百分比（%）",figureText="pass")

    list_a = ["testis_h between 1 and 3","varicocele_h=1","prepuce_h between 1 and 2","pubes_h!=0","adam_s_apple_h!=0","penis_h\
                !=0","epididymis_h!=0","spermaduct_h!=0"]
    list_d = ["", "", "", "", "", "", "", ""]
    labels = ["睾丸","精索静\n脉曲张","包皮","阴毛","喉结","阴茎","附睾","输精管"]
    figGen.drawDisease('44', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
                       isPercent=True, complete=True, picType="bar",
                       yLable="百分比（%）",figureText="pass")

    text_q = '全市平均水平'
    figGen.drawDistrict('45',
                        "(contraception_gongneijieyuqi_w=1 or contraception_pixiamaizhiji_w=1 or contraception_waiyongbiyunyao_w=1 or contraception_koufubiyunyao_w=1)",
                        "", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

def pic3_3(figGen):
    text_q = '全市平均水平'
    figGen.drawDistrict('46', "(suffered_disease_gaoxueya_w=1 or suffered_disease_xinzangbing_w=1 or suffered_disease_tangniaobing_w=1 or suffered_disease_dianxian_w=1 or suffered_disease_jiazhuangxian_w=1 or suffered_disease_manxingshenyan_w=1 or suffered_disease_zhongliu_w=1)", "is_had_disease_w is not null", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('47', "(suffered_disease_gaoxueya_h=1 or suffered_disease_xinzangbing_h=1 or suffered_disease_tangniaobing_h=1 or suffered_disease_dianxian_h=1 or suffered_disease_jiazhuangxianjibing_h=1 or suffered_disease_manxingshenyan_h=1 or suffered_disease_zhongliu_h=1)", "is_had_disease_h is not null", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    list_a = ['suffered_disease_gaoxueya_w=1', 'suffered_disease_xinzangbing_w=1', 'suffered_disease_tangniaobing_w=1', 'suffered_disease_dianxian_w=1', 'suffered_disease_jiazhuangxian_w=1', 'suffered_disease_manxingshenyan_w=1', 'suffered_disease_zhongliu_w=1']
    list_d = ['is_had_disease_w is not null','is_had_disease_w is not null','is_had_disease_w is not null','is_had_disease_w is not null','is_had_disease_w is not null','is_had_disease_w is not null','is_had_disease_w is not null']
    labels = ["高血压", "心脏病", "糖尿病", "癫痫", "甲状腺疾病", "慢性肾炎", "肿瘤"]
    figGen.drawDisease('48',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017", "all",config.year,
                           isPercent=True, complete=True,picType="hbar",
                           xLable="百分比（%）",upSort=False,colorList=['r'])

    list_a = ['suffered_disease_gaoxueya_h=1', 'suffered_disease_xinzangbing_h=1', 'suffered_disease_tangniaobing_h=1', 'suffered_disease_dianxian_h=1', 'suffered_disease_jiazhuangxianjibing_h=1',
              'suffered_disease_manxingshenyan_h=1', 'suffered_disease_zhongliu_h=1']
    list_d = ['is_had_disease_h is not null', 'is_had_disease_h is not null', 'is_had_disease_h is not null', 'is_had_disease_h is not null',
              'is_had_disease_h is not null', 'is_had_disease_h is not null', 'is_had_disease_h is not null']
    figGen.drawDisease('49', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", "all", config.year,
                       isPercent=True, complete=True, picType="hbar",
                       xLable="百分比（%）",upSort=False,colorList=['b'])
    #TODO 目前是手动找出前3然后调用
    list_a = ['suffered_disease_gaoxueya_w=1', 'suffered_disease_jiazhuangxian_w=1','suffered_disease_zhongliu_w=1']
    list_d = ['is_had_disease_w is not null','is_had_disease_w is not null', 'is_had_disease_w is not null']
    labels = ["高血压","甲状腺疾病", "肿瘤"]
    figGen.drawDiseaseYear('50', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ['suffered_disease_gaoxueya_h=1', 'suffered_disease_jiazhuangxianjibing_h=1', 'suffered_disease_tangniaobing_h=1']
    list_d = ['is_had_disease_h is not null', 'is_had_disease_h is not null', 'is_had_disease_h is not null']
    labels = ["高血压", "甲状腺疾病", "糖尿病"]
    figGen.drawDiseaseYear('51', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ["(systolic_pressure_w >= 140 or diastolic_pressure_w >= 90)", "(systolic_pressure_h >= 140 or diastolic_pressure_h >= 90)"]
    list_d = ["systolic_pressure_w is not null or diastolic_pressure_w is not null", "systolic_pressure_h is not null or diastolic_pressure_h is not null"]
    labels = ["女方", "男方"]
    figGen.drawDiseaseDistrict('52', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])
    figGen.drawYearDistrict('53', list_a[0], list_d[0], "guangdong_yunqianjianchabiao_2017",config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('54', list_a[1], list_d[1], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict('55-1',"(check_value_xuetang_w >= 6.10)","check_value_xuetang_w is not null", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('55-2',
                        "(check_value_xuetang_w>=7.0 or suffered_disease_tangniaobing_w=1)",
                        "(check_value_xuetang_w is not null or suffered_disease_tangniaobing_w is not null)", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    figGen.drawYearDistrict('56-1', "(check_value_xuetang_w >= 6.10)","check_value_xuetang_w is not null", "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('56-2', "(check_value_xuetang_w>=7.0 or suffered_disease_tangniaobing_w=1)",
                        "(check_value_xuetang_w is not null or suffered_disease_tangniaobing_w is not null)", "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    text_q = '全市平均水平'
    figGen.drawDistrict('57', "(check_value_cujiazhuangxianjisu_w<0.44 or check_value_cujiazhuangxianjisu_w>3.45)", "check_value_cujiazhuangxianjisu_w is not null", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawYearDistrict('58', "(check_value_cujiazhuangxianjisu_w<0.44 or check_value_cujiazhuangxianjisu_w>3.45)", "check_value_cujiazhuangxianjisu_w is not null", "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a = ["check_value_ganshenggongnengzhuananmei_w>45", "check_value_gangongzhuananmei_h>45"]
    list_d = ["check_value_ganshenggongnengzhuananmei_w is not null", "check_value_gangongzhuananmei_h is not null"]
    labels = ['女性', '男性']
    figGen.drawDiseaseDistrict('59', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=['r', 'b'])
    figGen.drawYearDistrict('60', list_a[0], list_d[0], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('61', list_a[1], list_d[1], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a = ["(check_value_ganshengongnengjigan_w>73 or check_value_ganshengongnengjigan_w<41)", "(check_value_shengongjigan_h > 97 or check_value_shengongjigan_h<57)"]
    list_d = ["check_value_ganshengongnengjigan_w is not null", "check_value_shengongjigan_h is not null"]
    labels = ['女性', '男性']
    figGen.drawDiseaseDistrict('62', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=['r', 'b'])
    figGen.drawYearDistrict('63', list_a[0], list_d[0], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('64', list_a[1], list_d[1], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

def pic3_4(figGen):
    text_q = '全市平均水平'
    figGen.drawDistrict('65', "(suffered_disease_jihe_w=1 or suffered_disease_yixingganyan_w=1 or suffered_disease_linbingmeiduyiyuanti_w=1)",
                        "is_had_disease_w is not null", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('66', "(suffered_disease_jiehe_h=1 or suffered_disease_yixingganyan_h=1 or suffered_disease_linbingmeiduyiyuanti_h=1)",
                        "is_had_disease_h is not null", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawYearDistrict('67', "(suffered_disease_jihe_w=1 or suffered_disease_yixingganyan_w=1 or suffered_disease_linbingmeiduyiyuanti_w=1)",
                        "is_had_disease_w is not null", "guangdong_yunqianjianchabiao_2017",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('68', "(suffered_disease_jiehe_h=1 or suffered_disease_yixingganyan_h=1 or suffered_disease_linbingmeiduyiyuanti_h=1)",
                        "is_had_disease_h is not null", "guangdong_yunqianjianchabiao_2017",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a1 = ['suffered_disease_jihe_w=1', 'suffered_disease_yixingganyan_w=1',
               'suffered_disease_linbingmeiduyiyuanti_w=1']
    list_a2 = ['suffered_disease_jiehe_h=1', 'suffered_disease_yixingganyan_h=1',
               'suffered_disease_linbingmeiduyiyuanti_h=1']
    list_d1 = ["is_had_disease_w is not null", "is_had_disease_w is not null",
               "is_had_disease_w is not null"]
    list_d2 = ["is_had_disease_h is not null", "is_had_disease_h is not null",
               "is_had_disease_h is not null"]
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女性', '男性']
    xlabels = ['结核', '乙肝', "性病"]
    figGen.drawDisease2('69', list_a, list_d, labels, xlabels, "guangdong_yunqianjianchabiao_2017", config.year, isSort=True,
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）",figureText="pass")

    figGen.drawDistrict('70', "(check_value_bingdushaichajuxibaoigm_w=1)", "", "guangdong_yunqianjianchabiao_2017",
                        config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('71', "(check_value_bingdushaichagognxingtiigm_w=1)", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('72', "(check_value_bingdushaichafengzhengbingdu_w=1)", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    list_a = ["check_value_yiganxueqinghbsag_w=1", "check_value_yiganxueiqnghbsag_h=1"]
    list_d = ["", ""]
    labels = ['女性', '男性']
    figGen.drawDiseaseDistrict('73', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=True,
                               hasTable=False, figureText="case", colorList=['r', 'b'])

    text_q = '全市平均水平'
    figGen.drawDistrict('74', "(check_value_meiduluoxianti_h=1)", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=['b'])
    figGen.drawDistrict('75', "(check_value_meiduluoxuanti_w=1)", "", "guangdong_yunqianjianchabiao_2017", config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=['r'])

    figGen.drawYearDistrict('76', "(check_value_meiduluoxuanti_w=1)", "", "guangdong_yunqianjianchabiao_2017",
                            config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('77', "(check_value_meiduluoxianti_h=1)", "", "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")



def pic3_5(figGen):
    # list_a = ["is_take_medicine_w=1","is_take_medicine_h=1"]
    # list_d = ["is_take_medicine_w is not null","is_take_medicine_h is not null"]
    # labels = ["女","男"]
    # figGen.figureHelper.nfigsize = [6,4.8]
    # figGen.drawDisease('78',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017", "all",config.year,
    #                        isPercent=True, complete=True,picType="bar",figureText="pass",
    #                        yLable="百分比（%）")
    # figGen.figureHelper.nfigsize = [8,4.8]
    # labels = ["女方","男方"]
    # figGen.drawDiseaseDistrict('79',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True, complete=True,picType="bar",
    #                        yLable="百分比（%）",hline=False,
    #                        hasTable=True, figureText="", colorList=[])
    #
    # labels = ["女","男"]
    # figGen.drawDiseaseYear('80',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,
    #                        yLable="百分比（%）")
    #
    #
    # text_q = '全市平均水平'
    # figGen.drawDistrict('92',"(is_somke_w=1)","is_somke_w is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=["r"])
    # figGen.drawDistrict('93',"(is_somke_h=1)","is_somke_h is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=["b"])

    list_a = ["is_passive_smoking_w=1","is_passive_smoking_w=2"]
    list_d = ["is_passive_smoking_w is not null","is_passive_smoking_w is not null"]
    labels = ["偶尔","经常"]
    figGen.drawDiseaseDistrict('94',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
                           isPercent=True, complete=True,picType="stbar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    list_a = ["is_passive_smoking_h=1","is_passive_smoking_h=2"]
    list_d = ["is_passive_smoking_h is not null","is_passive_smoking_h is not null"]
    figGen.drawDiseaseDistrict('95',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
                           isPercent=True, complete=True,picType="stbar",
                           yLable="百分比（%）",hline=False,
                           hasTable=True, figureText="", colorList=[])

    # figGen.drawYearDistrict('96',"(is_somke_w=1)","is_somke_w is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    # figGen.drawYearDistrict('97',"(is_somke_h=1)","is_somke_h is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    #
    # text_q = '全市平均水平'
    # figGen.drawDistrict('98',"(is_drink_w=1 or is_drink_w=2)","is_drink_w is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=[])
    # figGen.drawDistrict('99',"(is_drink_h=1 or is_drink_h=2)","is_drink_h is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=[])
    #
    # figGen.drawYearDistrict('100',"(is_drink_w=2)","is_drink_w is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    # figGen.drawYearDistrict('101',"(is_drink_h=2)","is_drink_h is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    #
    # text_q = '全市平均水平'
    # figGen.drawDistrict('102',"(is_harmful_environment_h=1)","is_harmful_environment_h is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=["b"])
    # figGen.drawDistrict('103',"(is_harmful_environment_w=1)","is_harmful_environment_w is not null","guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True,  complete= True,figureText=text_q,
    #                         yLable="百分比（%）",colorList=["r"])

    list_a = ['harmful_environment_shexian_h=1', 'harmful_environment_zaoyin_h=1', 'harmful_environment_qiangongzhongjinshu_h=1',
              'harmful_environment_xinzhuangxiu_h=1','harmful_environment_gaowen_h=1',
              'harmful_environment_jiechumaogoushengchu_h=1','harmful_environment_zhendong_h=1',
              'harmful_environment_nongyao_h=1']
    list_d = ['harmful_environment_shexian_h is not null', 'harmful_environment_zaoyin_h is not null', 'harmful_environment_qiangongzhongjinshu_h is not null',
              'harmful_environment_xinzhuangxiu_h is not null','harmful_environment_gaowen_h is not null',
              'harmful_environment_jiechumaogoushengchu_h is not null','harmful_environment_zhendong_h is not null',
              'harmful_environment_nongyao_h is not null']
    labels = ['接触\n辐射', '接触\n噪音', '接触\n重金属', '接触有\n机溶剂', '接触\n高温', '接触\n猫狗', '接触\n振动', '接触\n农药']
    figGen.drawDisease('104',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    list_a = ['harmful_environment_shexian_w=1', 'harmful_environment_zaosheng_w=1',
              'harmful_environment_qiangongzhongjinshu_w=1',
              'harmful_environment_xinzhuangxiu_w=1', 'harmful_environment_gaowen_w=1',
              'harmful_environment_maogoushengchu_w=1', 'harmful_environment_zhendong_w=1',
              'harmful_environment_nongyao_w=1']
    list_d = ['harmful_environment_shexian_w is not null', 'harmful_environment_zaosheng_w is not null',
              'harmful_environment_qiangongzhongjinshu_w is not null',
              'harmful_environment_xinzhuangxiu_w is not null', 'harmful_environment_gaowen_w is not null',
              'harmful_environment_maogoushengchu_w is not null', 'harmful_environment_zhendong_w is not null',
              'harmful_environment_nongyao_w is not null']
    figGen.drawDisease('105',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017", "all",config.year,
                           isPercent=True, complete=True,picType="bar",
                           yLable="百分比（%）")
    #
    # list_a = ["(is_pressure_w between 3 and 4)","(is_pressure_h between 3 and 4)"]
    # list_d = ["is_pressure_w is not null","is_pressure_h is not null"]
    # labels = ["女方","男方"]
    # figGen.drawDiseaseDistrict('106',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True, complete=True,picType="bar",
    #                        yLable="百分比（%）",hline=False,
    #                        hasTable=True, figureText="", colorList=[])
    #
    # list_a = ["(is_economic_pressure_w between 3 and 4)","(is_economic_pressure_h between 3 and 4)"]
    # list_d = ["is_economic_pressure_w is not null","is_economic_pressure_h is not null"]
    # labels = ["女方","男方"]
    # figGen.drawDiseaseDistrict('107',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True, complete=True,picType="bar",
    #                        yLable="百分比（%）",hline=False,
    #                        hasTable=True, figureText="", colorList=[])
    #
    # list_a = ["(is_relationship_tense between 3 and 4)","(is_relationship_tense_h between 3 and 4)"]
    # list_d = ["is_relationship_tense is not null","is_relationship_tense_h is not null"]
    # labels = ["女方","男方"]
    # figGen.drawDiseaseDistrict('108',list_a, list_d, labels,"guangdong_yunqianjianchabiao_2017",config.year,
    #                        isPercent=True, complete=True,picType="bar",
    #                        yLable="百分比（%）",hline=False,
    #                        hasTable=True, figureText="", colorList=[])
    #
    #
    # figGen.drawYearDistrict('109',"(is_pressure_h between 3 and 4)","is_pressure_h is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    # figGen.drawYearDistrict('110',"(is_pressure_w between 3 and 4)","is_pressure_w is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    #
    # figGen.drawYearDistrict('111',"(is_economic_pressure_h between 3 and 4)","is_economic_pressure_h is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    # figGen.drawYearDistrict('112',"(is_economic_pressure_w between 3 and 4)","is_economic_pressure_w is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    #
    # figGen.drawYearDistrict('113',"(is_relationship_tense_h between 3 and 4)","is_relationship_tense_h is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")
    # figGen.drawYearDistrict('114',"(is_relationship_tense between 3 and 4)","is_relationship_tense is not null","guangdong_yunqianjianchabiao_2017",config.year,2,
    #                        isPercent=True, complete=True,yLable="百分比（%）")

def pic3_1(figGen):
    text_q = '全市平均水平'
    a1 = "(is_born_ill=1 or thalassaemia =1 or down_syndrome=1 or albinism=1 or suffered_disease_tangniaobing_w1=1 or blood_sick=1 or  dysgnosia=1 or favism=1 or congenital_suffered_disease_xinzangbing_w=1 or hearing_disorder=1 or seeing_disorder=1 or infant_mortality=1 or sterility=1 or intermarry=1)"
    d1 = "(is_born_ill is not null or thalassaemia is not null or down_syndrome is not null or albinism is not null or suffered_disease_tangniaobing_w1 is not null or blood_sick is not null or  dysgnosia is not null or favism is not null or congenital_suffered_disease_xinzangbing_w is not null or hearing_disorder is not null or seeing_disorder is not null or infant_mortality is not null or sterility is not null or intermarry is not null)"
    a2 = "(is_born_ill=1 or thalassaemia =1 or down_syndrome=1 or albinism=1 or suffered_disease_tangniaobing_w1=1 or blood_sick=1 or  dysgnosia=1 or favism=1 or congenital_suffered_disease_xinzangbing_w=1 or hearing_disorder=1 or seeing_disorder=1 or infant_mortality=1 or sterility=1 or intermarry=1)"
    d2 = "(is_born_ill is not null or thalassaemia is not null or down_syndrome is not null or albinism is not null or suffered_disease_tangniaobing_w1 is not null or blood_sick is not null or  dysgnosia is not null or favism is not null or congenital_suffered_disease_xinzangbing_w is not null or hearing_disorder is not null or seeing_disorder is not null or infant_mortality is not null or sterility is not null or intermarry is not null)"
    figGen.drawDistrict('31',a1,d1, "guangdong_yunqianjianchabiao_2017",config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])
    figGen.drawDistrict('32',a2,d2, "guangdong_yunqianjianchabiao_2017",config.year,
                        isPercent=True, complete=True, figureText=text_q,
                        yLable="百分比（%）", colorList=[])

    figGen.drawYearDistrict('33', a1, d1, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('34', a2, d2, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")

    list_a1 = ['blood_sick =1', 'favism =1', 'congenital_suffered_disease_xinzangbing_w=1',
               'infant_mortality=1','(hearing_disorder=1 or seeing_disorder=1)','dysgnosia=1']
    list_a2 = ['blood_sick =1', 'favism =1', 'congenital_suffered_disease_xinzangbing_w=1',
               'infant_mortality=1','(hearing_disorder=1 or seeing_disorder=1)','dysgnosia=1']
    list_d1 = ['blood_sick  is not null', 'favism  is not null', 'congenital_suffered_disease_xinzangbing_w is not null',
               'infant_mortality is not null','(hearing_disorder is not null or seeing_disorder is not null)','dysgnosia is not null']
    list_d2 = ['blood_sick  is not null', 'favism  is not null', 'congenital_suffered_disease_xinzangbing_w is not null',
               'infant_mortality is not null','(hearing_disorder is not null or seeing_disorder is not null)','dysgnosia is not null']
    list_a = [list_a1, list_a2]
    list_d = [list_d1, list_d2]
    labels = ['女方', '男方']
    xlabels = ['地中海贫血', 'G6PD缺乏症', "先天性心脏病", '新生儿或婴\n幼儿死亡史', "内生障碍", '先天性智\n力低下']
    figGen.drawDisease2('35', list_a, list_d, labels, xlabels, "guangdong_yunqianjianchabiao_2017", config.year, isSort=True,
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
    figGen.drawDisease2('36', list_a, list_d, labels, xlabels, "guangdong_yunqianjianchabiao_2017", config.year, isSort=False,
                        isPercent=True, complete=True, picType="bar",
                        yLable="百分比（%）",figureText='pass',colorList=['r','b'])

    figGen.figureHelper.nfigsize = [8, 5.8]
    # list_a = [a1,b1,a2,b2]
    list_a = ['', '', '', '']
    list_d = ['','','','']
    labels = ["女性α地贫", '女性β地贫', "男性α地贫", '男性β地贫']
    figGen.drawDiseaseDistrict('37', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))
    figGen.figureHelper.nfigsize = [8, 4.8]

def pic3_6(figGen):

    list_a = ['(is_eat_meat_egg_w=0)', '(is_anorexia_vegetables_w=1)', '(is_eat_raw_meat_w=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseDistrict('81', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))

    list_a = ['(is_eat_meat_egg_h=0)', '(is_anorexia_vegetables_h=1)', '(is_eat_raw_meat_h=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseDistrict('82', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="百分比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[],gridcol=(24,21))

    list_a = ['(is_eat_meat_egg_w=0)', '(is_anorexia_vegetables_w=1)', '(is_eat_raw_meat_w=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseYear('83', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ['(is_eat_meat_egg_h=0)', '(is_anorexia_vegetables_h=1)', '(is_eat_raw_meat_h=1)']
    list_d = ['', '', '', '']
    labels = ["素食者", '厌食蔬菜', "食用生肉"]
    figGen.drawDiseaseYear('84', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）")

    list_a = ['(bmi_w < 18.5)', '(bmi_w >= 24 and bmi_w < 28)', '(bmi_w >= 28)']
    list_d = ['', '', '', '']
    labels = ["低体重", '超重', "肥胖"]
    figGen.drawDiseaseYear('85', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）",isSort = False)

    list_a = ['(bmi_h < 18.5)', '(bmi_h >= 24 and bmi_h < 28)', '(bmi_h >= 28)']
    list_d = ['', '', '', '']
    labels = ["低体重", '超重', "肥胖"]
    figGen.drawDiseaseYear('86', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year, 2,
                           isPercent=True, complete=True,
                           yLable="百分比（%）",isSort = False)

    figGen.figureHelper.nfigsize = [8, 5.8]
    list_a = ["(bmi_w >= 28)", "(bmi_w >= 24 and bmi_w < 28)", "(bmi_w >= 18.5 and bmi_w < 24)", "(bmi_w < 18.5)"]
    list_d = ["bmi_w is not null", "bmi_w is not null", "bmi_w is not null", "bmi_w is not null"]
    labels = ["肥胖","偏重","正常","偏瘦"]
    figGen.drawDiseaseDistrict('87', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])

    list_a = ["(bmi_h >= 28)", "(bmi_h >= 24 and bmi_h < 28)", "(bmi_h >= 18.5 and bmi_h < 24)", "(bmi_h < 18.5)"]
    list_d = ["bmi_h is not null", "bmi_h is not null", "bmi_h is not null", "bmi_h is not null"]
    labels = ["肥胖","偏重","正常","偏瘦"]
    figGen.drawDiseaseDistrict('88', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="spbar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])
    figGen.figureHelper.nfigsize = [8, 4.8]

    list_a = ["(suffered_disease_pinxue_w=1)", "(check_value_xuechangguixuehongdaiban_w<110)"]
    list_d = ["(is_had_disease_w is not null and check_value_xuechangguixuehongdaiban_w<110)",'check_value_xuechangguixuehongdaiban_w is not null']
    labels = ["自报患病率", "检出率"]
    figGen.drawDiseaseDistrict('89', list_a, list_d, labels, "guangdong_yunqianjianchabiao_2017", config.year,
                               isPercent=True, complete=True, picType="bar",
                               yLable="构成比（%）", hline=False,
                               hasTable=True, figureText="", colorList=[])

    figGen.drawYearDistrict('90', list_a[0], list_d[0], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")
    figGen.drawYearDistrict('91', list_a[1], list_d[1], "guangdong_yunqianjianchabiao_2017", config.year, 2,
                            isPercent=True, complete=True, yLable="百分比（%）")



if __name__ == '__main__':
    config = Config()
    inter = Interpreter(config)
    figGen = figureGenerate(config,inter,[8,4.8])

    # pic3_1(figGen)
    # pic3_2(figGen)
    # pic3_3(figGen)
    # pic3_4(figGen)
    pic3_5(figGen)
    # pic3_6(figGen)


    # pic1(figGen)
    # pic2(figGen)


    figGen.finish()
