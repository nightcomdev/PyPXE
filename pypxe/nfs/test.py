import nfsrpc
#chroot does not work becuase of reliance on os.urandom
#sudo mount -t nfs localhost:/ tmp
nfs = nfsrpc.NFS()
nfs.listen()