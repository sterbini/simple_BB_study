
# %%
from ruamel.yaml import YAML
yaml = YAML()

# open yaml file in ./1_build_distr_and_collider/config.yaml

with open('./1_build_distr_and_collider/config.yaml') as file:
    config = yaml.load(file)
config['config_mad']['links']['acc-models-lhc']='../modules/example_DA_study/external_dependencies/acc-models-lhc'

with open('./1_build_distr_and_collider/config.yaml', 'w') as file:
    yaml.dump(config, file)


# open the 'optics_specific_tools.py' in '/home/sterbini/BBWC_review/simple_BB_study/1_build_distr_and_collider'
# and replace 'acc-models-lhc/lhc_acc-models-lhc_b4.seq' with 'acc-models-lhc/lhc_b4.seq'

# with open('/home/sterbini/BBWC_review/simple_BB_study/1_build_distr_and_collider/optics_specific_tools.py', 'r') as file:
#     filedata = file.read()
# # and replace 'acc-models-lhc/lhc_acc-models-lhc_b4.seq' with 'acc-models-lhc/lhc_b4.seq'
# filedata = filedata.replace('acc-models-lhc/lhc_acc-models-lhc_b4.seq', 'acc-models-lhc/lhcb4.seq')
# filedata = filedata.replace('acc-models-lhc/lhc_acc-models-lhc.seq', 'acc-models-lhc/lhc.seq')

# with open('/home/sterbini/BBWC_review/simple_BB_study/1_build_distr_and_collider/optics_specific_tools.py', 'w') as file:
#     file.write(filedata)

# %%

with open('./2_configure_and_track/config.yaml') as file:
    config = yaml.load(file)

# %%
config['config_collider']['config_beambeam']['mask_with_filling_pattern']['pattern_fname']='../modules/example_DA_study/studies/filling_scheme/8b4e_1972b_1960_1178_1886_224bpi_12inj_800ns_bs200ns.json'

with open('./2_configure_and_track/config.yaml', 'w') as file:
    yaml.dump(config, file)
# %%
