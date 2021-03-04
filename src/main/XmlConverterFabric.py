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
    def __init__(self, *args, **kwargs):
        self.config = {
            "xml": None,
            "excel": None,
            "excel_filename": None,
            "_2d_array": None,  # [["parent_node", "child_node", "child_child_node"]]
            "caps": None,   # ["Чтение из файла", "Вывод"]
        }

    # set input and output path

    def set_config(self, config):
        self.config = config
        self.check_config(self)
        self.check_xml_dir(self)
        self.check_excel_dir(self)
        self.check_excel_filename(self)
        self.check_fields(self)
        self.check_caps(self)


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
    def check_fields(self):
        if not self.config["fields"]:
            raise Exception("Set fields")
        if not isinstance(self.config["fields"], list):
            raise Exception("Bad Fields")

    @staticmethod
    def check_caps(self):
        if not self.config["caps"]:
            raise Exception("Set caps")
        if not isinstance(self.config["fields"], list):
            raise Exception("Bad Fields")

    @staticmethod
    def check_config(self):
        empty_fields = [i[0] for i in self.config.items() if i[1] is None]
        if empty_fields:
            print("Error! There is an empty config fields :")
            for field in empty_fields:
                print(f"    {field}")
            raise Exception

    def run(self):
        self.check_config(self)
        if os.path.exists(self.config["xml"]) and os.path.isdir(os.path.dirname(self.config["excel"])):
            self.convert(self, self.config["xml"], os.path.join(self.config["excel"], self.config["excel_filename"]))

            print("Running the converter...")
        else:
            raise Exception("Bad xml dir or excel dir")

    @staticmethod
    def convert(self, *args, **kwargs):
        print("converted")


if __name__ == '__main__':
    fabric = XmlConverterFabric()
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\здания\\xml_здания_Выписки_ч3",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "Converted.xlsx",
        "caps": ["123"],
        "fields": ["123"],
    }
    fabric.set_config(config)
    fabric.run()
    print("Test ok")
