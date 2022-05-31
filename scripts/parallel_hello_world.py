#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpi4py import MPI

# Initialise MPI communicator
comm = MPI.COMM_WORLD
MPI_rank = comm.Get_rank()
MPI_size = comm.Get_size()

# Print rank number, and exit
print(f'Hello, this is rank {MPI_rank} of {MPI_size}')
