# pflare-test: compiles bundled smoke-test sources against installed pflare.
#
# This follows the PETSc make pattern used in PFLARE tests by including
# PETSc's conf variables/rules, then prepending pflare libs to LDLIBS.

PFLARE_CPPFLAGS ?=
PFLARE_LDFLAGS  ?=
PETSC_DIR ?=
PETSC_ARCH ?=

CFLAGS_INPUT := $(CFLAGS)
FFLAGS_INPUT := $(FFLAGS)
CPPFLAGS_INPUT := $(CPPFLAGS)
LDFLAGS_INPUT := $(LDFLAGS)

include ${PETSC_DIR}/lib/petsc/conf/variables
include ${PETSC_DIR}/lib/petsc/conf/rules

override CFLAGS += $(CFLAGS_INPUT)
override FFLAGS += $(FFLAGS_INPUT)
override CPPFLAGS += $(CPPFLAGS_INPUT) $(PFLARE_CPPFLAGS)
override LDFLAGS += $(LDFLAGS_INPUT)

LDLIBS := $(PFLARE_LDFLAGS) $(LDLIBS)

all: pflare_test_c pflare_test_f

pflare_test_c: main.c
	$(CLINKER) $(CPPFLAGS) $(CFLAGS) -o $@ $< $(LDFLAGS) $(LDLIBS)

pflare_test_f: main.F90
	$(FLINKER) $(CPPFLAGS) $(FFLAGS) -o $@ $< $(LDFLAGS) $(LDLIBS)

clean::
	$(RM) -f pflare_test_c pflare_test_f

.PHONY: all clean
