import os

print 'Process (%s) start...'%os.getpid()

pid = os.fork()

if pid == 0:
	print 'chind process (%s) and parent is %s.'%(os.getpid(),os.getppid())
else:
	print '(%s) just created child process (%s).'%(os.getpid(),pid)
