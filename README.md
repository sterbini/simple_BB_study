# Introduction

After having 
```
git clone 
```

go to your branch.
```
git checkut hl16
# or
# git checkout runIII
```

To install a new distribution in a UBUNTU like machine

```
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

