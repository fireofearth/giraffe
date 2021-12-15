"""GIRAFFE v8
- separate decoders for each object
- masking fix
- scaling of background features from decoder
"""

from im2scene.giraffev8 import (
    config, training, models
)

__all__ = [
    config, training, models
]
