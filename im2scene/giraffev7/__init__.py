"""GIRAFFE v7
- uses separate decoders for each object
- hierarchical sampling of sample points
- with masking fix.
TODO: work in progress. Finish Generator
"""

from im2scene.giraffev7 import (
    config, training, models
)

__all__ = [
    config, training, models
]
