from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


text = "Hello\nThis is a multiline text\nHere we have to handle line height manually\nAnd check that every line uses not more than pagewidth"
c = canvas.Canvas("test1.pdf")
c.drawText(1 * cm, 29.7 * cm - 1 * cm, text)
id = c.create_text(1 * cm, 29.7 * cm - 1 * cm, text)

c.showPage()


'''
for i, line in enumerate(text.splitlines()):
    c.drawString(1 * cm, 29.7 * cm - 1 * cm - i * cm, line)
    print('I =', i, 'Line = ', line)
'''
c.save()