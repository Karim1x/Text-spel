from openpyxl import load_workbook
from openpyxl.utils import *

wb = load_workbook("programmering texspel.xlsx")
ws = wb.active
#definierar save work sheeten
save_file = wb['Save']
room_number = 1
room_number_change_n = -1
room_number_change_s = 1
room_position = 'C'
start = True
wsRooms = wb["Rooms"]
wsMap = wb["map"]

#denna sparar min position i excel dokumentet.
wb.save("programmering texspel.xlsx")
room_number = (int(str(save_file["A2"].value)))

def look():
    print(ws[F"{room_position}{room_number}"].value)


def north():
    global room_number
    if room_number >= 1:
        room_number += room_number_change_n
        print(ws[F"{room_position}{room_number}"].value)

def south():
    global room_number
    if room_number >= 1:
        room_number += room_number_change_s
        print(ws[F"{room_position}{room_number}"].value)

def west():
    global room_position
    if room_position == 1:
        room_position -= 1
        print(ws[F"{room_position}{room_number}"].value)



while start:
    reading = input("")
    if reading == "look":
        look()
    if reading == 'north':
        north()
    if reading == "south":
        south()
    elif reading == "stop":
        start = False
    if reading == 'quit':
        start = False
   #Denna läser in columen där min senaste position har sparats och sätter in mig i det rum numret som sparats i columen.
    if reading == "save":
        save_file["A2"]=room_number
        wb.save("programmering texspel.xlsx")

