from docx import Document

doc = Document()
for i in range(10):
    doc.add_heading(f'제목 크기 비교 level {i} ', level=i)

doc.save("test1.docx")