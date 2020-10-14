'''Task: Create a script that inserts your currently running process names in alphabetical order 
into a one page pdf file. Write also the process id after the names. 
If you have more processes than one page then skip the remaining processes from the pdf. 
Use libraries like wmi and reportlab.pdfgen. 
'''
from subprocess import Popen, PIPE
from re import split
from sys import stdout
def getProc():
    temp = []
    sub_proc = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
    #Discard the first line (ps aux header)
    sub_proc.stdout.readline()
    for line in sub_proc.stdout:
        print (line)
        #The separator for splitting is 'variable number of spaces'
        #temp = split(" *", line.strip())
        #temp = split(' ', str(line))
        #temp = line.strip(" ", 10)
        temp = split(" *", line.strip())
        print(temp)
        #temp.append(Proc(proc_info))
    return temp

temp = getProc()

