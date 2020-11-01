import os
import xlrd



class ExcelUtils():
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet() #

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count



    def get_marged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info


    def get_merged_cell_valle02(self,row_index, col_index):
        cell_value = None
        for (rolw, rhigh, clow, chigh) in self.get_marged_info():
            if row_index >= rolw and row_index < rhigh:
                if col_index >= clow and col_index < chigh:
                    cell_value = self.sheet.cell_value(rolw, clow)
                    break
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)
            else:
                cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path,'../samples/data/testdata.xlsx')
    excelUtils = ExcelUtils(excel_path,'Sheet1')
    excelUtils.get_merged_cell_valle02(3,0)