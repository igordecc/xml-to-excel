import os, sys
import xmltodict
import pandas
import datetime


class XmlConverterFabric:
    def __init__(self, *args, **kwargs):
        self.xml_dir = None
        self.excel_dir = None
        self._2d_array = None   # [["parent_node", "child_node", "child_child_node"]]
        self.caps = None    # ["Чтение из файла", "Вывод"]


    def set_xml_dir(self, xml: str):
        if os.path.exists(xml):
            self.xml_dir = xml
        else:
            raise Exception("Xml Path does not exists")

    def set_excel_dir(self, excel: str):
        if os.path.exists(excel):
            if os.path.isdir(excel):
                self.excel_dir = os.path.join(excel, "Converted.xlsx")
            elif os.path.isfile(excel):
                self.excel_dir = excel
            else:
                raise Exception("Bad excel dir name")
        else:
            raise Exception("Excel Path does not exists")

    def set_excel_filename(self, filename: str):
        self.excel_dir = os.path.join(os.path.dirname(self.excel_dir), filename)

    def set_fields(self, _2d_array: list):
        self._2d_array = _2d_array

    def set_caps(self, caps: list):
        self.caps = caps

    def run(self):

        if os.path.exists(self.xml_dir) and os.path.isdir(os.path.dirname(self.excel_dir)):
            self.convert(self.xml_dir, self.excel_dir)
            empty_fields = [i[0] for i in self.__dict__.items() if i[1] is None]
            if empty_fields:
                print("Error! There is an empty config fields :")
                for field in empty_fields:
                    print(f"    {field}")
                raise Exception
            print("Running the converter...")
        else:
            raise Exception("Bad xml dir or excel dir")

    @staticmethod
    def convert(*args, **kwargs):
        print("converted")


if __name__ == '__main__':
    fabric = XmlConverterFabric()
    fabric.set_xml_dir("D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\здания\\xml_здания_Выписки_ч3")
    fabric.set_excel_dir("D:\\PYTHON\\xml-to-excel\\Вывод.xlsx")
    fabric.set_excel_filename("Converted.xlsx")
    fabric.set_caps([])
    fabric.set_fields([])
    fabric.run()
