#импорт рандома для рандомизации вариантов
import random

#проверка языка
print('Выбор языка / Language selection(eng, rus, or exit): ')
language = input().lower()


#функция для рандомизации выбора героя с плейстайлом на русском
def random_hero_rus(heroes, playstyles, damagedeal):
    strenght = ('Ogre Magi, Alchemist, Axe, Bristleback, Centaur Warrunner, Chaos Knight, Dawnbreaker, Doom, '
                'Dragon Knight, Earth Spirit, Earthshaker, Elder Titan, Huskar, Kunkka, Legion Commander, '
                'Lifestealer, Mars, Night Stalker, Omniknight, Primal Beast, Pudge, Slardar, Spirit Breaker, Sven, '
                'Tidehunter, Tiny, Treant, Protector, Tusk, Underlord, Undying, Wraith King.')
    dexterity = ('Anti-Mage, Arc Warden, Bloodseeker, Bounty Hunter, Clinkz, Drow Ranger, Ember Spirit, Faceless '
                 'Void, Gyrocopter, Hoodwink, Juggernaut, Luna, Medusa, Meepo, Monkey King, Morphling, Naga, Siren, '
                 'Phantom Assassin, Phantom Lancer, Razor, Riki, Shadow Fiend, Slark, Sniper, Spectre, '
                 'Templar Assassin, Terrorblade, Troll Warlord, Ursa, Viper, Weaver.')
    intelligence = ('Ancient Apparition, Crystal Maiden, Death Prophet, Disruptor, Enchantress, Grimstroke, Invoker, '
                    'Jakiro, Keeper of the Light, Leshrac, Lich, Lina, Lion, Muerta, Nature’s Prophet, Necrophos, '
                    'Oracle, Outworld Devourer, Puck, Pugna, Queen of Pain, Rubick, Shadow Demon, Shadow Shaman, '
                    'Silencer, Skywrath, Mage, Storm Spirit, Tinker, Warlock, Witch Doctor, Zeus.')
    universal = ('Abaddon, Bane, Batrider, Chen, Beastmaster, Brewmaster, Broodmother, Clockwerk, Dark Seer, '
                 'Dark Willow, Dazzle, Enigma, Io, Lone Druid, Lycan, Magnus, Marci, Mirana, Nyx Assassin, Pangolier, '
                 'Phoenix, Sand King, Snapfire, Techies, Timbersaw, Vengeful Spirit, Venomancer, Visage, Void Spirit, '
                 'Windranger, Winter Wyvern.')

    heroes_rand = random.randrange(len(heroes))
    playstyle_rand = random.randrange(len(playstyles))
    damagerand = random.randrange(len(damagedeal))
    hero = heroes[heroes_rand]

    if hero in strenght:
        print(f'Герой: {heroes[heroes_rand]} (силовик) \n'
              f'Стиль игры: {playstyles[playstyle_rand]} \n'
              f'Тип урона: {damagedeal[damagerand]}')
    elif hero in dexterity:
        print(f'Герой: {heroes[heroes_rand]} (ловкач) \n'
              f'Стиль игры: {playstyles[playstyle_rand]} \n'
              f'Тип урона: {damagedeal[damagerand]}')
    elif hero in intelligence:
        print(f'Герой: {heroes[heroes_rand]} (Умныый) \n'
              f'Стиль игры: {playstyles[playstyle_rand]} \n'
              f'Тип урона: {damagedeal[damagerand]}')
    elif hero in universal:
        print(f'Герой: {heroes[heroes_rand]} (универсал) \n'
              f'Стиль игры: {playstyles[playstyle_rand]} \n'
              f'Тип урона: {damagedeal[damagerand]}')


