import psutil
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

processes = {}
#Let's start the loop and iterate over the generator:

for process in psutil.process_iter():
    processes[process.pid] = process.name()

sortedproc = sorted(processes.items(), key=lambda x: x[1])   

for key, value in sortedproc:
    print(value,":",key)

c = canvas.Canvas("test.pdf")
i = 0

'''
This create single A4 size and print the txt from the dic iteration. 
'''
for key, value in sortedproc:
    txt = str(value) + ": " + str(key)
    c.drawString(1 * cm, 29.7 * cm - 1 * cm - i * cm, txt)
    print('I =', i, 'Line = ', txt)
    i= i+1
c.save()  
 
