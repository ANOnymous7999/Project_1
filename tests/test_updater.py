import unittest
from unittest.mock import patch, MagicMock
import subprocess
from indiosint.updater import check_for_updates, perform_update

class TestUpdater(unittest.TestCase):

    @patch('os.path.exists')
    @patch('subprocess.run')
    @patch('subprocess.check_output')
    def test_check_for_updates_up_to_date(self, mock_check_output, mock_run, mock_exists):
        mock_exists.return_value = True

        # Mock upstream check
        mock_upstream = MagicMock()
        mock_upstream.returncode = 0
        mock_run.return_value = mock_upstream

        # Mock local and remote hashes
        mock_check_output.side_effect = [b"hash1\n", b"hash1\n"]

        self.assertFalse(check_for_updates())

    @patch('os.path.exists')
    @patch('subprocess.run')
    @patch('subprocess.check_output')
    def test_check_for_updates_new_version(self, mock_check_output, mock_run, mock_exists):
        mock_exists.return_value = True

        # Mock upstream check
        mock_upstream = MagicMock()
        mock_upstream.returncode = 0
        mock_run.return_value = mock_upstream

        # Mock local and remote hashes
        mock_check_output.side_effect = [b"hash1\n", b"hash2\n"]

        self.assertTrue(check_for_updates())

    @patch('subprocess.run')
    def test_perform_update_success(self, mock_run):
        mock_res = MagicMock()
        mock_res.stdout = "Already up to date."
        mock_run.return_value = mock_res

        self.assertTrue(perform_update())

if __name__ == "__main__":
    unittest.main()
