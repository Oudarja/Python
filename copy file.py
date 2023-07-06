#copyfile->copies contents of a file
#copy->copyfile+permisision mode
#copy2->copy()+copy metadata
import shutil
import os
shutil.copy('test1.txt', 'yoo.txt')
'''directories can also be used to copy a file'''
'''move a file from one location to another'''
'''file can not be moved from one disk to another disk'''
src='src.tx'
des='F:\\certificate\\src.txt'
os.replace(src,des)
''' to remove a file'''
#os.remove(path) delete a file
#os.remdir(path) delete an empty directory
#shutil.rmtree(path) delet a folder that is not empty
os.remove('test1.txt')
os.rmdir('hellomyboy')
shutil.rmtree('hello')
