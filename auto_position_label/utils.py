

class Deep_vs_Wide_Dict:
    def __init__(self, stop_key_sign='x0', escape_c='-'):
        self.stop_key_sign = stop_key_sign
        self.escape_c = escape_c

        self.d_dict = dict()
        self.mid_dict = dict()
        self.w_dict = dict()

    def is_leaf(self, diction):
        if self.stop_key_sign in diction:
            return True
        return False

    def d_to_w(self):
        self.encode_dict(self.d_dict)
        return self.w_dict

    def encode_dict(self, dic, path_str=""):
        if self.is_leaf(dic):
            self.w_dict[path_str[1:]] = dic
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


class Cluster:
    def __init__(self, w_dict):
        self.similar_thr = 3

        self.wh_list = list()
        self.w_dict = w_dict
        for k, v in self.w_dict.items():
            self.wh_list.append([v['x1'] - v['x0'], v['y1'] - v['y0']])
        self.cluster_center_list = list()
        self.cluster_list = list()

        self.calculate_cluster()
        self.change_w_dict()

    def is_similar(self, wh_a, wh_b):
        aw, ah = wh_a
        bw, bh = wh_b
        if abs(aw-bw) < self.similar_thr and abs(ah-bh) < self.similar_thr:
            return True
        return False

    def calculate_center(self, wh_list):
        w_sum, h_sum = 0, 0
        for wh in wh_list:
            w_sum += wh[0]
            h_sum += wh[1]
        return w_sum/len(wh_list), h_sum/len(wh_list)

    def calculate_cluster(self):
        for wh in self.wh_list:
            wh_find_cluster = False
            for i, cluster_center in enumerate(self.cluster_center_list):
                if self.is_similar(wh, cluster_center):
                    self.cluster_list[i].append(wh)
                    self.cluster_center_list[i] = self.calculate_center(self.cluster_list[i])
                    wh_find_cluster = True
            if not wh_find_cluster:
                self.cluster_center_list.append(wh)
                self.cluster_list.append([wh])
        print('rect w,h cluster num: ', len(self.cluster_center_list))

    def change_w_dict(self):
        for k, v in self.w_dict.items():
            w, h = v['x1'] - v['x0'], v['y1'] - v['y0']
            for wh in self.cluster_center_list:
                if self.is_similar([w, h], wh):
                    self.w_dict[k]['x1'] = wh[0]
                    self.w_dict[k]['y1'] = wh[1]
                    break


if __name__ == '__main__':
    from auto_position_label.crop_position import screen_position

    dvw_dict = Deep_vs_Wide_Dict()
    dvw_dict.d_dict = screen_position
    dvw_dict.d_to_w()

    cluster = Cluster(dvw_dict.w_dict)
    print(cluster.w_dict)
