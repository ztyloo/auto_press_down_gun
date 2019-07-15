delta = 306

#  ['x0', 'y0', 'x1', 'y1']
screen_position = \
    {'fire_mode': [1496, 1128, 1942, 1153],
     'small_fire_mode': [1600, 1317, 1660, 1343],
     'in_tab': [1053, 138, 1087, 155],
     'in_scope': [1669, 1179, 1766, 1208],
     'weapon1name': [2245, 135, 2400, 160],
     'weapon1muzzle': [2191, 330, 2256, 395],
     'weapon1grip': [2327, 330, 2392, 395],
     'weapon1magazine': [2474, 330, 2539, 395],
     'weapon1scope': [2554, 152, 2619, 217],
     'weapon1butt': [2644, 193, 2709, 258],
     'weapon2name': [2245, 442, 2400, 467],
     'weapon2muzzle': [2191, 636, 2256, 701],
     'weapon2grip': [2327, 636, 2392, 701],
     'weapon2magazine': [2474, 636, 2539, 701],
     'weapon2scope': [2554, 459, 2619, 524],
     'weapon2butt': [2644, 499, 2709, 564],
     'helmet': [1319, 226, 1397, 304],
     'armor': [1319, 578, 1397, 656],
     'backpack': [1319, 489, 1397, 567],
     'ground0': [675, 206, 870, 226],
     'ground1': [675, 289, 870, 309],
     'ground2': [675, 372, 870, 392],
     'ground3': [675, 454, 870, 474],
     'ground4': [675, 537, 870, 557],
     'ground5': [675, 620, 870, 640],
     'ground6': [675, 702, 870, 722],
     'ground7': [675, 785, 870, 805],
     'ground8': [675, 868, 870, 888],
     'ground9': [675, 950, 870, 970],
     'ground10': [675, 1033, 870, 1053],
     'ground11': [675, 1116, 870, 1136],
     'ground12': [675, 1198, 870, 1218],
     }


screen_position_states = \
    {'fire_mode': ['single', 'burst', 'full'],
     'small_fire_mode': ['single', 'burst', 'full'],
     'in_tab': ['in'],
     'in_scope': ['in'],
     'weapon1name': ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', 'pp19', 'g36c'],
     'weapon1muzzle': ['flash', 'suppressor', 'compensator'],
     'weapon1grip': ['thumb', 'lightweight', 'half', 'angled', 'vertical'],
     'weapon1magazine': [],
     'weapon1scope': ['1r', '1h', '2', '3', '4', '6', '8', '15'],
     'weapon1butt': ['m416_butt'],
     'weapon2name': ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', 'pp19', 'g36c'],
     'weapon2muzzle': ['flash', 'suppressor', 'compensator'],
     'weapon2grip': ['thumb', 'lightweight', 'half', 'angled', 'vertical'],
     'weapon2magazine': [],
     'weapon2scope': ['1r', '1h', '2', '3', '4', '6', '8', '15'],
     'weapon2butt': ['m416_butt'],
     'helmet': [],
     'armor': [],
     'backpack': [],
     'ground0': [],
     'ground1': [],
     'ground2': [],
     'ground3': [],
     'ground4': [],
     'ground5': [],
     'ground6': [],
     'ground7': [],
     'ground8': [],
     'ground9': [],
     'ground10': [],
     'ground11': [],
     'ground12': []
     }


def crop_screen(screen, pos):
    x0, y0, x1, y1 = pos
    return screen[y0:y1, x0:x1, :]
