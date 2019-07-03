

class Deep_vs_Wide_Dict:
    def __init__(self, stop_key_sign=list, escape_c='-'):
        self.stop_key_sign = stop_key_sign
        self.escape_c = escape_c

        self.d_dict = dict()
        self.mid_dict = dict()
        self.w_dict = dict()

    def is_leaf(self, v):
        if isinstance(v, self.stop_key_sign):
            return True
        return False

    def d_to_w(self):
        self.encode_dict(self.d_dict)
        return self.w_dict

    def encode_dict(self, dic, path_str=""):
        if self.is_leaf(dic):
            self.w_dict[path_str[len(self.escape_c):]] = dic
            return
        for k in dic:
            self.encode_dict(dic[k], path_str + self.escape_c + k)

    def w_to_d(self):
        for k, v in self.w_dict.items():
            path_sep = k.split(self.escape_c)
            temp_dict = self.mid_dict
            for path in path_sep:
                if not path in temp_dict:
                    temp_dict[path] = dict()
                temp_dict = temp_dict[path]
            temp_dict[path_sep[-1]] = v

    def key_w2d(self, key_w):
        key_d_list = key_w.split(self.escape_c)
        return key_d_list


if __name__ == '__main__':
    from auto_position_label.crop_position import screen_position_states

    dvw_dict = Deep_vs_Wide_Dict(escape_c='-')
    dvw_dict.d_dict = screen_position_states
    dvw_dict.d_to_w()
    dvw_dict.w_to_d()
    print(dvw_dict.w_dict)

    # cluster = Cluster(dvw_dict.w_dict)
    # print(cluster.w_dict)
