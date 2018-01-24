'''
    配置文件：记录相关配置信息
'''

import os
import pandas as pd
import pymysql
from json import load
from datetime import datetime

# TODO:添加生成日期的选择
class Config:

    def __init__(self):
        self.__ROOT = os.getcwd()
        self.__confJson = self.__getConfJson()
        self.__districts = self.__confJson['districts'] if 'districts' in self.__confJson else self.__getDistrictsConf()
        self.__year = self.__confJson['year'] if 'year' in self.__confJson else 2017
        self.__city = self.__confJson['city'] if 'city' in self.__confJson else self.__getCityConf()
        self.__date = self.__confJson['date'] if 'date' in self.__confJson else '\\today'
        self.__chapters = self.__confJson['chapters'] if 'chapters' in self.__confJson else 3
        self.__dbconn = self.__getDBConn()


    @property
    def tmpFilePath(self):
        return os.path.join(self.__ROOT, 'Templates')

    @property
    def ltxFilePath(self):
        return os.path.join(self.__ROOT, 'LaTeXFiles')

    @property
    def supFilePath(self):
        return os.path.join(self.__ROOT, 'SupportFiles')

    @property
    def logFilePath(self):
        return os.path.join(self.supFilePath, 'log')

    @property
    def districts(self):
        return self.__districts

    @property
    def date(self):
        return self.__date

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        try:
            value = int(value)
            if 1800 < value < 5000:
                self.__year = value
        except Exception as e:
            logFile = open(self.logFilePath, 'a')
            print('设置年份出错', file=logFile)
            print(e, file=logFile)
            logFile.close()
        return

    @property
    def city(self):
        return self.__city

    @property
    def chapters(self):
        return self.__chapters

    @property
    def confJson(self):
        return self.__confJson

    @property
    def dbConn(self):
        return self.__dbconn

    @property
    def code(self):
        return self.confJson['service_code']

    # 记录日志
    def __log(self, msg):
        logFile = open(self.logFilePath, 'a')
        print(msg, file=logFile)
        logFile.close()

    # 检查配置文件中的必要信息
    # 包括service_code
    def __checkConf(self, confJson, checkList=['service_code', 'DB']):
        checkFlag = False
        for item in checkList:
            if item not in confJson:
                checkFlag = True
                msg = '%s配置缺失，请检查配置文件'%item
                print(msg)
                self.__log(msg)
            elif item == 'DB':
                self.__checkConf(confJson['DB'], ['host', 'port', 'user', 'pwd', 'db'])
        if checkFlag:
            exit(1)
        return

    # 读取配置信息
    def __getConfJson(self):
        try:
            confFile = open(os.path.join(self.supFilePath, 'configuration.conf'), 'r', encoding='utf-8')
            tmpFile = open(os.path.join(self.supFilePath, 'configuration.tmp'), 'w', encoding='utf-8')
            for line in confFile:
                # 删除注释
                if not line.strip(' ').startswith('#'):
                    print(line, end='', file=tmpFile)
            confFile.close()
            tmpFile.close()
            tmpFile = open(os.path.join(self.supFilePath, 'configuration.tmp'), 'r', encoding='utf-8')
            confJson = load(tmpFile)
            tmpFile.close()
            os.remove(os.path.join(self.supFilePath, 'configuration.tmp'))
            # 检查配置文件中的必要信息是否齐全
            self.__checkConf(confJson)
            return confJson
        except Exception as e:
            print("读取配置文件出错，请保证配置文件格式正确")
            logFile = open(self.logFilePath, 'a')
            print(datetime.today(), e, file=logFile)
            logFile.close()
            exit(1)

    # 读取城市名称
    def __getCityConf(self):

        infile = open(os.path.join(self.supFilePath, 'county_6_code.csv'), 'r', encoding='utf-8')
        cnt = 0
        for line in infile:
            if cnt == 0:
                cnt += 1
                continue
            line = line.split(sep=',')
            try:
                if line[1].startswith(str(self.__confJson['service_code'])):
                    infile.close()
                    return line[0].split(sep='市')[0]+'市'

            except Exception as e:
                print('读取配置文件出错，请保证配置文件格式正确')
                logFile = open(self.logFilePath, 'a')
                print(datetime.today(), e, file=logFile)
                logFile.close()
                exit(1)
        # 未找到对应的地区代码
        infile.close()
        print('不存在的地址编码，请检查地址编码是否正确')
        exit(1)

    # 读取当前省市区的数量
    def __getDistrictsConf(self):
        df = pd.read_csv(os.path.join(self.supFilePath, 'county_6_code.csv'),sep=',', encoding='utf-8', engine='python')
        lb = int(str(self.__confJson['service_code']) + '00')
        ub = int(str(self.__confJson['service_code']) + '99')
        return df[(df.id >= lb) & (df.id <= ub)].count()[0]

    # 链接数据库
    def __getDBConn(self):
        conn = None
        try:
            conn = pymysql.connect(host=self.confJson['DB']['host'],
                                   port=self.confJson['DB']['port'],
                                   user=self.confJson['DB']['user'],
                                   password=self.confJson['DB']['pwd'],
                                   db=self.confJson['DB']['db'],
                                   charset='utf8')
            print("数据库链接成功")
        except Exception as e:
            print("数据库链接失败")
            self.__log(e)
        return conn