
def detect_item(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]] // 255

    test_im = test_im * shield
    target_im = target_im * shield
    return np.sum(test_im - target_im)