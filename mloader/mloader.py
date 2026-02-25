'''
Mloader is a kivy framework utility for preloading kv_lang files in custom widgets when trying to create self reliant/app independent widgets or kivy/kivymd components.

With mloader you avoid hard coding kv_lang file names for your python files which may lead to misspelled names and unnecessary errors.

Mloader is being developed & maintained with love by Nathan R.K, young developer passionate about Robotics, Machine learning & intelligent systems(in general) from Malawi(MW).

Dependencies:
	python 3.x
	Kivy framework

Note: While mloader applies to any project structure, better project files naming conventions and directory structuring may yield excellent results.

Example Usage:

	from kivymd.uix.screen import MDScreen
	from mloader import load_kv

	load_kv()  # No arguments needed — auto-detects the calling file!

	class ExampleIndependentScreen(MDScreen):
		pass

		or in __init__:
		load_kv()

Thank you for choosing mloader to support your pythoning journey!
'''

# built-in python packages
import logging
import inspect
from glob import glob
from pathlib import Path

# installed with kivy/kivymd
from kivy.lang import Builder

# configure module-level logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='[mloader] %(levelname)s: %(message)s')


def load_kv(mainfile: str = None) -> list:
	'''
	Loads the kv file related to the file from which it is called.

	First, it looks for a .kv file that matches the name of the calling python file.
	If not found, it falls back to loading all .kv files in the same directory.

	Params:
		mainfile (str, optional): Absolute path of the python file to resolve kv from.
		                          Defaults to auto-detecting the caller's file via inspect.

	Returns:
		list: A list of kv file paths that were successfully loaded.
	'''

	# auto-detect the caller's file if mainfile is not provided
	if mainfile is None:
		frame = inspect.stack()[1]
		mainfile = frame[1]
		logger.info(f'Auto-detected caller file: {mainfile}')

	caller_path = Path(mainfile).resolve()
	kv_filename = caller_path.stem + '.kv'
	kv_path = caller_path.parent / kv_filename

	loaded_files = []

	try:
		if str(kv_path) not in Builder.files:
			Builder.load_file(str(kv_path))
			loaded_files.append(str(kv_path))
			logger.info(f'Loaded matched kv file: {kv_path}')
		else:
			logger.info(f'Already loaded, skipping: {kv_path}')

	except FileNotFoundError:
		logger.warning(f'No matched kv file found for "{kv_filename}", falling back to glob...')

		av_paths = glob(str(caller_path.parent / '*.kv'))

		if not av_paths:
			logger.warning(f'No .kv files found in directory: {caller_path.parent}')
		else:
			for path in av_paths:
				if path not in Builder.files:
					try:
						Builder.load_file(path)
						loaded_files.append(path)
						logger.info(f'Loaded via glob: {path}')
					except Exception as e:
						logger.error(f'Failed to load {path}: {e}')

	return loaded_files

#files = load_kv()
#print(files)