# -*- coding:utf-8 -*-
'''
    翻译模块：将txt模板编译生成为.tex文件
'''
import re
import pdb
import sys
import os
from datetime import datetime

class Interpreter:

    def __init__(self, conf):
        # 样式正则表达式
        self.__styleReg = re.compile(r'^\[chapter]|\[section]|\[subsection]|\[subsubsection]|\[subsection\*]|\[subsubsection\*]')
        # 表达式正则表达式
        self.__exprReg   = re.compile(r'{{expr:(int|float)[ ]*=[ ]*(.+?)}}')
        # TODO:修改正则表达式
        # 当前正则表达式可以匹配如{{fig=(name, caption, )}}的非法字符串
        self.__figReg = re.compile(r'{{fig[ ]*=[ ]*\((.+),(.+),([^)]+)\)}}')
        self.__tabReg = re.compile(r'{{tab[ ]*=[ ]*[^ ]+?}}')
        self.__lblReg = re.compile(r'{{label[ ]*=[ ]*([^ ]+?)}}')
        self.__sqlReg = re.compile(r'{{sql:\(([1-9]\d*),[ ]*([1-9]\d*)\)[ ]*=[ ]*(.+?)}}')
        self.__conf = conf

    def __log(self, msg):
        logfile = open(os.path.join(self.__conf.supFilePath, 'logger.log'), 'a', encoding='utf-8')
        print(datetime.today(), msg, file=logfile)
        logfile.close()
        return

    @property
    def styleReg(self):
        return self.__styleReg

    @property
    def figReg(self):
        return self.__figReg

    @property
    def lblReg(self):
        return self.__lblReg

    @property
    def sqlReg(self):
        return self.__sqlReg

    @property
    def exprReg(self):
        return self.__exprReg

    # 变量插值表达式解析
    # expr: 待分析的插值表达式
    def __expressionEval(self, expr):
        try:
            res = eval(expr)
        except:
            res = None
        return res

    # 对输入字符串进行样式检查
    def __styleCheck(self, txt):
        s = self.__styleReg.match(txt)
        if s is not None:
            s = s.group().strip('[]')
            print("生成%s中..."%(txt.strip('\n')), file=sys.__stdout__)
            txt = self.__styleReg.sub('\\'+s+'{', txt.strip('\n'))
            txt = txt+'}\n'
        return txt

    # 运算表达式检查
    def __expressionCheck(self, txt):
        # TODO: 获取匹配得到的表达式exp
        m = self.exprReg.split(txt)
        l = len(m)
        i = 0
        s = ''
        while i < l:
            if i == l-1:
                s += m[i]
            else:
                value = self.__expressionEval(m[i+2])
                if m[i+1] == 'int':
                    s = s + m[i] + ('None' if value is None else str(int(value)))
                else:
                    s = s + m[i] + ('None' if value is None else('%.2f' % value))
            i += 3
        return s

    # 图检查
    # FIXME:一行中插入多个图的时候，只替换第一个
#   \begin{figure}[htbp]
#     \centering
#     \includegraphics[width=1\textwidth]{1.png}
#     \caption{测试图片}
#     \label{123}
#   \end{figure}
    def __figureCheck(self, txt):
        m = self.__figReg.search(txt)
        if m is not None:
            # 获取匹配的整体字符串
            name = self.parse(m.groups()[0]).strip(' ')
            caption = self.parse(m.groups()[1]).strip(' ')
            label = self.parse(m.groups()[2]).strip(' ')
            # 这里的\\\\是为了在调用sub函数时能正确的输出\begin和\textwidth
            rpls = '\n\\\\begin{figure}[htbp]\n' \
                   '\t\centering\n' \
                   '\t\includegraphics[width=1\\\\textwidth]{%s}\n' \
                   '\t\caption{%s}\n' \
                   '\t\label{%s}\n' \
                   '\end{figure}\n'%(name, caption, label)
            # print('替换的图字符串为:%s'%rpls)
            txt = self.__figReg.sub(rpls, txt)

        return txt

    # 表检查
    # TODO: 待完善

    def __tableCheck(self, txt):
        return txt

    # 图表引用检查
    # TODO:重写循环
    # \ref{fig:logo}
    def __labelCheck(self, txt):
        m = self.__lblReg.split(txt)
        # 拼接并替换字符串
        # 分割后列表长度
        l = len(m)
        s = ''
        i = 0
        while i < l:
            if i == l-1:
                s += m[i]
            else:
                s += (m[i] + '\\ref{%s}'%m[i+1])
            i += 2
        return s
        # for label in m:
        #     txt = self.__lblReg.sub('\\\\ref{%s}'%label, txt)
        # if m is not None:
        #     label = m.groups()[0]
        #     txt = self.__lblReg.sub('\\\\ref{%s}' % label, txt)

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
            self.__log(sql)
            self.__log(e)
            self.__conf.dbConn.rollback()
        return res


    # sql语句引用检查
    def ___sqlCheck(self, txt):
        m = self.sqlReg.split(txt)
        l = len(m)
        s = ''
        i = 0
        while i < l:
            if i == l-1:
                s += m[i]
            else:
                tupleCnt = int(m[i+1])
                eleCnt = int(m[i+2])
                sql = m[i+3]
                # sql = self.__expressionCheck(m[i+1])

                res = self.__executeSQL(sql, tupleCnt, eleCnt)
                s += (m[i] + str(res))
            i += 4
        return s

    # 固定替换检查
    # 对固定的数值进行替换
    # 包括年份、城市、区域数量
    def __fixedReplace(self, txt):
        # 时间地点替换检查
        res = txt.replace('{{year}}', str(self.__conf.year))
        res = res.replace('{{year-1}}', str(self.__conf.year-1))
        res = res.replace('{{city}}', self.__conf.city)
        res = res.replace('{{districts}}', str(self.__conf.districts))
        res = res.replace('{{service_code}}', str(self.__conf.code))


        return res

    # 对输入字符串进行插值、图、表检查
    def __specialCheck(self, txt):
        # 固定替换检查
        res = self.__fixedReplace(txt)

        # SQL查询检查
        res = self.___sqlCheck(res)

        # 运算表达式检查
        res = self.__expressionCheck(res)

        # 图表引用检查
        res = self.__labelCheck(res)

        # 图检查
        res = self.__figureCheck(res)

        # 表检查
        res = self.__tableCheck(res)

        return res

    # 特殊字符替换
    def __symCheck(self, txt):
        # 将%替换为转义字符
        res = txt.replace('%', '\%')
        res = res.replace('_', '\_')

        return res

    # 解析输入字符串
    # txt: 待解析的字符串
    # ret: 解析后的tex格式字符串
    # conf: 配置类实例
    def parse(self, txt):
        # 样式检查
        res = self.__styleCheck(txt)

        # 插值检查
        # 包括插值、图、表分析、时间地点替换
        res = self.__specialCheck(res)

        # 特殊符号替换，主要是转义字符
        # 例如百分号%需要替换为\%
        # 下划线_替换为\_
        res = self.__symCheck(res)

        return res

