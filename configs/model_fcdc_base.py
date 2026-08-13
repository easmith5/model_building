from magiconfig import MagiConfig

# base config
config = MagiConfig()
config.channel = 's'
config.mmed = 1000
# StringFlav:mesonUDvector = 0.5 in Monash tune (and CP5 tune)
# StringFlav:mesonUDvector sets V/PS, while probVector sets V/(V+PS)
config.pvector = 0.333
config.spectrum = 'fcdc'
config.gq = 0.25
