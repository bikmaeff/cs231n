import tensorflow as tf

FLAGS = tf.app.flags.FLAGS


tf.app.flags.DEFINE_string('Run_Mode', 'dev', '''run mode''')

tf.app.flags.DEFINE_integer('IMG_SIZE', 64, '''IMG_SIZE''')
tf.app.flags.DEFINE_integer('IMG_CHANNEL', 3, '''IMG_CHANNEL''')
tf.app.flags.DEFINE_integer('NUM_CLASS', 200, '''NUM_CLASS''')

tf.app.flags.DEFINE_integer('Train_Batch_Size', 256, '''Train_Batch_Size''')
tf.app.flags.DEFINE_integer('Val_Batch_Size', 256, '''Validation_Batch_Size''')
tf.app.flags.DEFINE_integer('Train_Steps', 80000, '''Total steps that you want to train''')
tf.app.flags.DEFINE_float('Init_lr', 0.01, '''Initial learning rate''')
tf.app.flags.DEFINE_float('Weight_Decay', 0.0002, '''scale for l2 regularization''')

tf.app.flags.DEFINE_boolean('USE_CKPT', False, '''USE_CKPT''')
tf.app.flags.DEFINE_string('CKPT_PATH', "ckpts/model_ckpt.dat", '''USE_CKPT''')