#на английском
def random_hero_eng(heroes, playstyles, damagedeal):
    strenght = ('Ogre Magi, Alchemist, Axe, Bristleback, Centaur Warrunner, Chaos Knight, Dawnbreaker, Doom, '
                'Dragon Knight, Earth Spirit, Earthshaker, Elder Titan, Huskar, Kunkka, Legion Commander, '
                'Lifestealer, Mars, Night Stalker, Omniknight, Primal Beast, Pudge, Slardar, Spirit Breaker, Sven, '
                'Tidehunter, Tiny, Treant, Protector, Tusk, Underlord, Undying, Wraith King.')
    dexterity = ('Anti-Mage, Arc Warden, Bloodseeker, Bounty Hunter, Clinkz, Drow Ranger, Ember Spirit, Faceless '
                 'Void, Gyrocopter, Hoodwink, Juggernaut, Luna, Medusa, Meepo, Monkey King, Morphling, Naga, Siren, '
                 'Phantom Assassin, Phantom Lancer, Razor, Riki, Shadow Fiend, Slark, Sniper, Spectre, '
                 'Templar Assassin, Terrorblade, Troll Warlord, Ursa, Viper, Weaver.')
    intelligence = ('Ancient Apparition, Crystal Maiden, Death Prophet, Disruptor, Enchantress, Grimstroke, Invoker, '
                    'Jakiro, Keeper of the Light, Leshrac, Lich, Lina, Lion, Muerta, Nature’s Prophet, Necrophos, '
                    'Oracle, Outworld Devourer, Puck, Pugna, Queen of Pain, Rubick, Shadow Demon, Shadow Shaman, '
                    'Silencer, Skywrath, Mage, Storm Spirit, Tinker, Warlock, Witch Doctor, Zeus.')
    universal = ('Abaddon, Bane, Batrider, Chen, Beastmaster, Brewmaster, Broodmother, Clockwerk, Dark Seer, '
                 'Dark Willow, Dazzle, Enigma, Io, Lone Druid, Lycan, Magnus, Marci, Mirana, Nyx Assassin, Pangolier, '
                 'Phoenix, Sand King, Snapfire, Techies, Timbersaw, Vengeful Spirit, Venomancer, Visage, Void Spirit, '
                 'Windranger, Winter Wyvern.')

    heroes_rand = random.randrange(len(heroes))
    playstyle_rand = random.randrange(len(playstyles))
    damagerand = random.randrange(len(damagedeal))

    hero = heroes[heroes_rand]

    if hero in strenght:
        print(f'Hero: {heroes[heroes_rand]} (strenght) \n'
              f'Playstyle: {playstyles[playstyle_rand]} \n'
              f'Type of damage: {damagedeal[damagerand]}')
    elif hero in dexterity:
        print(f'Hero: {heroes[heroes_rand]} (dexterity) \n'
              f'Playstyle: {playstyles[playstyle_rand]} \n'
              f'Type of damage: {damagedeal[damagerand]}')
    elif hero in intelligence:
        print(f'Hero: {heroes[heroes_rand]} (intelligence) \n'
              f'Playstyle: {playstyles[playstyle_rand]} \n'
              f'Type of damage: {damagedeal[damagerand]}')
    elif hero in universal:
        print(f'Hero: {heroes[heroes_rand]} (universal) \n'
              f'Playstyle: {playstyles[playstyle_rand]} \n'
              f'Type of damage: {damagedeal[damagerand]}')


