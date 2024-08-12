
# %%
import yaml

# open yaml file in ./1_build_distr_and_collider/config.yaml

with open('./1_build_distr_and_collider/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# %%
config['config_mad']['links']['acc-models-lhc']='../modules/example_DA_study/external_dependencies/acc-models-lhc'

with open('./1_build_distr_and_collider/config.yaml', 'w') as file:
    yaml.dump(config, file)
# %%
