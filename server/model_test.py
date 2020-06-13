"""Model tests."""

import unittest
import model


class ModelTest(unittest.TestCase):
    """Various tests for classes in model."""

    def test_create_task(self):
        """Create new task."""
        task = model.Task()
        self.assertIsInstance(task, model.Task)

    def test_create_user(self):
        """Create new User."""
        user = model.User()
        self.assertIsInstance(user, model.User)


if __name__ == '__main__':
    unittest.main()
