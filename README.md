# PFLARE Spack External Repository

Usage:
1) Clone this repo

2) Add this repo to Spack:
   ```bash
   spack repo add PFLARE_spack
   ```

3) Install PFLARE and check it worked:
   ```bash
   spack install --test=root pflare
   ```
   or there is a Python variant that uses petsc4py to build Python bindings for PFLARE:
   ```bash
   spack install --test=root pflare+python
   ```   
   All other configurations depend on the options used during the PETSc build. For example, to build a static version of PFLARE, set the shared library variant for PETSc to false:
   ```bash
   spack install --test=root pflare ^petsc~shared
   ```      

4) To enable easy linking to PFLARE (this sets environmental variables):
   ```bash
   spack load pflare+python
   ```
