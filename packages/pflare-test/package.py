# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *
from spack.util.executable import Executable


class PflareTest(MakefilePackage):
    """Downstream linkage smoke-test for the pflare Spack package.

    Explicitly exercises spec['pflare'].headers and spec['pflare'].libs
    so that a missing @property decorator on either in pflare/package.py
    fails this build during build() with AttributeError.
    """

    homepage = "https://github.com/PFLAREProject/PFLARE"
    has_code = False

    maintainers("stevendargaville")
    license("MIT")

    version("1.0")

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("pflare")
    depends_on("petsc")

    def build(self, spec, prefix):
        pflare = spec["pflare"]

        # The regression trap: access .headers / .libs as attributes (not
        # call them). If the pflare recipe drops @property, these return
        # method objects and the .include_flags / .ld_flags accesses
        # below raise AttributeError.
        hdrs = pflare.headers
        libs = pflare.libs
        include_flags = hdrs.include_flags
        link_flags = libs.ld_flags

        src_dir = join_path(self.package_dir, "files")
        work = self.stage.source_path
        os.makedirs(work, exist_ok=True)
        for name in ("main.c", "main.F90", "Makefile"):
            shutil.copy(join_path(src_dir, name), work)

        make_args = [
            f"PFLARE_CPPFLAGS={include_flags}",
            f"PFLARE_LDFLAGS={link_flags}",
            f"PETSC_DIR={spec['petsc'].prefix}",
            "PETSC_ARCH=",
        ]
        with working_dir(work):
            make("all", *make_args)

    def install(self, spec, prefix):
        work = self.stage.source_path
        with working_dir(work):
            os.makedirs(prefix.bin, exist_ok=True)
            install("pflare_test_c", prefix.bin)
            install("pflare_test_f", prefix.bin)

    @run_after("install")
    def run_serial(self):
        if not self.run_tests:
            return
        Executable(join_path(self.prefix.bin, "pflare_test_c"))()
        Executable(join_path(self.prefix.bin, "pflare_test_f"))()
