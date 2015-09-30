#from multiprocessing import Process
#from multiprocessing import Process
import multiprocessing
import os
import time


def run_proc(name):
	print 'Run child process %s (%s)...'%(name,os.getpid())
	time.sleep(4)
if __name__ == '__main__':
	print 'Parent process %s.'%os.getpid()
	
	p = multiprocessing.Process(target=run_proc,args=('test',))
	print 'Process will start'
	
	p.start()
	p.join()
	print 'Process end.'
