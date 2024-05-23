import PyPDF2

# pip install PyPDF2 pycryptodome
# 把加密的pdf用密码解开后,复制每一页生成一个新的pdf文件

pdf1 = open('secret.pdf', 'rb')
pdf1Reader = PyPDF2.PdfReader(pdf1)
# 这里填入加密pdf文件的密码
pdf1Reader.decrypt('123456')
print("总页数:", len(pdf1Reader.pages))
pdfWriter = PyPDF2.PdfWriter()

for page_num in range(len(pdf1Reader.pages)):
    # 复制每一页
    print(page_num)
    page_obj = pdf1Reader.pages[page_num]
    pdfWriter.add_page(page_obj)

pdfOutputFile = open('new.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1.close()