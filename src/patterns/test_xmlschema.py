import xmlschema
import os
import xml.etree.ElementTree as ElementTree
from pprint import pprint
import xmltodict


def check_file(file):
    xsd_main_file = "extract_base_params_construction_v01.xsd"
    xsd_folder = "D:\\PYTHON\\xml-to-excel\\src\\patterns\\xsd_files\\"
    xsd_main = os.path.join(xsd_folder, xsd_main_file)
    schema = xmlschema.XMLSchema(xsd_main, base_url=xsd_folder)

    etree = ElementTree.parse(file)
    print(f"xmlschema: {schema.is_valid(file)} ;  etree: {schema.is_valid(etree)}  in file: {os.path.split(file)[1]}")


def main():
    xml_dir = "D:\\PYTHON\\xml-to-excel\\xml\\"
    xml_files = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if os.path.isfile(os.path.join(xml_dir, f))]
    for f in xml_files:
        check_file(f)


def watch():
    file = "D:\\PYTHON\\xml-to-excel\\xml\\1_report1 (404).xml"
    xsd_main_file = "extract_base_params_construction_v01.xsd"
    xsd_folder = "D:\\PYTHON\\xml-to-excel\\src\\patterns\\xsd_files\\"
    xsd_main = os.path.join(xsd_folder, xsd_main_file)
    schema = xmlschema.XMLSchema(xsd_main, base_url=xsd_folder)

    etree = ElementTree.parse(file)
    print(f"xmlschema: {schema.is_valid(file)} ;  etree: {schema.is_valid(etree)}  in file: {os.path.split(file)[1]}")

    wdict = schema.to_dict(etree)
    print(wdict)


if __name__ == '__main__':
    main()



