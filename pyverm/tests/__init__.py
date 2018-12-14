import unittest
loader = unittest.TestLoader()
start_dir = ''
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner(verbosity=2, descriptions=True)
runner.run(suite)