
# %%
from ruamel.yaml import YAML
yaml = YAML()

# open yaml file in ./1_build_distr_and_collider/config.yaml

with open('./1_build_distr_and_collider/config.yaml') as file:
    config = yaml.load(file)

# %%
config['config_mad']['links']['acc-models-lhc']='../modules/example_DA_study/external_dependencies/acc-models-lhc'

with open('./1_build_distr_and_collider/config.yaml', 'w') as file:
    yaml.dump(config, file)

# %%

with open('./2_configure_and_track/config.yaml') as file:
    config = yaml.load(file)

# %%
config['config_collider']['config_beambeam']['mask_with_filling_pattern']['pattern_fname']='../modules/example_DA_study/studies/filling_scheme/8b4e_1972b_1960_1178_1886_224bpi_12inj_800ns_bs200ns.json'

with open('./2_configure_and_track/config.yaml', 'w') as file:
    yaml.dump(config, file)
# %%
