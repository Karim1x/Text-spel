#importerar för att läsa in workbook och den kommer från pyxl.
from openpyxl import load_workbook

#varablar
wb = load_workbook("Programmering textspel.xlsx")
ws = wb.active
start= True

#skriver man help så kommer alla commandon man kan använda.
def help():
    print("look,north,south,west,stop,active room")

#en loop som läser in en input, ifall man skriver skriver help så hjälper den dig, ifall man skríver stop så anvlutas loopen
while start:
    reading = input("")
    if reading == "help":
        help()
    if reading == "stop":
        start=False






