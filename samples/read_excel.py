import os
import xlrd

current_path = os.path.dirname(__file__)
data_excel_path = os.path.join(current_path,'data/testdata.xls')

workbook = xlrd.open_workbook(data_excel_path)
sheet = workbook.sheet_by_index(0)
#处理merged
merged = sheet.merged_cells
print(merged)

def get_merged_cell_valle(row_index,col_index):
    cell_value = None
    for (rolw, rhigh, clow, chigh) in merged:
        if row_index >= rolw and row_index<rhigh:
            if col_index>=clow and col_index<chigh:
                cell_value = sheet.cell_value(rolw,clow)
                break
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

