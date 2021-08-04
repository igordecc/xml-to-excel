import xmlschema
import os
import xml.etree.ElementTree as ElementTree
from pprint import pprint
import xmltodict


def check_file_with_schema(file,
                           xsd_main_file,
                           xsd_folder
                           ):
    xsd_main = os.path.join(xsd_folder, xsd_main_file)
    schema = xmlschema.XMLSchema(xsd_main, base_url=xsd_folder)
    etree = ElementTree.parse(file)
    print(f"xmlschema: {schema.is_valid(file)} ;  etree: {schema.is_valid(etree)} ; in file: {os.path.split(file)[1]}")
    return schema, etree


def check_files(xmls_to_check,
                xsd_main_file,
                xsd_folder
                ):
    xml_files = [os.path.join(xmls_to_check, f) for f in os.listdir(xmls_to_check) if os.path.isfile(os.path.join(xmls_to_check, f))]
    for xml_file in xml_files:
        check_file_with_schema(xml_file,
                               xsd_main_file=xsd_main_file,
                               xsd_folder=xsd_folder
                               )


def watch_etree(
        file,
        xsd_main_file,
        xsd_folder,
        ):
    schema, etree = check_file_with_schema(file, xsd_main_file, xsd_folder)
    wdict = schema.to_dict(etree)
    print(wdict)

# ======== EXAMPLES
def check_сооружения():
    check_files(xmls_to_check="D:\\PYTHON\\xml-to-excel\\xml_сооружения\\",
                xsd_main_file="extract_base_params_construction_v01.xsd",
                xsd_folder="D:\\PYTHON\\xml-to-excel\\xsd_сооружения\\xsd_files\\"
                )

def check_здания():
    check_files(xmls_to_check="D:\\PYTHON\\xml-to-excel\\xml_здания\\",
                xsd_main_file="extract_base_params_build_v01.xsd",
                xsd_folder="D:\\PYTHON\\xml-to-excel\\xsd_здания\\xsd_files\\"
                )



if __name__ == '__main__':
    pass
    check_files(xmls_to_check="D:\\PYTHON\\xml-to-excel\\xml_сооружения_29.12.2020\\",
                xsd_main_file="extract_base_params_construction_v01.xsd",
                xsd_folder="D:\\PYTHON\\xml-to-excel\\xsd_сооружения\\xsd_files\\"
                )
    # check_здания()



