import tensorflow_datasets as tfds
import pandas as pd

tfds.load('celeb_a', split=['train','test'], data_dir="/app/data/")
