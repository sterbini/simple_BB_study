# Introduction

After having 
```
git clone https://github.com/sterbini/simple_BB_study.git
```
checkout  your branch (e.g. hl16 or runIII)
```
git checkout hl16
# or
# git checkout runIII
```

To install a new distribution in a UBUNTU like machine

```
# tested on pcbe-abp-hpc002
source 0_install_miniforge.sh 
```

Then you can run the first job

```
cd 1_build_distr_and_collider/
python 1_build_distr_and_collider.py 
```

Then you can run the second job
```
cd ../2_configure_and_track/
python 2_configure_and_track.py 
```

