# PFLARE Spack External Repository

Usage:
1) Clone this repo

2) Add this repo to Spack:
   ```bash
   spack repo add PFLARE_spack
   ```

3) Install PFLARE and check it worked:
   ```bash
   spack install --test=root pflare+python
   ```

4) To enable easy building/linking with PFLARE (this sets environmental variables):
   ```bash
   spack load pflare+python
   ```
