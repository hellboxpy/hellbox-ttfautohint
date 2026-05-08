from unittest.mock import MagicMock, patch

from hellbox.jobs.ttfautohint import Autohint


class TestAutohint:
    def test_init(self):
        assert Autohint()

    def test_process(self):
        file = MagicMock()
        copy = MagicMock()
        file.copy.return_value = copy
        copy.read_bytes.return_value = b"fake ttf data"

        with patch("hellbox.jobs.ttfautohint.autohint._autohint") as mock_ta:
            mock_ta.return_value = b"hinted ttf data"
            result = Autohint().process(file)

        file.copy.assert_called_once()
        mock_ta.assert_called_once_with(in_buffer=b"fake ttf data")
        copy.content_path.write_bytes.assert_called_once_with(b"hinted ttf data")
        assert result is copy
