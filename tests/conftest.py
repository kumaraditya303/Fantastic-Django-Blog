# -*- coding: utf-8 -*-
import os

import pytest
from PIL import Image

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture(autouse=True, scope="module")
def image():
    os.makedirs("media", exist_ok=True)
    with open(os.path.join("media", "testing.jpeg"), "w") as f:
        Image.new("RGB", (100, 100), (150, 0, 0)).save(f)
