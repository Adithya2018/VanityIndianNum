import re
import openpyxl as opxl
from vanity_indian_no import VanityIndianNo


if __name__ == '__main__':
    
    vanity_check_wb = opxl.load_workbook("Data/vanity check.xlsx")
    vanity_check_sheet_names = vanity_check_wb.sheetnames

    vanity_check_ws = vanity_check_wb[vanity_check_sheet_names[0]]
    
    for i in range(2, 26):
        cell_obj = vanity_check_ws.cell(row = i, column = 1)
        vn = VanityIndianNo(str(cell_obj.value))
        if vn.is_valid_no(vn.phone_no):
            vn.pattern_check(vn.phone_no)
