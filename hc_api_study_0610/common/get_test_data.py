import json
import os
import xlrd

# 定义一个函数用来获取excel表中的测试用例数据
def get_test_case(sheetname):
    #定义一个空列表
    testcaselist = []
    #获取excel测试用例表路劲
    testcase_path = os.path.join(os.path.dirname(__file__),"..","excel_testcase_data","接口测试用例.xlsx")
    #打开excel文档读取测试数据
    workbook = xlrd.open_workbook(testcase_path)
    #通过sheet页名称来获取sheet页数据
    worksheet = workbook.sheet_by_name(sheetname)
    #获取表格中sheet页有效的数据（行）
    maxrows = worksheet.nrows
    for row in range(1,maxrows):
        #获取请求参数
        reqinfo = worksheet.cell(row,8).value
        # print(reqinfo)
        #获取返回结果并以字典的形式输出，用来断言
        resinfo = worksheet.cell(row,10).value
        # print(resinfo)
        #获取测试用例编号
        test_num = worksheet.cell(row,0).value
        #获取测试用例标题
        testcase_title = worksheet.cell(row,2).value
        #把获取到的测试放到列表中
        testcaselist.append([reqinfo,resinfo,test_num,testcase_title])
        #返回
    return testcaselist


if __name__ == '__main__':
    print(get_test_case("主题首页")[1])
