import unittest

loader = unittest.TestLoader()
start_dir = 'pyverm'
suite = loader.discover(start_dir, pattern="test_*")


print("\n")
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)