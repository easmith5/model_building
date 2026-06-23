import os, sys, imp
from magiconfig import MagiConfig

config_dir = os.path.join(os.getcwd(), "configs")
sys.path.append(config_dir)

nEvents = 10000
config_name = "configs/model_fcdc_10.py"
configs_fcdc = imp.load_source("configs_fcdc", config_name)
from configs_fcdc import config
objs = [obj for obj in dir(config) if obj.startswith('Nc')]

for obj in objs:
    logName = "model_"+obj
    cmd = f'./run_model helper -C {config_name} -O config.{obj} --dir  /eos/uscms/store/user/easmith/svj/fcdc --steps all --events {nEvents} --verbose >  /eos/uscms/store/user/easmith/svj/fcdc/{logName}.log'
    print(cmd)
    os.system(cmd)
