from docx import Document
from docx.shared import Cm

doc = Document()
t = doc.add_table(rows=2, cols=3)
t.style = doc.styles['Table Grid']

rows = t.rows
cells = rows[0].cells
cells[0].text = "a"
cells[1].text = "b"
cells[2].text = "c"
cells = rows[1].cells
cells[0].text = "d"
cells[1].text = "e"
cells[2].text = "f"
cells = t.add_row().cells
cells[1].iter_inner_content = ["g"]
t.add_column(Cm(2.0))

doc.save("test5.docx")