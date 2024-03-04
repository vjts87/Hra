##### Majster Levíc #####
import dialogues

from classes import Player, NPC, Inventory, Position
from dialogueManager import dialogueManager

##### Príbeh #####

def story_scenario(player):
    #####intro_intro#####
    if True:
        print("*Vitaj! Už čoskoro sa vydáš na dobrodružstvo, najskôr však potrebujem vedieť, tvoje meno.*")
        player.name = input("*Ako sa voláš?* \n> ")
        print(f"\n*Ahoj, {player.name}! Už viem všetko potrebné. Môžme začať...*")
        print("*Štatistiky si vieš kedykoľvek pozrieť cez príkaz #stats#*. \n*Štatistiky NPC si vieš kedykoľvek pozrieť cez príkaz #npcstats + meno a priezvysko NPC#*. \n*Predmety v inventári si vieš kedykoľvek pozrieť cez príkaz #inventory + názov predmetu#*")
        choice = input("*Pre spustenie hry stlač 1.* \n> ")

    #####intro_Matej_Kristal#####
    if True:
        if choice == "1":
            print("\n*1 nová správa od používateľa Matej Krištál*")
        else:
            print("\n*Nesprávna voľba. Skús znovu.*")
            choice = input("*Pre spustenie hry stlač 1.* \n> ")
            if choice == "1":
                print("\n*1 nová správa od používateľa Matej Krištál*")
        choice = dMan.handleChoices(dialogues.OtvoritSpravu)
        if choice == "1":
            print(f"\n< Ahoj {player.name}, \ndlho sme sa nevideli, ako máš? Stále si sa nevrátil k šachu? Našiel som jeden zaujímavý diagram, posielam Ti ho v prílohe. Na Tvojom mieste by som sa naň pozrel. \n")
        MatejKrištál.display_npc_stats()
        print('*niektoré akcie ti zlepšia štatistiky, ktoré neskôr môžu odomknúť nové pokračovania príbehu*')
        choice = dMan.handleChoices(dialogues.PrvyDiagram)
        if choice == "1":
            position.showChessBoard('6kr/5ppp/8/8/8/8/5PPP/R5K1')
            move = input("*Napíš najlepší ťah.*\n> ")
            # Check if the move is correct (case-insensitive)
            if move.lower() in ['va8', 'va8#']:
                print("\n*Správne! Získavaš 10 ELO bodov.*")
                player.elo += 10
            else:
                print("\n*Nesprávny ťah. Strácaš 10 ELO bodov.*")
                player.elo -= 10
        elif choice == "2":
            print("\n> Ahoj, \nprepáč momentálne nemám náladu na šach. \n*Strácaš 25 ELO bodov.* \n")
            player.elo -= 25
        player.display_stats()

    #####MTNK#####
    if True:
        print("*1 nová správa od používateľa Matej Krištál*")
        choice = dMan.handleChoices(dialogues.OtvoritSpravu)
        if choice == "1":
            print(f"\n< Ahoj {player.name}, \nneviem, či si zachytil, ale budúci týždeň sa hrajú online majstrovstvá Trenčianskeho kraja. Posielam Ti propozície pre prípad, že by si sa chcel zúčastniť.")
        choice = input("1. zúčastniť sa turnaja \n> ")
        if choice == "1":
            print("\n*Rozhodol si sa hrať. Na turnaji sa ti celkom darí vzhľadom na to, že si tak dlho nehral. Pred posledným kolom máš 4 body. Ak chceš postúpiť na MSR, musíš vyhrať.*\n")
        print("*Tvojím posledným súperom je Maroš Bazalka. Hráš s čiernymi: \n1. d4 d5 2. Sf4 Jc6 3. e3 Sf5 4. Jf3 e6 5. Jc3 Sd6 6. Sxd6 Dxd6 7. Sd3 Sg6 8. Je5 Jxe5 9. dxe5 Dxe5 10. Sxg6 hxg6 11. Je2 O-O-O 12. Vb1 Kb8 13. g3 Jf6 14. O-O Jg4 15. f4 Dxe3+ 16. Kg2* \n*Môžeš vyhrať. Čo zahráš?*")
        position.showChessBoard('1k1r3r/ppp2pp1/4p1p1/3p4/5Pn1/4q1P1/PPP1N1KP/1R1Q1R2')
        move = input("> ")
        # Check if the move is correct (case-insensitive)
        if move.lower() in ['vxh2', 'vxh2#', 'vh2', 'vh2#']:
            print("\n*Správne! Získavaš 10 ELO bodov a 90 bodov reputácie.*")
            print("*Postúpil si do celoslovenského kola.* \n")
            player.reputation += 90
            player.elo += 20
            pozvankaNaOnlineMSR.quantity += 1
        else:
            print("\n*Nesprávny ťah. Strácaš 10 ELO bodov.*")
            player.elo -= 10
        player.display_stats()
        pozvankaNaOnlineMSR.display_inventory()

    #####intro_Maros_Bazalka#####
    if True:
        print("\n*1 nová správa od používateľa Maroš Bazalka*")
        choice = dMan.handleChoices(dialogues.OtvoritSpravu)
        if choice == "1":
            print(f"\n< Dobrá hra {player.name}... Mal si šťastie... Čo povieš na odvetu? Samozrejme ak sa nebojíš.")
        choice = dMan.handleChoices(dialogues.VyzvaNaPartiu)
        if choice == "1":
            print("\n> Kto by sa ťa bál? Bez problémov ťa opäť rozbijem.")
            position.showChessBoard('r4rk1/5p2/pp1qnp2/3NN2p/3P4/3Q3P/PPP3P1/5RK1')
            print("BNŤ.")
            move = input("> ")
            # Check if the move is correct (case-insensitive)
            if move.lower() in ['jf6', 'jxf6', 'jxf6+', 'jf6+']:
                print("\n*Správne! Získavaš 10 ELO bodov a 10 bodov reputácie.*")
                player.reputation += 10
                player.elo += 20
                player.friends += 1
                print("\n< Dobrá hra... predsa len v tebe niečo bude.")
                MarosBazalka.isFriend = True
            else:
                print("\n*Nesprávny ťah. Strácaš 10 ELO bodov, 5 bodov mentálneho zdravia a 10 bodov reputácie.*")
                player.elo -= 10
                player.reputation -= 10
                player.mentalhealth -= 5
                print("\n< Kto by sa ma bál? Naozaj? Očividne by si sa mal TY! XDD \n< Choď sa prebaliť, potrénovať a potom možno - ak sa raz na kolenách doplazíš naspäť - ti dám 2. šancu.")
        elif choice == "2":
            print("\n> Prepáč, teraz sa mi nedá. Možno inokedy.")
            player.reputation -= 15
            print("\n< Myslel som si, že si zbabelý... no nie až takto. Ak raz vytiahneš hlavu z piesku napíš, aby som ťa mohol rozbiť. \n*Strácaš 15 bodov reputácie.*")
        player.display_stats()
        MarosBazalka.display_npc_stats()
    
    #####online_MSR#####
    if True: 
        if pozvankaNaOnlineMSR.quantity == 1:
            print("\n*Blížia sa online MSR. Chceš sa zúčastniť?*")
            choice = dMan.handleChoices(dialogues.VstupDoTurnaja)
            if choice == "1":
                print("*\nNa MSR sa ti až tak nedarí. V 3. kole máš však šancu nádherne vyhrať. Podarí sa ti nájsť rozhodujúcu taktiku?*")
                pozvankaNaOnlineMSR.quantity == 0
                position.showChessBoard('6k1/5p1p/2q3p1/6Q1/2pb4/1Ppr1PP1/r6P/2B2R1K')
                print("ČNŤ")
                move = input("> ")
                # Check if the move is correct (case-insensitive)
                if move.lower() in ['df3', 'dxf3', 'df3+', 'dxf3+']:
                    print("\n*Správne! Získavaš 10 ELO bodov a 10 bodov reputácie.*")
                    print("\n*Si so svojím výsledkom na turnaji spokojný. Získavaš 5 bodov mentálneho zdravia.*")
                    player.reputation += 10
                    player.elo += 20
                    player.mentalhealth += 5
                else:
                    print("\n*Nesprávny ťah. Strácaš 10 ELO bodov a 10 bodov reputácie.*")
                    player.elo -= 10
                    player.reputation -= 10
            elif choice == "2":
                print("\n*Klamal si, aby si nemusel hrať. Prichádzaš o 10 bodov reputácie*")
                player.reputation -= 10
        player.display_stats()

    #####intro_Bubo_Kielik#####(!)
    if True:
        print("*1 nová správa od používateľa Bubo Kielik*")
        choice = dMan.handleChoices(dialogues.OtvoritSpravu)
        if choice == '1':
            print(f"\n< Ahoj {player.name}, \nVšimol som si, že si na majstrovstvách podal chválitebný výkon. Mohol by z Teba byť celkom slušný šachista... samozrejme, keby trochu potrénuješ. Ak by si sa chcel šachu aktívnejšie venovať, príď sa ukázať na tréning. V prílohe Ti posielam detaily.")
            choice = dMan.handleChoices(dialogues.Odpisat)
            if choice == '1':
                print("\n> Ahoj, \nďakujem za pozvanie, určite sa zastavím.")
                print("\n< To rád počujem. Mal by si čas na 1 rýchlu partiu? Nech sa uistím, že sa mi o Tvojich výkonoch nesnívalo. ;)")
                choice == dMan.handleChoices(dialogues.VyzvaNaPartiu)
                if choice == '1':
                    print("\n> Samozrejme, aj tak nemám nič lepšie na práci.")
                    print("\n< Ako povieš... vyber si stranu.")
                    print("\n*Niektoré partie sa rozhodnú podľa pravdepodobnosti na výhru. Tú si môžeš zvýšiť získavaním ela.*")
                    player.friends += 1
                    BuboKielik.isFriend = True
                    choice = input("\n1. Biele (výhra = 1%) \n2. Čierne (výhra = 1%) \n> ")
                    if choice == '1':
                        print("\n> Skúsim biele. \n< OK. Veľa šťastia.")
                        import random
                        random_number = random.randint(1, 100)
                        if random_number == 1:
                            print("\n*Ako zázrakom sa ti podarilo vyhrať* \n< Wow! Takže sa mi naozaj nesnívalo, hráš veľmi dobre. Pravda, za túto prehru si môžem sám, ale aj tak si ma prekvapil. Niekedy v klube dáme odvetu.")
                            print("\n*Získavaš 100 ELO, 50 bodov reputácie a ") #predmet
                            player.elo += 100
                            player.reputation += 50
                            # pridať predmet
                        else:
                            print("\n*Prehral si.* \n< Takže sa mi naozaj nesnívalo, hráš veľmi dobre. Niekedy v klube dáme odvetu.")
                    elif choice == '2':
                        print("\n> Skúsim čierne. \n< OK. Veľa šťastia.")
                        import random
                        random_number = random.randint(1, 100)
                        if random_number == 1:
                            print("\n*Ako zázrakom sa ti podarilo vyhrať* \n< Wow! Takže sa mi naozaj nesnívalo, hráš veľmi dobre. Pravda, za túto prehru si môžem sám, ale aj tak si ma prekvapil. Niekedy v klube dáme odvetu.")
                            print("\n*Získavaš 100 ELO, 50 bodov reputácie a ") #predmet
                            player.elo += 100
                            player.reputation += 50
                            # pridať predmet
                        else:
                            print("\n*Prehral si.* \n< Takže sa mi naozaj nesnívalo, hráš veľmi dobre. Niekedy v klube dáme odvetu.")
                elif choice == '2':
                    print("\n> Prepáč, momentálne sa mi nedá. Možno inokedy.")
                    print("\n< OK. Nevadí, vidíme sa v klube.")
        player.display_stats()
        BuboKielik.display_npc_stats()

    #####vstup_do_klubu#####
    print("*vstupuješ do klubu*")
    print(f"*Bubo Kielik:* \n< Ahoj {player.name}, som rád, že si sa ukázal. Dnes budeš trénovať so mnou. Dám ti pár taktík a potom si môžeš zahrať s ostatnými. Myslím, že s Viki sa poznáš. Nebolo by však na škodu, keby sa zoznámiš aj s ostatnými. \n< Myslím, že môžme začať.")
    position.showChessBoard('8/8/2k2P2/8/8/8/8/7K')
    choice = input("\n< Dnes sa pozrieme na pešiakové koncovky. Dokáže v tejto pozícii čierny na ťahu chytiť pešiaka? \n1. áno \n2. nie")
    if choice == '1':
        print("> Myslím, že áno, mal by ho dobehnúť.")
        print("< Správne.")
    elif choice == '2':
        print("> Nie, ten pešiak je moc ďaleko.")
        print("< Nemáš pravdu. Pešiak je síce ďaleko, no čierny kráľ ho dokáže chytiť.")
    position.showChessBoard('8/8/2k2P2/8/8/8/8/7K')
    choice = input("< ")

    #####intro_viktoria_bubonova#####
        

    #####idk#####


# Main game loop
player = Player(name="")
pozvankaNaOnlineMSR = Inventory('Pozvánka na online MSR', 0, 0, 0, 0)
items = {
    'pozvanka na online msr': pozvankaNaOnlineMSR,
}
MatejKrištál = NPC('Matej Krištál', 1400, 0, True)
MarosBazalka = NPC('Maroš Bazalka', 1500, 0, False)
BuboKielik = NPC('Bubo Kielik', 2200, 0, False)
RukoLyljak = NPC('Ruko Lyljak', 0, 0, True) 
ViktoriaBubonova = NPC('Viktória Buboňová', 1500, 10, False)
NPCS = {
    'matej kristal': MatejKrištál,
    'maros bazalka': MarosBazalka,
    'bubo kielik': BuboKielik,
    'ruko lyljak': RukoLyljak,
    'viktoria bubonova': ViktoriaBubonova,
}
position = Position() 
dMan = dialogueManager(player, NPCS, items)

story_scenario(player)

