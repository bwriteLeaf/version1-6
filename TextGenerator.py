# -*- coding:utf-8 -*-
'''
    主程序：生成LaTeX文档
'''
import os
import sys
import pdb

from interpreter import Interpreter
from configuration import Config

# 计数器类
# 负责记录章节号等
class Counter():
    def __init__(self):
        self.__chapterCount = 0

    def generateChapterId(self):
        self.__chapterCount += 1
        return 

    def getChapterCount(self):
        self.generateChapterId()
        return self.__chapterCount

# 章节计数
# 弃用，使用Counter类代替
def chapterCountWrapper():
    count = 0
    def chapterCount():
        nonlocal count
        count += 1
        return str(count)
    return chapterCount

# 输出LaTeX文档导言区内容
def printPreInfo(doc, year='2017', program='国家免费孕前优生项目', city='xx市', date='\\today'):
    # 重定向输出到文档
    sys.stdout = doc

    print('%!TEX encoding = UTF-8 Unicode')
    print('%!TEX program = xelatex')
    print('\documentclass[UTF8,doctor,pdf]{ustcthesis}', file=doc)
    print('\\usepackage{xeCJK}')
    print('\\setCJKmainfont{FangSong}')
    print('\graphicspath{{figures/}}')
    print('\\title{%s年度}\n\\program{%s}\n\\city{%s数据分析报告}'%(year, program, city), file=doc)
    print('\\date{%s}\n\\author{国家孕前优生数据中心}'%date, file=doc)

    # 恢复标准输出
    sys.stdout = sys.__stdout__
    config.year = year
    return

# 插入图
# doc: 输出文档
# figureName: 图名称
# caption: 图标题
def insertFigure(doc, figureName, caption, label):
    # 重定向标准输出到文档
    sys.stdout = doc

    print('\\begin{figure}[htbp]')
    print('\centering')
    print('\includegraphics[width=1\\textwidth]{%s}'%figureName)
    print('\caption{%s}'%caption)
    print('\label{%s}'%label)
    print('\end{figure}')


    sys.stdout = sys.__stdout__
    return 

# 生成标题和目录
def makeTitleandContents(doc):
    print('\n\\maketitle', file=doc)
    print('\n\\frontmatter', file=doc)
    print('\\tableofcontents', file=doc)
    return 

# 生成前言
# doc: 输出文档
# parser: 文档翻译器
def makePreface(doc, parser):
    # 生成前言的LaTeX文档
    # templateFile: 作为输入的模板文件
    def makePrefaceTex(templateFile):
        # 生成前言LaTeX文档
        prefaceFile = open('preface.tex', 'w', encoding='utf-8')
        sys.stdout = prefaceFile
        for line in templateFile:
            res = parser.parse(line)
            print(res)

        sys.stdout = sys.__stdout__
        return 

    # 保存当前工作目录
    cwd = os.getcwd()
    if not os.path.exists('chapters'):
        # 章节目录不存在
        os.mkdir('chapters')
    
    # 切换至章节目录
    os.chdir('chapters')

    # 生成前言的LaTeX文档
    tmpFile = open(os.path.join(config.tmpFilePath, 'preface.txt'), 'r', encoding='utf-8')
    makePrefaceTex(tmpFile)
    tmpFile.close()

    # 输出前言文档引入控制序列
    print('\\input{chapters/preface}\t%前言', file=doc)

    os.chdir(cwd)
    return 


# 生成一章正文
# counter: 计数器
# parser: 文档翻译器
# templateFile: 待翻译的模板文件
def makeChapter(doc, counter, parser, templateFile):
    # 生成正文章节的LaTeX文档
    def makeChapterTex(chapterId, templateFile):
        # 新建文档文件
        chapterFile = open('%s.tex'%chapterId, 'w', encoding='utf-8')
        sys.stdout = chapterFile
        for line in templateFile:
            print(parser.parse(line))

        sys.stdout = sys.__stdout__
        chapterFile.close()
        return 

    # 保存当前工作目录
    cwd = os.getcwd()
    if not os.path.exists('chapters'):
        # 章节目录不存在
        os.mkdir('chapters')
    
    # 切换至章节目录
    os.chdir('chapters')
    
    # 生成当前章节号
    chapterId = 'chapter'+str(counter.getChapterCount())

    # 输出章节引入控制序列
    print('\\input{chapters/%s}\t' % (chapterId), file=doc)
    print('------------------生成%s...'%(chapterId))
    # 生成新章节的LaTeX文档
    makeChapterTex(chapterId, templateFile)
    print('------------------%s生成结束'%(chapterId))

    os.chdir(cwd)
    return 


# 生成文章正文
# counter: 计数器
# parser: 文档解释器
def makeMainBody(doc, counter, parser):
    print('\n\mainmatter', file=doc)

    # 生成各章内容
    for x in range(1, config.chapters+1):
        tmpFile = open(os.path.join(config.tmpFilePath, 'chapter%d.txt'%x), 'r', encoding='utf-8')
        makeChapter(doc, counter, parser, tmpFile)
        tmpFile.close()

    return

# 生成文档主体内容
# doc: 输出文档
# counter: 计数器实例
# parser: 文档翻译器
def makeBody(doc, counter, parser):
    # 文档开始标记
    print('\n\\begin{document}', file=doc)
    
    # 生成标题和目录
    makeTitleandContents(doc)
    # 生成前言
    # makePreface(doc, parser)

    # 生成正文部分
    makeMainBody(doc, counter, parser)

    # 文档结束标记
    print('\n\\end{document}', file=doc)

    return 


# 生成文档主函数
# counter: 计数器
# parser: 文档分析器
def generateLaTeXFile(counter, parser):
    # 保存当前工作目录
    cwd = os.getcwd()
    # 切换工作目录至模板文件所在目录
    os.chdir('LaTexFiles')
    # 新建文档文件
    doc = open("%d.tex"%config.code, 'w', encoding='utf-8')

    # pdb.set_trace()
    # 生成导言区
    printPreInfo(doc, year=config.year, city=config.city, date=config.date)
    # 生成主体
    makeBody(doc, counter, parser)
    doc.close()
    print('生成成功')
    os.chdir(cwd)

    return 


# 生成章节计数器
counter = Counter()
config = Config()
parser = Interpreter(config)
generateLaTeXFile(counter, parser)
print(config.city)


