from depth_from_video_in_the_wild.model import Model
from util import loadJson, parseArgs
from PIL import Image
import numpy as np
import tensorflow.compat.v1 as tf
import sys

session_config = tf.ConfigProto(device_count = {'GPU': 0})

def main(config):
    rgb_image = Image.open(config["video"])
    rgb_image = np.array(rgb_image) # [H, W, C]
    H, W, C = rgb_image.shape

    assert C == 3, "Error: Number of channels is not 3."

    rgb_image = np.expand_dims(rgb_image, 0)
    #rgb_image = tf.convert_to_tensor(rgb_image, dtype=tf.float32)

    model = Model(  is_training=False,
                    batch_size=1, # frames, 1 for image
                    img_height=H,
                    img_width=W,
                    imagenet_norm=True)
    
    with tf.Session(config=session_config) as sess:
        sess.run(tf.global_variables_initializer())
        model.inference_depth(rgb_image, sess) # TODO: How to get output?

if __name__ == '__main__':
    config_path = parseArgs(sys.argv[1:])
    config_dict = loadJson(config_path)
    main(config_dict)