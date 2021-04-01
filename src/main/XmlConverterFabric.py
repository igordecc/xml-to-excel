import os, sys
import xmltodict
import pandas
import datetime

"""
xml -> excel
Main idea is to set all fields, that need to be read
and the way we will read them fields, before-hand;
then execute most common fields
then word directly with complicated one
then return result
"""


class XmlConverterFabric:
    def __init__(self, _config: dict, row_class: type(type), *args, **kwargs):
        if not _config:
            raise Exception("No config specified!")
        self.RowClass = row_class
        self.config = _config
        self.check_config(self)
        self.check_xml_dir(self)
        self.check_excel_dir(self)
        self.check_excel_filename(self)
        # self.check_excel_fields(self)
        self.check_caps(self)
        if self.config["caps"]:
            self.COL_MAX_NUM = len(self.config["caps"])
        else:
            self.COL_MAX_NUM = 0
        self.ex_range = range(1, self.COL_MAX_NUM + 1)

    # set input and output path


    @staticmethod
    def check_xml_dir(self):
        if not os.path.exists(self.config["xml"]):
            raise Exception("Xml Path does not exists")

    @staticmethod
    def check_excel_dir(self):
        if not os.path.isdir(self.config["excel"]):
            raise Exception("Bad excel dir name")

    @staticmethod
    def check_excel_filename(self):
        if not os.path.splitext(self.config["excel_filename"])[1] == ".xlsx":
            raise Exception("Wrong excel file extension")

    @staticmethod
    def check_caps(self):
        if not self.config["caps"]:
            raise Exception("Set caps")

    @staticmethod
    def check_config(self):
        empty_fields = [i[0] for i in self.config.items() if i[1] is None]
        if empty_fields:
            print("Error! There is an empty config fields :")
            for field in empty_fields:
                print(f"    {field}")
            raise Exception

    def run(self):
        """
        Converts all xml file files in self.confg["xml"] directory into one self.confg["excel"] file,
        where 1 row is one xml file
        """
        # extracting any xml file in dir to parse
        file_list = [os.path.join(self.config["xml"], file) for file in os.listdir(self.config["xml"]) if ".xml" == os.path.splitext(file)[-1]]

        # creating list of Excel_row objects
        list_of_rows = [[i for i in range(1, self.COL_MAX_NUM + 1)]]
        for i in [self.RowClass(file, col_max=self.COL_MAX_NUM)() for file in file_list]:
            list_of_rows.append(i)

        df = pandas.DataFrame(list_of_rows, columns = self.config["caps"])

        writer = pandas.ExcelWriter(os.path.join(self.config["excel"], self.config["excel_filename"]))
        df.to_excel(writer, index=False)
        if self.config.get("excel_format"):
            writer = self.config["excel_format"](writer)
        writer.save()
        print("Сохранено!")


if __name__ == '__main__':
    def excel_format(writer):
        sheet_setting = writer.sheets["Sheet1"]
        wrap_format = writer.book.add_format({'text_wrap': True})
        wid = 20
        sheet_setting.set_column(0, 7, width=wid, cell_format=wrap_format)
        sheet_setting.set_column(8, 8, width=wid * 3, cell_format=wrap_format)
        sheet_setting.set_column(9, 10, width=wid * 3, cell_format=wrap_format)
        sheet_setting.set_column(11, 12, width=wid * 6, cell_format=wrap_format)
        sheet_setting.set_column(13, 14, width=wid, cell_format=wrap_format)
        sheet_setting.set_column(15, 15, width=wid * 6, cell_format=wrap_format)
        sheet_setting.set_column(16, 17, width=wid * 3, cell_format=wrap_format)
        sheet_setting.set_column(18, 19, width=wid * 12, cell_format=wrap_format)
        return writer
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\здания\\xml_здания_Выписки_ч3",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "Converted.xlsx",
        "caps": ["123"],
        "xml_values": {},
        "xml_values_script": [],
        "excel_fields_script": [],
        "excel_format": excel_format,
    }
    fabric = XmlConverterFabric(config)
    fabric.run()
    print("Test ok")
