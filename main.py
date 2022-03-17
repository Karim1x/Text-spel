from openpyxl import load_workbook
from openpyxl.utils import *

wb = load_workbook("textspel.xlsx")
ws = wb.active
room_number = 2
room_number_change_n = -1
room_number_change_s = 1
room_position_change = 1
#Den visar hur mycket spelaren rör sig
position = {1:'A', 2:'B', 3:'C'}
room_position = 3
start = True
wsRooms = wb["Rooms"]
wsMap = wb["map"]




def look():
    print(ws[F"{position[room_position]}{room_number}"].value)
    #Printar ut


def north():
    global room_number
    if room_number >= 1:
        room_number += room_number_change_n
        print(ws[F"{position[room_position]}{room_number}"].value)

def south():
    global room_number
    if room_number >= 1:
        room_number += room_number_change_s
        print(ws[F"{position[room_position]}{room_number}"].value)


def west():
    global room_position
    if room_position >= 1:
        room_position -= room_position_change
        print(ws[F"{position[room_position]}{room_number}"].value)
        #Gör exakt samma sak som East def fast den subtraherar istället för addera

def east():
    global room_position
    if room_position >= 1:
        room_position += room_position_change
        print(ws[F"{position[room_position]}{room_number}"].value)
        #Jag har gjort bokstäverna till siffror.
        #Det gör att jag kan addera eller subtrahera ett tal för att förflytta spelaren.




while start:
    reading = input("")
    if reading == "look":
        look()
    if reading == 'north':
        north()
    if reading == "south":
        south()
    if reading == "west":
        west()
    elif reading == "stop":
        start = False
    if reading == 'quit':
        start = False




