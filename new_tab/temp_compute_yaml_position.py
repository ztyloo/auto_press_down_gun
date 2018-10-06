import time
import yaml

# with open('tab_position.yaml', 'r') as dumpfile:
#     position_dict = yaml.load(dumpfile)
#
# assert position_dict is not None
# time.sleep(1)
#
# len_list = [83, 83, 82]*5
#
#
# x0 = position_dict['ground_0']['x0']
# x1 = position_dict['ground_0']['x1']
# y0 = position_dict['ground_0']['y0']
# y1 = position_dict['ground_0']['y1']
# for i in range(1, 13):
#     temp_dict = dict()
#     temp_dict['x0'] = x0
#     temp_dict['x1'] = x1
#     dy = sum(len_list[0:i])
#     temp_dict['y0'] = y0+dy
#     temp_dict['y1'] = y1+dy
#     position_dict['ground_'+str(i)] = temp_dict
#
# with open('tab_position.yaml', 'w') as dumpfile:
#     dumpfile.write(yaml.dump(position_dict))


with open('tab_position.yaml', 'r') as dumpfile:
    position_dict = yaml.load(dumpfile)

for k, v in position_dict.items():
    temp_dict = dict()
    temp_dict['x0'] = v['x0']
    temp_dict['x1'] = v['x1']
    temp_dict['y0'] = v['y0'] - 7
    temp_dict['y1'] = v['y1'] - 7
    position_dict[k] = temp_dict

with open('tab_position.yaml', 'w') as dumpfile:
    dumpfile.write(yaml.dump(position_dict))
