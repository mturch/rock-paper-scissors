import unittest
from custom_utils import get_absolute_import_path
import os

class TestGetAbsoluteImportPath(unittest.TestCase):
	def test_relative_path_to_absolute(self):
		"""
		Test that the function correctly converts a relative path to an absolute path.
		"""
		# Define a relative path
		relative_path = "../code/rock_paper_scissors/rock_paper_scissor.py"

		# Expected result is the absolute path to the given relative path
		expected_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
		expected_path = os.path.normpath(expected_path)

		# Get the actual result from the function
		actual_path = get_absolute_import_path(relative_path)

		# Assert that the actual path is equal to the expected path
		self.assertEqual(actual_path, expected_path)

	def test_current_directory(self):
		"""
		Test that the function handles relative paths pointing to the current directory.
		"""
		# Define a relative path pointing to the current directory
		relative_path = "."

		# Expected result is the absolute path to the current directory
		expected_path = os.path.dirname(os.path.abspath(__file__))

		# Get the actual result from the function
		actual_path = get_absolute_import_path(relative_path)

		# Assert that the actual path is equal to the expected path
		self.assertEqual(actual_path, expected_path)

	def test_parent_directory(self):
		"""
		Test that the function handles relative paths pointing to the parent directory.
		"""
		# Define a relative path pointing to the parent directory
		relative_path = ".."

		# Expected result is the absolute path to the parent directory
		expected_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

		# Get the actual result from the function
		actual_path = get_absolute_import_path(relative_path)

		# Assert that the actual path is equal to the expected path
		self.assertEqual(actual_path, expected_path)

if __name__ == '__main__':
	unittest.main()



