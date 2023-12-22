# """chaos_dataset dataset."""

from pathlib import Path
import random
import keras
import tensorflow_datasets as tfds
import pydicom
import tensorflow as tf
import numpy as np
from PIL import Image

class Builder(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for chaos_dataset dataset."""

    VERSION = tfds.core.Version('1.0.0')
    RELEASE_NOTES = {
        '1.0.0': 'Initial release.'
    }
    
    base_path: Path = Path(__file__).parent


    def _info(self):
        return self.dataset_info_from_configs(
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(
                    shape=(None, None, 1)
                ),
                "segmentation_mask": tfds.features.Image(
                    shape=(None, None, 1)
                ),
            }),
            supervised_keys=("image", "segmentation_mask"),
            homepage="https://zenodo.org/records/3431873#.ZSKsIuxBy3I",
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns splits."""
        
        # dataset_dir = dl_manager.download_and_extract(
        #   'https://zenodo.org/records/3431873/files/CHAOS_Train_Sets.zip?download=1'
        # )

        # self.base_path = Path(dataset_dir) / "Train_Sets"

        # 60/20/20 split
        


        # Setup train and test splits
        train_split = tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "folder": 'train',
            },
        )
        validate_split = tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "folder": 'test',
            },
        )
        test_split = tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "folder": 'test',
            },
        )

        return [train_split, validate_split, test_split]
    
    def _generate_examples(self, folder: str):
        # path_base = "MR/1/T1DUAL/DICOM_anon/InPhase"    # pari      [2,4...]
        # path_base = "MR/1/T1DUAL/DICOM_anon/OutPhase"   # dispari   [1,3...]
        # path_base = "MR/1/T1DUAL/Ground"                # pari      [2,4...]

        # path_base = "MR/1/T2SPIR/DICOM_anon"
        # path_base = "MR/1/T2SPIR/Ground"


        # extra = "" if "T2SPIR" else "InPhase" + "OutPhase"
        # dcm_base  = "MR/{p_num}/{dicom_type}/DICOM_anon{extra}/{dicom_name}.dcm"   # IMG-0004-00004.dcm
        # mask_base = "MR/{p_num}/{dicom_type}/Ground/{dicom_name}.png"              # IMG-0004-00004.png

        mr_base = self.base_path.parent / folder

        for patient in (mr_base / "image").iterdir():

            for slice in patient.iterdir():
                yield random.getrandbits(256), {
                    "image": slice,
                    "segmentation_mask": str(slice).replace("image", "label")
                }

            # base_folder = mr_base / str(patient)

            # t2spir_folder = base_folder / "T2SPIR" / "DICOM_anon"
            # for dcm in list(t2spir_folder.iterdir()):
            #     yield random.getrandbits(256), {
            #         "image": self.load_dicom(dcm),
            #         "segmentation_mask": self.normalize_mask(dcm.parent.parent / "Ground" / f"{dcm.stem}.png")
            #     }

            # inPhase_folder =  base_folder / "T1DUAL" / "DICOM_anon" / "InPhase"
            # for dcm in list(inPhase_folder.iterdir()):
            #     yield random.getrandbits(256), {
            #         "image": self.load_dicom(dcm),
            #         "segmentation_mask": self.normalize_mask(dcm.parent.parent.parent / "Ground" / f"{dcm.stem}.png")
            #     }

            # outPhase_folder = base_folder / "T1DUAL" / "DICOM_anon" / "OutPhase"
            # for dcm in list(outPhase_folder.iterdir()):
            #     mask_name = "-".join(dcm.stem.split("-")[:-1]) + "-" + str(1+int(dcm.stem.split("-")[-1])).zfill(5)

            #     yield random.getrandbits(256), {
            #         "image": self.load_dicom(dcm),
            #         "segmentation_mask": self.normalize_mask(dcm.parent.parent.parent / "Ground" / f"{mask_name}.png")
            #     }