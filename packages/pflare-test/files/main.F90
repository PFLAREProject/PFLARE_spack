      program pflare_test_f
      use petscksp
#include "finclude/pflare.h"
#include "petsc/finclude/petscksp.h"
      implicit none
      PetscErrorCode :: ierr

      call PetscInitialize(PETSC_NULL_CHARACTER, ierr)
      if (ierr /= 0) stop 'PetscInitialize failed'
      print *, 'pflare_test_f OK'
      call PetscFinalize(ierr)
      end program pflare_test_f
