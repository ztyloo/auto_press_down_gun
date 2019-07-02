

all_guns = ['98k', 'akm', 'aug', 'awm', 'dp28', 'groza', 'm16', 'm24', 'm249', 'm416', 'm762', 'mini14', 'mk14',
                 'mk47', 'qbu', 'qbz', 's12k', 's1987', 's686', 'scar', 'sks', 'slr', 'tommy', 'ump9', 'uzi', 'vector',
                 'vss', 'win94']

single_guns = ['98k', 'awm', 'm16', 'm24', 'mini14', 's12k', 's1987', 's686', 'sks', 'slr', 'win94']
full_guns = ['dp28', 'm249']
single_burst_guns = ['m16', ]
single_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss']
single_burst_full_guns = ['m762', 'ump45', 'vector']

can_full_guns = ['akm', 'aug', 'groza', 'm416', 'qbz', 'scar', 'mk14', 'tommy', 'uzi', 'vss', 'm762', 'ump45', 'vector', 'dp28', 'm249', ]


def gun_next_mode(gun_name, now_mode):
    if gun_name in single_burst_guns:
        if now_mode == 'single':
            return 'burst'
        if now_mode == 'burst':
            return 'single'

    if gun_name in single_full_guns:
        if now_mode == 'single':
            return 'full'
        if now_mode == 'full':
            return 'single'

    if gun_name in single_burst_full_guns:
        if now_mode == 'single':
            return 'burst'
        if now_mode == 'burst':
            return 'full'
        if now_mode == 'full':
            return 'single'




