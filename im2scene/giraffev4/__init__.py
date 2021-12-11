"""GIRAFFE v4 fix by masking samples for CARLA foreground objects that are out of bounds"""

from im2scene.giraffev4 import (
    config, training, models
)

__all__ = [
    config, training, models
]
