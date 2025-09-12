# PFLARE Spack External Repository

Usage:
1) Clone this repo
   
2) Add this repo to Spack:
   - spack repo add pflare-spack-repo
   - spack repo list

3) Install PFLARE and check it worked:
   - spack install --test=root pflare+python

4) To use PFLARE (this sets environmental variables):
   - spack load pflare+python
