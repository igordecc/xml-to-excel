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
    etree = ET.parse(file_path)
    root = etree.getroot()
    # doc_df = pandas.DataFrame(list(iter_docs(root)))
    

if __name__ == '__main__':
    file = "D:\\PYTHON\\xml_to_excel\\Помещения.xml"
    main(file)
