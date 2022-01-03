import cv2
import math
import numpy
from decimal import Decimal

from PIL import Image

from util import config_util
from util.deeplab import DeepLabModel

distance_threshold = Decimal(config_util.properties.get('distance_threshold'))
area_threshold = float(config_util.properties.properties.get('area_threshold'))


def get_focus_and_length(ellipse):
    edge = sorted(ellipse[1])
    c = math.sqrt((edge[1] / 2) ** 2 - (edge[0] / 2) ** 2)
    theta = ellipse[2]
    if theta > 180:
        theta = theta - 180

    if theta <= 90:
        theta_radian1 = math.radians(360 - theta)
        theta_radian2 = math.radians(180 - theta)
    else:
        theta_radian1 = math.radians(180 - theta)
        theta_radian2 = math.radians(360 - theta)

    x1 = ellipse[0][0] + math.cos(theta_radian1) * c
    y1 = ellipse[0][1] + math.sin(theta_radian1) * c
    x2 = ellipse[0][0] + math.cos(theta_radian2) * c
    y2 = ellipse[0][1] + math.sin(theta_radian2) * c

    return (x1, y1), (x2, y2), edge[1] / 2


def get_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    distance_decimal = Decimal(distance)
    return distance_decimal


def judge(contour, ellipse):
    focus1, focus2, a = get_focus_and_length(ellipse)
    correct_distance = Decimal(a * 2)
    sum_distance_error = Decimal(0)
    point_num = contour.size // 2
    contour = contour.reshape((point_num, 2))

    for point in contour:
        distance = get_distance(focus1, point) + get_distance(focus2, point)
        sum_distance_error += Decimal(math.fabs(distance - correct_distance))

    avg_distance_error = sum_distance_error / point_num
    if avg_distance_error > distance_threshold:
        return False, avg_distance_error
    else:
        return True, avg_distance_error


def change_pixel_color(image):
    return numpy.where(image > 38, 0, image)


def get_set_iou(s1, s2):
    intersection = len(s1 & s2)
    union = len(s1 | s2)
    print('intersection ' + str(intersection))
    print('union ' + str(union))
    iou = intersection / union
    if iou > area_threshold:
        return True, iou
    else:
        return False, iou


def get_result(image):
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype(numpy.uint8)
    ret, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    segment_list = numpy.argwhere(binary == 255).tolist()
    segment_set = set(tuple(x) for x in segment_list)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    ellipse = cv2.fitEllipse(contours[0])

    img_ellipse = cv2.ellipse(binary, ellipse, 127, cv2.FILLED)
    fit_list = numpy.argwhere(img_ellipse == 127).tolist()
    fit_set = set(tuple(x) for x in fit_list)

    judge_by_distance, distance_error = judge(contours[0], ellipse)
    judge_by_area, iou = get_set_iou(segment_set, fit_set)

    result = judge_by_area and judge_by_distance
    return int(result), (distance_error, iou)


if __name__ == '__main__':
    pretrained_weights = 'H:\\毕业设计\\results\\model2\\frozen_inference_graph.pb'
    MODEL = DeepLabModel(pretrained_weights)  # 加载模型

    img_name = '../images/000038_image.png'
    result_path = '../images/deeplab_result.jpg'
    cv_image = cv2.imread(img_name)
    img = Image.open(img_name)
    resized_im, seg_map = MODEL.run(img)  # 获取结果
    seg_map = seg_map.astype(numpy.uint8)
    result = get_result(seg_map)
    print(result)
    cv2.imwrite(result_path, seg_map)
    # seg_image = Image.fromarray(seg_map)
    # seg_image.save('../images/output.jpg')  # 保存mask结果图像