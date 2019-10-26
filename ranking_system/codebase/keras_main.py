import keras
from keras.engine import Model
from keras.applications import VGG19

bm = VGG19(weights="imagenet")
model = Model.get_weights(path)
path = "/home/flomko/.keras/models/vgg19_weights_tf_dim_ordering_tf_kernels.h5"
bm.load_weights(path)
path = "/home/flomko/.keras/models/vgg19_weights_tf_dim_ordering_tf_kernels.h5"
bm.load_weights(path)
dn = VGG19.load_weights(path)
dn = VGG19().load_weights(path)
dn
# dn.
dn
VGG19().load_weights(path)
# history
