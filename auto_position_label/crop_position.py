delta = 306

screen_position = {
    'fire_mode': {'x0': 1496, 'x1': 1942, 'y0': 1128, 'y1': 1153},
    'in_tab': {'x0': 1053, 'x1': 1087, 'y0': 138, 'y1': 155},
    'in_scope': {'x0': 1669, 'x1': 1766, 'y0': 1179, 'y1': 1208},

    'weapon': {
        '0':
            {
                'name': {'x0': 2245, 'x1': 2400, 'y0': 135, 'y1': 160},
                'muzzle': {'x0': 2191, 'x1': 2256, 'y0': 330, 'y1': 395},
                'grip': {'x0': 2327, 'x1': 2392, 'y0': 330, 'y1': 395},
                'magazine': {'x0': 2474, 'x1': 2539, 'y0': 330, 'y1': 395},
                'scope': {'x0': 2554, 'x1': 2619, 'y0': 152, 'y1': 217},
                'butt': {'x0': 2644, 'x1': 2709, 'y0': 193, 'y1': 258},
            },
        '1':
            {
                'name': {'x0': 2245, 'x1': 2400, 'y0': 135 + 307, 'y1': 160 + 307},
                'muzzle': {'x0': 2191, 'x1': 2256, 'y0': 330 + delta, 'y1': 395 + delta},
                'grip': {'x0': 2327, 'x1': 2392, 'y0': 330 + delta, 'y1': 395 + delta},
                'magazine': {'x0': 2474, 'x1': 2539, 'y0': 330 + delta, 'y1': 395 + delta},
                'scope': {'x0': 2554, 'x1': 2619, 'y0': 152 + delta, 'y1': 217 + delta},
                'butt': {'x0': 2644, 'x1': 2709, 'y0': 193 + delta, 'y1': 258 + delta},
            }
    },

    'helmet': {'x0': 1319, 'x1': 1397, 'y0': 226, 'y1': 304},
    'armor': {'x0': 1319, 'x1': 1397, 'y0': 578, 'y1': 656},
    'backpack': {'x0': 1319, 'x1': 1397, 'y0': 489, 'y1': 567},

    'ground':
        {
            '0': {'x0': 675, 'x1': 870, 'y0': 206, 'y1': 226},
            '1': {'x0': 675, 'x1': 870, 'y0': 289, 'y1': 309},
            '2': {'x0': 675, 'x1': 870, 'y0': 372, 'y1': 392},
            '3': {'x0': 675, 'x1': 870, 'y0': 454, 'y1': 474},
            '4': {'x0': 675, 'x1': 870, 'y0': 537, 'y1': 557},
            '5': {'x0': 675, 'x1': 870, 'y0': 620, 'y1': 640},
            '6': {'x0': 675, 'x1': 870, 'y0': 702, 'y1': 722},
            '7': {'x0': 675, 'x1': 870, 'y0': 785, 'y1': 805},
            '8': {'x0': 675, 'x1': 870, 'y0': 868, 'y1': 888},
            '9': {'x0': 675, 'x1': 870, 'y0': 950, 'y1': 970},
            '10': {'x0': 675, 'x1': 870, 'y0': 1033, 'y1': 1053},
            '11': {'x0': 675, 'x1': 870, 'y0': 1116, 'y1': 1136},
            '12': {'x0': 675, 'x1': 870, 'y0': 1198, 'y1': 1218}
        }
}


def crop_screen(screen, pos):
    x0, x1, y0, y1 = pos['x0'], pos['x1'], pos['y0'], pos['y1']
    return screen[y0:y1, x0:x1, :]