#герои
heroes_of_dota = (
    'Ogre Magi, Alchemist, Axe, Bristleback, Centaur Warrunner, Chaos Knight, Dawnbreaker, Doom, Dragon Knight, '
    'Earth Spirit, Earthshaker, Elder Titan, Huskar, Kunkka, Legion Commander, Lifestealer, Mars, '
    'Night Stalker, Omniknight, Primal Beast, Pudge, Slardar, Spirit Breaker, Sven, Tidehunter, Tiny, Treant, '
    'Protector, Tusk, Underlord, Undying, Wraith King, Anti-Mage, Arc Warden, Bloodseeker, Bounty Hunter, '
    'Clinkz, Drow Ranger, Ember Spirit, Faceless Void, Gyrocopter, Hoodwink, Juggernaut, Luna, Medusa, Meepo, '
    'Monkey King, Morphling, Naga, Siren, Phantom Assassin, Phantom Lancer, Razor, Riki, Shadow Fiend, Slark, '
    'Sniper, Spectre, Templar Assassin, Terrorblade, Troll Warlord, Ursa, Viper, Weaver, Ancient Apparition, '
    'Crystal Maiden, Death Prophet, Disruptor, Enchantress, Grimstroke, Invoker, Jakiro, Keeper of the Light, '
    'Leshrac, Lich, Lina, Lion, Muerta, Nature’s Prophet, Necrophos, Oracle, Outworld Devourer, Puck, Pugna, '
    'Queen of Pain, Rubick, Shadow Demon, Shadow Shaman, Silencer, Skywrath, Mage, Storm Spirit, Tinker, '
    'Warlock, Witch Doctor, Zeus, Abaddon, Bane, Batrider, Chen, Beastmaster, Brewmaster, Broodmother, '
    'Clockwerk, Dark Seer, Dark Willow, Dazzle, Enigma, Io, Lone Druid, Lycan, Magnus, Marci, Mirana, '
    'Nyx Assassin, Pangolier, Phoenix, Sand King, Snapfire, Techies, Timbersaw, Vengeful Spirit, Venomancer, '
    'Visage, Void Spirit, Windranger, Winter Wyvern.').split(', ')

#плейстайлы на английском
play_style_eng = ('Agressive, Heal, TERPILA (MADE STACKS), Suck Mid lane (Oblizivatel), Forest, Otbitiy ebanat '
                  'dohnushiy pod vishkoy(DEAD ALWAYS), afk radik(radiance) v(in) lesu(forest), leave...(or afk before '
                  'leave), steal farm from 3/1 pos').split(', ')

damage_eng = ('Hybrid, Magical, Phys').split(', ')

#плейстайлы на русском
play_style_rus = ('Агрессивно, Хил, ТЕРПИЛА (ДЕЛАЙ СТАКИ), Облизыватель мидлейна(подсос мидера), Лесок, Конченый '
                  'дебил умирающий под вражеской вышкой, афк в лесу после радика(первой шмоткой), лив...(либо афк до '
                  'лива), кража фарма у 3/1 pos').split(', ')

damage_rus = ('Гибрид, Физический, Магический').split(', ')

#проверка языка с циклом, пока не будет выбран правильный вариант ответа или не будет выключена программа
while language != 'eng' or language != 'rus':
    if language == 'rus':
        break
    elif language == 'eng':
        break
    elif language == 'exit':
        exit('Пока хуила! / Goodbye m8!')
    else:
        print('Ошибка. Повторите снова. / Error. Try again.')
        language = input().lower()

#выбор героя на русском с возомжностью реролла
if language == 'rus':
    random_hero_rus(heroes_of_dota, play_style_rus, damage_rus)
    print('Повторить? (y/n)')
    while True:
        answer = input().lower()
        if answer == 'y':
            random_hero_rus(heroes_of_dota, play_style_rus, damage_rus)
            print('Повторить? (y/n)')
            continue
        elif answer == 'n':
            exit('Пока!!! Удачной игры!')
        else:
            print('Неверный ответ! Попробуй еще раз!')
            continue

#выбор героя на английском с возомжностью реролла
elif language == 'eng':
    random_hero_eng(heroes_of_dota, play_style_eng, damage_eng)
    print('Try again? (y/n)')
    while True:
        answer = input().lower()
        if answer == 'y':
            random_hero_eng(heroes_of_dota, play_style_eng, damage_eng)
            print('Try again? (y/n)')
            continue
        elif answer == 'n':
            exit('Goodbye! GL HF!')
        else:
            print('Wrong answer! Try again!')
            continue
