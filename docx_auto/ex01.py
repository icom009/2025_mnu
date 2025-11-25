from docx import Document

#새롭게 파일을 만들때
#doc = Document()

#파일을 불러올때에
doc = Document("test1.docx")

doc.save("test2.docx")

