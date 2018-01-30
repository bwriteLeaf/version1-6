# -*- coding:utf-8 -*-
'''
    数据库调取封装：
'''


import os
import sys
import pdb
import pandas as pd
from configuration import Config
from interpreter import Interpreter
import traceback

class DBInterface:

    def __init__(self, conf, inter):
        self.__conf = conf
        self.__inter = inter

    # 得到该城市所有地区的数目，名字，第一列为code，第二列为字符串
    def getDistricts(self):
        df = pd.read_csv(os.path.join(self.__conf.supFilePath, 'county_6_code.csv'), sep=',', encoding='utf-8',
                         engine='python')
        lb = int(str(self.__conf.code) + '00')
        ub = int(str(self.__conf.code) + '99')
        district_list = []
        for i in range(0, len(df)):
            code = int(df["id"][i])
            name = df["name"][i][6:]
            if (code >= lb) and (code <= ub):
                district_list.append((code, name))
        return district_list

     # 输入：最基本的SQL表达式
     # 返回执行结果，一个数值 int
    def execSQL(self,serviceCode,expr,dbName,year,complete):
        try:
            serviceCode = str(serviceCode)
            year = str(year)

            year_str = "service_time"
            complete_str = " and complete=1"
            service_str = "service_code"

            if dbName == "early":
                year_str = "earlyfollowup_time"
                complete_str = " and earlyyncomplete=1"
            elif dbName == "outcome":
                year_str = "followup_time"
                complete_str = " and yncomplete=1"
            elif dbName == "exam, early":
                year_str = "exam.complete_date"
                service_str = "exam.service_code"

            sql = "select count(*) from " + dbName + " where "+service_str+" like '" + serviceCode + "%" \
                     + "' and "+year_str+" between '" + year + "-01-01' and '" + year + "-12-31'"
            if len(expr) != 0:
                sql = sql + " and " + expr
            if complete:
                sql = sql + complete_str
            return self.__executeSQL(sql, 1, 1)

        except Exception as e:
            print(traceback.print_exc())

    #输入：分子的sql表达式，分母的sql表达式
    #返回List，[('大鹏新区', 8.8), ('罗湖区', 5.0), ('龙华新区', 4.8)]
    def getDistrictData(self,attrExpr,divideExpr,diseaseName,dbName,districtType,year,isPercent=True,complete=True):
        ret_list = []
        if (districtType != "all") and (districtType != "district"):
            print('接口调用错误 getDistrictData districtType wrong', file=sys.__stdout__)
            return ret_list
        #得到该城市所有地区的数目，名字，第一列为code，第二列为字符串
        district_list = self.getDistricts()
        for i in range(0,len(district_list)):
            code_district = district_list[i][0]
            name_district = district_list[i][1]
            if districtType == "all":
                code_district = str(self.__conf.code)
                name_district = diseaseName
            #sql分别执行
            r_up_s = self.execSQL(code_district,attrExpr,dbName,year,complete)
            r_up = int(r_up_s)
            if isPercent:
                r_down_s = self.execSQL(code_district,divideExpr,dbName,year,complete)
                r_down = int(r_down_s)
                percentage = r_up / r_down * 100
                percentage = round(percentage, 2)
                ret_list.append((name_district, percentage))
            else:
                ret_list.append((name_district, r_up))

            if (districtType == "all") and (i==0):
                break
        return ret_list

    #输入：分子的sql表达式，分母的sql表达式
    #返回List，多个List，每个小类指标一个List
    def getDiffDistrictData(self,attrExprList,divideExprList,diseaseNameList,dbName,districtType,year,isPercent=True,complete=True):
        dif_list = []
        diseaseName = ""
        for j in range(0,len(attrExprList)):
            if districtType == "all":
                diseaseName = diseaseNameList[j]
            attrExpr = attrExprList[j]
            divideExpr = ""
            if isPercent:
                divideExpr = divideExprList[j]
            ret_list = self.getDistrictData(attrExpr,divideExpr,diseaseName,dbName,districtType,year,isPercent,complete)
            dif_list.append(ret_list)
        return dif_list

    #对一个二维数组进行排序
    def sortArray(self,dataRaw):
        all_list = []
        for i in range(0, len(dataRaw)):
            data_now = dataRaw[i]
            for j in range(0,len(data_now)):
                if i==0:
                    all_list.append(list(data_now[j]))
                else:
                    all_list[j].append(data_now[j][1])
        sorted_list = sorted(all_list, key=lambda all_list: all_list[1], reverse=1)
        return sorted_list

        # 对一个二维数组不进行排序返回类似格式
    def noSortArray(self,dataRaw):
        all_list = []
        for i in range(0, len(dataRaw)):
            data_now = dataRaw[i]
            for j in range(0,len(data_now)):
                if i==0:
                    all_list.append(list(data_now[j]))
                else:
                    all_list[j].append(data_now[j][1])
        return all_list

    def timeArray(self, dataRawList):
        all_list = []
        diseaseCnt = len(dataRawList[0])
        yearCnt = len(dataRawList)
        for i in range(0, diseaseCnt):
            for j in range(0, yearCnt):
                data_now = dataRawList[j]  # 每年
                if i == 0:
                    all_list.append(list(data_now[i][0]))
                    all_list[j].append(list(data_now[i][0]))
                else:
                    all_list[j].append(list(data_now[i][0]))
                    if i == 1:
                        del(all_list[j][0])
                        del(all_list[j][0])
        return all_list


    def sortList(self,dataRaw,sortType = True):
        if sortType:
            return  sorted(dataRaw, key=lambda dataRaw: dataRaw[1], reverse=1)
        else:
            return sorted(dataRaw, key=lambda dataRaw: dataRaw[1])

    def getTopk(self,attrExprList, divideExprList,diseaseNameList, dbName,mainType,retType,k, year,sortType=True,isPercent=True,complete=True):
        ret_list = []
        sorted_list = []

        if mainType == "disease":
            data_raw = self.getDiffDistrictData(attrExprList, divideExprList,diseaseNameList, dbName, "all", year,isPercent, complete)
            ret_list = [x[0] for x in data_raw]
        if mainType == "district":
            data_raw = self.getDiffDistrictData(attrExprList, divideExprList,diseaseNameList, dbName,"district", year,isPercent, complete)
            ret_list = data_raw[0]

        if sortType:
            sorted_list = sorted(ret_list, key=lambda ret_list: ret_list[1],reverse=1)
        else:
            sorted_list = sorted(ret_list, key=lambda ret_list: ret_list[1])

        if retType == "text":
            return sorted_list[k-1][0]
        elif retType == "num":
            return str(sorted_list[k-1][1]) + "%"
        elif retType == "texts":
            ret = ""
            for i in range(0,k-1):
                ret = ret + sorted_list[i][0] + "、"
            ret = ret + sorted_list[k-1][0]
            return ret
        elif retType == "nums":
            ret = ""
            for i in range(0,k-1):
                ret = ret + str(sorted_list[i][1]) + "%、"
            ret = ret + str(sorted_list[k-1][1]) + "%"
            return ret
        return sorted_list[0:k]

    def getOneData(self,attrExprList, divideExprList, dbName, isPercent=True,complete=True):
        attrExpr, divideExpr = attrExprList[0], divideExprList[0]
        this_year = self.__conf.year
        dataRaw = self.getDistrictData(attrExpr, divideExpr, "",dbName,"all", this_year, isPercent,complete)
        return dataRaw[0][1]

    #得到两年：今年去年所有地区的数值
    def getTwoYearByDistrict(self,attrExpr, divideExpr, dbName,districtType, complete):
        this_year = self.__conf.year
        last_year = this_year-0
        this_list = self.getDistrictData(attrExpr, divideExpr, "",dbName,districtType, this_year, complete)
        last_list = self.getDistrictData(attrExpr, divideExpr,"", dbName,districtType,last_year, complete)

        return this_list, last_list


    #两年的数值比较，返回所有今年高于去年、低于去年、持平的地区名称
    def getDistrictTwoYear(self,attrExprList, divideExprList, dbName,mainType, complete):
        attrExpr, divideExpr = attrExprList[0], divideExprList[0]
        this_list, last_list = self.getTwoYearByDistrict(attrExpr, divideExpr, dbName,"district", complete)
        bigger = []
        smaller = []
        same = []
        for i in range(0, len(this_list)):
            district = this_list[i][0]
            for j in range(0, len(this_list)):
                district_now = last_list[j][0]
                if district == district_now:
                    break

            sub = this_list[i][1] - last_list[j][1]
            if sub > 0:
                bigger.append((district, sub))
            elif sub < 0:
                smaller.append((district, sub))
            else:
                same.append((district, sub))

        bigger = self.sortList(bigger)
        smaller = self.sortList(smaller,False)

        ret = ""
        if mainType == "high":
            k = len(bigger)
            for i in range(0,  k - 1):
                ret = ret + bigger[i][0] + "、"
            if k != 0:
                ret = ret + bigger[k - 1][0]
        elif mainType == "low":
            k = len(smaller)
            for i in range(0, k - 1):
                ret = ret + smaller[i][0] + "、"
            if k != 0:
                ret = ret + smaller[k - 1][0]
        elif mainType == "same":
            k = len(same)
            for i in range(0, k - 1):
                ret = ret + same[i][0] + "、"
            if k != 0:
                ret = ret + same[k - 1][0]
        else:
            ret = bigger, smaller, same

        return ret

    def textSubstitute(self, attrExprList, divideExprList,diseaseNameList, dbName,mainType,textList,dimenType, complete):
        sub = 0
        if mainType == "disease":
            data_raw = self.getDiffDistrictData(attrExprList, divideExprList,diseaseNameList, dbName, "all", self.__conf.year,
                                isPercent=True, complete=True)
            ret_list = [x[0] for x in data_raw]
            sub = ret_list[0][1] - ret_list[1][1]

        if mainType == "year":
            this_list, last_list = self.getTwoYearByDistrict(attrExprList[0], divideExprList[0], dbName, "all", complete)
            sub = this_list[0][1] - last_list[0][1]

        if sub > 0:
            return textList[0]
        elif sub == 0:
            return textList[1]
        else:
            return textList[2]


    # 执行sql语句
    # tupleCount: 表示返回查询结果的数量
    # elementCount: 表示每条查询结果中返回字段的数量
    # 除非返回的结果仅有一条记录且该记录仅有一个元素，返回该元素的值，否则返回值均为列表，列表元素均为元组
    def __executeSQL(self, sql, tupleCnt=1, eleCnt=1):
        cur = self.__conf.dbConn.cursor()
        res = None
        try:
            totalCnt = cur.execute(sql)
            if totalCnt > tupleCnt:
                resTuple = cur.fetchall()[:tupleCnt]
            else:
                resTuple = cur.fetchall()
            res = [0 for x in range(0, tupleCnt)]
            if resTuple is not None:
                for x in range(0, tupleCnt):
                    res[x] = resTuple[x][:eleCnt]
            self.__conf.dbConn.commit()
            if res is not None and len(res) == 1 and len(res[0]) == 1:
                res = res[0][0]
        except Exception as e:
            print('查询数据库错误', file=sys.__stdout__)
            print(sql)
          #  self.__inter.__log(sql)
          #  self.__inter.__log(e)
            self.__conf.dbConn.rollback()
        return res

