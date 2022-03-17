from openpyxl import Workbook, load_workbook

wb = load_workbook("1programmering textspel.xlsx")
ws = wb.active
print(ws)
current_room = 2
start = True
wsRooms= wb["Rooms"]
def active_room():
    print(ws[F"B{current_room}"].value)


while start:
    reading = input("")
    if reading == "active room":
        active_room()
        

