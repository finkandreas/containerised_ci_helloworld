from mpi4py import MPI

comm = MPI.Comm(MPI.COMM_WORLD)
size = comm.Get_size()
rank = comm.Get_rank()

print(f'Hello from rank {rank}. {size=}')