if __name__ == '__main__':

    config = Config()
    inter = Interpreter(config)
    dbInf = DBInterface(config, inter)
    # print(dbInf.getDiffDistrictData(["use_medicine=1"],["use_medicine is not null"],["服药"],"exam","all",config.year,True,True))
    # print(dbInf.getDiffDistrictData(["use_medicine=1"],["use_medicine is not null"],[],"exam","district",config.year,True,True))
    # print(dbInf.getDiffDistrictData(["use_medicine=1"],[""],[],"exam","district",config.year,False,True))

    #
    list_a = ["second_hand_smoking=1","second_hand_smoking=2"]
    list_b = ["second_hand_smoking is not null","second_hand_smoking is not null"]
    list_c = ['偶尔', '经常']
    list_d = ['高于', '等于', '低于']
    print(dbInf.getDiffDistrictData(list_a,list_b,list_c,"exam","all",config.year,True,True))
    print(dbInf.getDiffDistrictData(list_a,list_b,list_c,"exam","district",config.year,False,True))
    print(dbInf.getDistrictTwoYear(["use_medicine=1"],["use_medicine is not null"],"exam","same",True))
    print(dbInf.textSubstitute(list_a,list_b,list_c,"exam","disease",list_d,"1",True))
    print(dbInf.textSubstitute(list_a,list_b,[],"exam","year",list_d,"1",True))
    print(dbInf.getOneData(["(micro_sp=1)"],[""],"exam"))

    list_a = ["pubes!='0'","breast!='0'","vulva!='0'","vagina!='0'","secretions!='0'","vervix!='0'","uterus_bump!='0'","uterus_size!='0'","uterus_act!='0'","uterus_adnexa!='0'"]
    list_b = ["","","","","","","","","",""]
    list_c = ["阴毛异常","乳房异常","外阴异常","阴道异常","分泌物异常","宫颈异常","子宫包块","子宫大小异常","子宫活动度差","子宫双侧附件异常"]

    print(dbInf.getTopk(list_a,list_b,list_c,"exam","disease","texts",10,config.year,True))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","disease","nums",10,config.year,True))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","disease","text",4,config.year,True))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","disease","num",4,config.year,True))

    list_a = ["second_hand_smoking=1"]
    list_b = ["second_hand_smoking is not null"]
    list_c = ['偶尔']
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","district","texts",3,config.year,False))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","district","nums",3,config.year,False))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","district","text",1,config.year,False))
    print(dbInf.getTopk(list_a,list_b,list_c,"exam","district","num",1,config.year,False))