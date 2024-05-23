import os
from win32com import client as wc


def save_doc_to_docx(rawpath):
    """doc转docx"""
    word = wc.Dispatch("Word.Application")
    filenamelist = os.listdir(rawpath)
    for i in filenamelist:
        if i.endswith('.doc') and not i.startswith('~$'):
            doc = word.Documents.Open(rawpath + i)
            rename = os.path.splitext(i)
            doc.SaveAs(rawpath + rename[0] + '.docx', 12)
            doc.Close()
    word.Quit()


def save_docx_to_doc(rawpath):
    word = wc.Dispatch("Word.Application")
    """docx转doc"""
    filenamelist = os.listdir(rawpath)
    for i in filenamelist:
        if i.endswith('.docx') and not i.startswith('~$'):
            doc = word.Documents.Open(rawpath + i)
            rename = os.path.splitext(i)
            doc.SaveAs(rawpath + rename[0] + '.doc', 0)
            doc.Close()
    word.Quit()


if __name__ == '__main__':
    doc_path = 'E:\\doc\\'
    save_doc_to_docx(doc_path)
    docx_path = r'E:\\docx\\'
    save_docx_to_doc(docx_path)
