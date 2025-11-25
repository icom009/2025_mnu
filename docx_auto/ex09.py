from docx import Document
from docx.oxml.ns import qn

doc = Document()
style = doc.styles['Normal']
rPr = style.element.rPr()
rFonts = rPr.get_or_add_rFonts()
font_name = '나눔 고딕'
rFonts.set(qn('w:eastAsia'), font_name)
doc.add_paragraph("Save Text")

doc.save("test9.docx")