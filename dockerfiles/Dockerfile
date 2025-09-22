ARG BASE_IMAGE=stevendargaville/petsc_spack
FROM ${BASE_IMAGE}
# Checkout the main branch by default
# This is the branch of the spack build recipe we are checking out
# not the branch of PFLARE itself
ARG BRANCH=main

LABEL maintainer='Steven Dargaville'
LABEL description='pflare_spack'

ENV DEBIAN_FRONTEND=noninteractive
ENV CHECKOUT_BRANCH=$BRANCH

# Create non-root user and allow writing to the Spack store/DB (keeps cache reuse)
RUN useradd -m -s /bin/bash -u 1000 builder && \
    chown -R builder:builder /opt/spack

WORKDIR /build/
RUN chown -R builder:builder /build

USER builder
ENV HOME=/home/builder

# Build and install PFLARE with spack, test it works
# We build the main branch of PFLARE against three different petsc buids
# 1) Static libraries
# 2) Shared libraries
# 3) Shared libraries + python + kokkos
RUN set -e; \
    echo "Cloning branch: ${CHECKOUT_BRANCH}" && \
    git clone --branch ${CHECKOUT_BRANCH} https://github.com/PFLAREProject/PFLARE_spack.git && \
    spack repo add PFLARE_spack && \
    spack install -v --test=root pflare@main ^petsc~shared && \
    spack install -v --test=root pflare@main && \
    spack install -v --test=root pflare@main+python ^petsc+kokkos
    

