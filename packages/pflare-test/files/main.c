#include <petscksp.h>
#include "pflare.h"

int main(int argc, char **argv)
{
    PetscCall(PetscInitialize(&argc, &argv, NULL, "pflare-test\n"));
    PCRegister_PFLARE();
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "pflare_test_c OK\n"));
    PetscCall(PetscFinalize());
    return 0;
}
