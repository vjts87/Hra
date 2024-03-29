import os
from PIL import Image
# player class -> class(display_stats(???))
class Player:
    def __init__(self, name, elo=1400, love=50, friends=2, reputation=20, mentalhealth=75):
        self.elo = elo
        self.love = love
        self.friends = friends
        self.reputation = reputation
        self.name = name
        self.mentalhealth = mentalhealth

    def display_stats(self):
        print(f"\nŠtatistiky:\nElo: {self.elo}\nLáska: {self.love}\nPriatelia: {self.friends}\nReputácia: {self.reputation}\nMentálne zdravie: {self.mentalhealth} \n")

class NPC:
    def __init__(self, name, elo, loveToPlayer, isFriend, isPet: bool = False):
        self.name = name
        self.elo = elo
        self.loveToPlayer = loveToPlayer
        self.isFriend = isFriend
        self.isPet = isPet

    def display_npc_stats(self):
        print(f"\nMeno: {self.name} \nElo: {self.elo} \nCity: {self.loveToPlayer} \nPriateľstvo: {self.isFriend} \nDomáce zviera: {self.isPet} \n")

class Inventory:
    def __init__(self, name, descriprion, quantity, eloRise, loveRise, friendRise, pic: str = ''):
        self.name = name
        self.description = descriprion
        self.quantity = quantity
        self.eloRise = eloRise
        self.loveRise = loveRise
        self.friendRise = friendRise
        self.pic = pic

    def show_image(self):
        if self.pic.strip() == '':
            print("Tento predmet nemá obrázok.")
            return
        workdir = os.path.dirname(__file__) + "//images"
        image = Image.open(os.path.join(workdir, self.pic))
        image.show()
    
    def display_inventory(self):
        print(f"\nInfo o predmete: \nNázov: {self.name} \nPopisok: {self.description} \nPočet: {self.quantity} \nPrírastok ela: {self.eloRise} \nPrírastok lásky: {self.loveRise} \nPrírastok priateľstva: {self.friendRise} \n")

class Position:
    def __init__(self) -> None:
        self.chrs = {
        'P': u'\u265F',
        'R': u'\u265C',
        'N': u'\u265E',
        'B': u'\u265D',
        'K': u'\u265A',
        'Q': u'\u265B',
        'p': u'\u2659',
        'r': u'\u2656',
        'n': u'\u2658',
        'b': u'\u2657',
        'k': u'\u2654',
        'q': u'\u2655'
        }
    
    def drawField(self, position, piece):

        if position == 0:
            print('|', end="")

        print(' ' + piece + ' |', end="")

    def drawFloor(self):
        print('+---' * 8, end="")
        print('+')

    def showChessBoard(self, FEN):

        rows = FEN.split('/')
        rows.reverse()

        self.drawFloor()
        position = 0
        for row in rows[::-1]:
            for pismeno in row:
                if ord(pismeno) in range(ord('0'), ord('9') + 1):
                    for _ in range(int(pismeno)):
                        self.drawField(position, " ")
                        position += 1
                else:
                    if pismeno in self.chrs.keys():
                        self.drawField(position, self.chrs[pismeno])
                        position += 1
                    else:
                        position += 1
                        continue

            position = 0
            print()
            self.drawFloor()


class ImageManager():
    def __init__(self, filename):
        self.filename = filename
        self.work_dir = os.path.dirname(__file__) + "//images"
        self.image = Image.open(os.path.join(self.work_dir, self.filename))
    
    def show(self):
        self.image.show()
