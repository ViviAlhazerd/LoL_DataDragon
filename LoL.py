from riotwatcher import  LolWatcher, ApiError
lol_watcher = LolWatcher('RGAPI-992b1c5b-d385-4ff6-9ea6-d81dbba0ad04')
my_region = 'jp1'#サーバーによってかわります 日本鯖はjp1
# me = lol_watcher.summoner.by_name(my_region, "Vivi Alhazerd")

# First we get the latest version of the game from data dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

# versionsの中身
# {'n': {'item': '11.4.1', 'rune': '7.23.1', 'mastery': '7.23.1', 'summoner': '11.4.1', 
# 'champion': '11.4.1', 'profileicon': '11.4.1', # 'map': '11.4.1', 'language': '11.4.1',
# 'sticker': '11.4.1'}, 
# 'v': '11.4.1', 
# 'l': 'ja_JP', 
# 'cdn': 'https://ddragon.leagueoflegends.com/cdn', 
# 'dd': '11.4.1', 
# 'lg': '11.4.1', 
# 'css': '11.4.1', 
# 'profileiconmax': 28, 
# 'store': None}

# Lets get some champions
current_champ_list = lol_watcher.data_dragon.champions(champions_version)

# Lets get some champions static information
static_champ_list = lol_watcher.data_dragon.champions(champions_version, True, 'ja_JP')

# championFull.jsonのstatsとspellsを各チャンピオン別に格納
champ_det = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_det[row['name']] = {"stats"   : row["stats"],
                              "passive" : row['passive'],
                              "spells"  : row['spells'] }
# print(champ_det["アフェリオス"])

print(champ_det['ガリオ']["spells"][1])

# チャンピオンのネームリスト
champ_list = {}
i = 1
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_list[i] = row['name']
    i += 1
# print(champ_list)
