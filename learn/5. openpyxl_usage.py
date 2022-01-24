# openpyxl 
# https://pythondocs.net/openpyxl/openpyxl-%EC%82%AC%EC%9A%A9%EB%B2%95-%EA%B8%B0%EC%B4%88/
import openpyxl 
import os 
import sys

print(sys.path[0])
filename = sys.path[0] + "\\sample.xlsx"
#file = open(

wb = openpyxl.load_workbook(filename=filename, read_only=True, data_only=True)
# BadZipFile error. 2.6.3으로 변경해도 발생 

#기존 엑셀 파일 불러오기
ws = wb.active
# 현재 활성화 되어 있는 시트를 가리킴 
ws = wb['Sheet4']
