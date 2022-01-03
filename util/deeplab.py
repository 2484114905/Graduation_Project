import os
import tarfile

import cv2
import tensorflow.compat.v1 as tf
from PIL import Image
import numpy as np


class DeepLabModel(object):
    """class to load deeplab model and run inference"""

    INPUT_TENSOR_NAME = 'ImageTensor:0'
    OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
    INPUT_SIZE = 513
    FROZEN_GRAPH_NAME = 'frozen_inference_graph'

    def __init__(self, pretrained_weights):
        """Creates and loads pretrained deeplab model."""
        self.graph = tf.Graph()
        graph_def = None
        # Extract frozen graph from tar archive
        if pretrained_weights.endswith('.tar.gz'):
            tar_file = tarfile.open(pretrained_weights)
            for tar_info in tar_file.getmembers():
                if self.FROZEN_GRAPH_NAME in os.path.basename(tar_info.name):
                    file_handle = tar_file.extractfile(tar_info)
                    graph_def = tf.GraphDef.FromString(file_handle.read())
                    break
            tar_file.close()
        else:
            with tf.gfile.GFile(pretrained_weights, 'rb') as fd:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(fd.read())

        if graph_def is None:
            raise RuntimeError('Cannot find inference graph in tar archive.')

        with self.graph.as_default():
            tf.import_graph_def(graph_def, name='')

        gpu_options = tf.GPUOptions(allow_growth=True)
        config = tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False)
        self.sess = tf.Session(graph=self.graph, config=config)

    def run(self, image):
        """Runs inference on a single image.
        Args:
            image: A PIL.Image object, raw input image.
        Returns:
            resized_image:RGB image resized from original input image.
            seg_map:Segmentation map of 'resized_iamge'.
        """
        width, height = image.size
        resize_ratio = 1.0 * self.INPUT_SIZE / max(width, height)
        target_size = (int(resize_ratio * width), int(resize_ratio * height))
        resized_image = image.convert('RGB').resize(target_size, Image.ANTIALIAS)
        batch_seg_map = self.sess.run(
            self.OUTPUT_TENSOR_NAME,
            feed_dict={self.INPUT_TENSOR_NAME: [np.asarray(resized_image)]}
        )
        seg_map = batch_seg_map[0]
        seg_map[seg_map == 1] = 255  # 将人像的像素值置为255
        seg_map = seg_map.astype(np.uint8)

        return resized_image, seg_map


if __name__ == '__main__':
    pass
