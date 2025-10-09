# PFLARE Spack External Repository

This repository provides a Spack package for PFLARE (https://github.com/PFLAREProject/PFLARE), including optional support for Python bindings via Cython and PETSc4Py.

Usage:
1) Clone this repo

2) Add this repo to Spack:
   ```bash
   spack repo add PFLARE_spack
   ```

3) Install PFLARE:
   ```bash
   spack install pflare
   ```
   PFLARE depends on PETSc, so the build configuration will follow the PETSc options you choose. For example, to build a static version of PETSc (and hence PFLARE), set the shared library variant for PETSc to false:
   ```bash
   spack install pflare ^petsc~shared
   ```
   or for example, to build PETSc (and hence PFLARE) with 64 bit integers:
   ```bash
   spack install pflare ^petsc+int64
   ```
   
4) After installation, you can set up your environment (e.g., ``LD_LIBRARY_PATH``, etc.) using:
   ```bash
   spack load pflare
   ```

## Optional Python variant
   
1) To build PFLARE with Python bindings (via Cython and PETSc4Py):
   ```bash
   spack install pflare+python
   ```
   or the test flag can be added to check that the Python bindings are built during the install:
   ```bash
   spack install --test=root pflare+python
   ```
   
2) After installation, you can set up your environment (including ``PYTHONPATH``) using:
   ```bash
   spack load pflare+python
   ```      
