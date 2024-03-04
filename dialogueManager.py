class dialogueManager:
    def __init__(self, player, npcList, items):
        self.player = player
        self.npcList = npcList
        self.items = items

    def handleChoices(self, dialogue):
        for i in range(len(dialogue)):
            print(f'{i+1}. {dialogue[str(i+1)]}')
        choice = input('> ').lower()
        while choice not in dialogue.keys():
            #if dialogue[choice]:
                #break
            if choice == 'stats':
                self.player.display_stats()
                choice = input('\n> ')
            elif 'inventory' in choice:
                choice = choice.split('inventory')[-1].strip()
                if choice in self.items.keys():
                    itemInfo = self.items[choice]
                    itemInfo.display_inventory()
                    choice = input('\n> ')
            elif 'npcstats' in choice:
                choice = choice.split('npcstats')[-1].strip()
                if choice in self.npcList.keys():
                    npcInfo = self.npcList[choice]
                    npcInfo.display_npc_stats()
                    choice = input('\n> ')
            else:
                choice = input('\n*Nesprávna voľba. Skús znovu.* \n> ')
        return choice
    
