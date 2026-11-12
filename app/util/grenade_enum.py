from enum import Enum

class GrenadeType(str, Enum):
    FLASHBANG = "flashbang"
    HE = "he"
    SMOKE = "smoke"
    MOLOTOV = "molotov"
    DECOY = "decoy"
