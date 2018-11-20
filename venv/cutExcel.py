'''from win32com.client import Dispatch, DispatchEx
import win32com.client,win32process'''
import openpyxl
import xlrd
import pythoncom
from PIL import ImageGrab, Image
import uuid


# screen_area——类似格式"A1:J10"
def excel_catch_screen(filename, sheetname, screen_area, img_name=False):
    wx = xlrd.open_workbook(filename);
    print(wx);
    return
    """ 对excel的表格区域进行截图——用例：excel_catch_screen(ur"D:\Desktop\123.xlsx", "Sheet1", "A1:J10")"""
    pythoncom.CoInitialize()  # excel多线程相关
    print(1);
    excel = win32com.client.DispatchEx("Excel.Application")  # 启动excel
    print(2);
    excel.Visible = True  # 可视化
    print(3);
    excel.DisplayAlerts = False  # 是否显示警告
    print(4);
    wb = excel.Workbooks.Open(filename)  # 打开excel
    print(5);
    ws = wb.Sheets(sheetname)  # 选择sheet
    print(6);
    ws.Range(screen_area).CopyPicture()  # 复制图片区域
    print(7);
    ws.Paste()  # 粘贴 ws.Paste(ws.Range('B1'))  # 将图片移动到具体位置
    print("wb:" + wb);
    name = str(uuid.uuid4())  # 重命名唯一值
    new_shape_name = name[:6]
    excel.Selection.ShapeRange.Name = new_shape_name  # 将刚刚选择的Shape重命名，避免与已有图片混淆
    print("name:"+name);
    ws.Shapes(new_shape_name).Copy()  # 选择图片
    img = ImageGrab.grabclipboard()  # 获取剪贴板的图片数据
    if not img_name:
        img_name = name + ".PNG"
    print(img_name);
    img.save(img_name)  # 保存图片
    wb.Close(SaveChanges=0)  # 关闭工作薄，不保存
    excel.Quit()  # 退出excel
    pythoncom.CoUninitialize()


if __name__ == '__main__':
    excel_catch_screen("D:\\NewFolder\\city_sales_data.xls","city","A1:J53")