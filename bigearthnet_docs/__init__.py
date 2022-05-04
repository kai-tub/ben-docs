import importlib.metadata
from enum import Enum
import pdb
import appdirs
from pathlib import Path
import tarfile
from importlib import resources
import bigearthnet_docs


__version__ = importlib.metadata.version("bigearthnet_docs")


class Resource(str, Enum):
    s1_example_bz2_tar = "BigEarthNet-S1-Example.tar.bz2"
    s2_example_bz2_tar = "BigEarthNet-S2-Example.tar.bz2"

    def __str__(self):
        return self.value


USER_DIR = Path(appdirs.user_data_dir("bigearthnet_documentation"))
USER_DIR.mkdir(exist_ok=True, parents=True)


def _extract_sentinel_resource(resource, target_dir, subfolder) -> Path:
    extracted_dir = target_dir / subfolder
    if extracted_dir.exists():
        return extracted_dir

    if not resources.is_resource(bigearthnet_docs, resource):
        raise ValueError(
            f"{resource} resource is not available! This means that it was forgotten to be packaged."
        )
    with resources.path(bigearthnet_docs, resource) as resource_path:
        tar_file = tarfile.open(resource_path)
        folder_dir = tar_file.getnames()[0]
        assert folder_dir == subfolder
        tar_file.extractall(target_dir)
    assert extracted_dir.exists()
    return extracted_dir


def get_s1_example_folder_path() -> Path:
    resource = Resource.s1_example_bz2_tar
    target_dir = USER_DIR
    subfolder = "BigEarthNet-S1-Example"
    return _extract_sentinel_resource(resource, target_dir, subfolder)


def get_s2_example_folder_path() -> Path:
    resource = Resource.s2_example_bz2_tar
    target_dir = USER_DIR
    subfolder = "BigEarthNet-S2-Example"
    return _extract_sentinel_resource(resource, target_dir, subfolder)


def get_s1_example_patch_path() -> Path:
    s1_dir = get_s1_example_folder_path()
    return sorted(p for p in s1_dir.iterdir())[0]


def get_s2_example_patch_path() -> Path:
    s2_dir = get_s2_example_folder_path()
    return sorted(p for p in s2_dir.iterdir())[0]
