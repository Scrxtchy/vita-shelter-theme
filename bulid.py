import os
#import zipfile
from shutil import copy2, make_archive, rmtree
if os.path.exists('./build') is False:
	os.makedirs('build')
for root, dirs, files in os.walk("."):
	try:
		dirs.remove('build')
		dirs.remove('.git')
	except Exception:
		pass
	files = [ file for file in files if not file.endswith( ('.py','.psd','.db', '.zip') ) ]
	for file in files:
		copy2(os.path.join(root,file), './build/')

make_archive(os.path.split(os.getcwd())[-1], 'zip', './build/')
rmtree('./build/')