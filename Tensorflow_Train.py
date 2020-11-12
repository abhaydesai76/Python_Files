import numpy as np
import tensorflow as tf
import math

from time import time
from include.data import get_data_set
from include.model import model, xmlrpc

train_x, train_y = get_data_set("train")
test_x, test_y = get_data_set("test")

