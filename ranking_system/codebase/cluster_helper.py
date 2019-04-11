import keras
from keras.engine import Model
from keras.applications import VGG19
bm = VGG19(weights='imagenet')
model = Model(inputs=bm.input, outputs=bm.get_layer('fc1').output)
model.get_weights()
file = '/home/flomko/.keras/models/vgg19_weights_tf_dim_ordering_tf_kernels.h5'
model.load_weights(file)
file2 = '/home/flomko/.keras/models/vgg19_weights_tf_dim_ordering_tf_kernels2.h5'
model.load_weights(file2)

