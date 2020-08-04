if cc == "Nick#4611":
            unique_fish = []
            v = open("C:/Users/Bgenest96/Desktop/discord-bot/Libraries/" + 'fishing_inventory_nick.txt', 'r+')
            fishing_inventory_nick = [line for line in v.readlines()]
            fishing_inventory_nick1 = []
            print(fishing_inventory_nick)
            for i in fishing_inventory_nick:
                fishing_inventory_nick1.append(i.strip())
            set_list = sorted(set(fishing_inventory_nick1))
            for i in set_list:
                unique_fish.append(fishing_inventory_nick1.count(i))
            print(unique_fish)
            print(set_list)
            await message.channel.send(f"Nick's inventory:")
            fishing_dict = {}
            for i in unique_fish:
                fishing_dict = dict(zip(set_list, unique_fish))
            table = PrettyTable()
            table.field_names = ["Fish", "Qty", "Rarity"]
            for x, y in fishing_dict.items():
                if x in fish_common.keys():
                    r = "common"
                    table.add_row([x.title(), y, r.title()])
            for x, y in fishing_dict.items():
                if x in fish_uncommon.keys():
                    r = "uncommon"
                    table.add_row([x.title(), y, r.title()])
            for x, y in fishing_dict.items():
                if x in fish_rare.keys():
                    r = "rare"
                    table.add_row([x.title(), y, r.title()])
            for x, y in fishing_dict.items():
                if x in fish_rare2.keys():
                    r = "very rare"
                    table.add_row([x.title(), y, r.title()])
            await message.channel.send(table)