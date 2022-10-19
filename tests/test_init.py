import pytest
from bigearthnet_common.constants import BEN_S1_RE, BEN_S2_RE
from bigearthnet_docs import (
    get_s1_example_folder_path,
    get_s1_example_patch_path,
    get_s2_example_folder_path,
    get_s2_example_patch_path,
)


def test_s1_folder():
    assert get_s1_example_folder_path().exists()


def test_s2_folder():
    assert get_s2_example_folder_path().exists()


def test_s1_example_patch_folder():
    s1_patch_path = get_s1_example_patch_path()
    assert BEN_S1_RE.fullmatch(s1_patch_path.name)


def test_s2_example_patch_folder():
    s2_patch_path = get_s2_example_patch_path()
    assert BEN_S2_RE.fullmatch(s2_patch_path.name)
