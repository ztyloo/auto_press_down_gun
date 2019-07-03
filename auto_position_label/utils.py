

class Cluster:
    def __init__(self, c_dict):
        self.similar_thr = 3

        self.wh_list = list()
        self.c_dict = c_dict
        for k, v in self.c_dict.items():
            self.wh_list.append([v['x1'] - v['x0'], v['y1'] - v['y0']])
        self.cluster_center_list = list()
        self.cluster_list = list()

        self.calculate_cluster()
        self.change_c_dict()

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

    def change_c_dict(self):
        for k, v in self.c_dict.items():
            w, h = v['x1'] - v['x0'], v['y1'] - v['y0']
            for wh in self.cluster_center_list:
                if self.is_similar([w, h], wh):
                    self.c_dict[k]['x1'] = int(self.c_dict[k]['x0'] + wh[0])
                    self.c_dict[k]['y1'] = int(self.c_dict[k]['y0'] + wh[1])
                    break


if __name__ == '__main__':
    pass

    # cluster = Cluster(dvw_dict.w_dict)
    # print(cluster.w_dict)
