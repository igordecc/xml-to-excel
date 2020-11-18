import os, sys
import pandas
import xml.etree.ElementTree as ET


def iter_docs(author):
    author_attr = author.attrib
    for doc in author.iter('document'):
        doc_dict = author_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict


def main(*args, **kwargs):
    file_path = args[0]
    folder_path = args[1]
    print(file_path)
    print(folder_path)
    etree = ET.parse(file_path)
    root = etree.getroot()
    print(f" {root.tag}")
    print(f" {root.attrib}")

    # todo выбрать файлы (много)
    xml_dict = {}
    for i in root.iter():
        xml_dict. # todo pack all xml into dict - gg ez
        print(f"  {i.tag}  attrib: {i.text}")

    # root = etree.getroot()
    # doc_df = pandas.DataFrame(list(iter_docs(root)))
    

if __name__ == '__main__':
    file = "D:\\PYTHON\\xml-to-excel\\1_report1.xml"
    main(file, "D:\\")
