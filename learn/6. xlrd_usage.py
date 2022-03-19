# xlrd 
# openpyxl에서 오류가 나와서 변경 

import xlrd 

wb=xlrd.open_workbook("sample.xlsx")
ws=wb.sheet_by_index(0)

print(wb.sheet_names())

# xlrd도 OLE 정보 때문에 읽기에 실패한다. 
# 완전하고 쉬운 방법이 없어 보이므로 csv를 기본 형식으로 간다. 

# Excel OLE DB Provider를 사용하면 부드럽게 변환할 수 있다. 
# 제품 개발자의 지원을 받으면 쉽고 확실하다. 

