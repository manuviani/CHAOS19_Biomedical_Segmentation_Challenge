# """chaos_dataset dataset."""

# import tensorflow_datasets as tfds
# from . import chaos_dataset_dataset_builder


# class ChaosDatasetTest(tfds.testing.DatasetBuilderTestCase):
#   """Tests for chaos_dataset dataset."""
#   # TODO(chaos_dataset):
#   DATASET_CLASS = chaos_dataset_dataset_builder.Builder
#   SPLITS = {
#       'train': 3,  # Number of fake train example
#       'test': 1,  # Number of fake test example
#   }

#   # If you are calling `download/download_and_extract` with a dict, like:
#   #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
#   # then the tests needs to provide the fake output paths relative to the
#   # fake data directory
#   # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


# if __name__ == '__main__':
#   tfds.testing.test_main()


"""Tests for imagenet dataset module."""
from tensorflow_datasets import testing
import tensorflow_datasets as tfds
from . import chaos_dataset_dataset_builder


class ChaosDatasetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = chaos_dataset_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on each split.
      # "train": 1,
      # "validate": 1,
      # "test": 1,
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}

  # DL_EXTRACT_RESULT = {
  #     "images": ".",
  #     "annotations": ".",
  # }


if __name__ == "__main__":
  testing.test_main()
