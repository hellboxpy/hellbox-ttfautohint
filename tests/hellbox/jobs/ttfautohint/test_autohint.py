from pathlib import Path

from hellbox.source_file import SourceFile
from hellbox.jobs.ttfautohint import Autohint

FIXTURE = Path(__file__).parents[3] / "fixtures" / "RoundSans.ttf"


class TestAutohint:
    def test_init(self):
        assert Autohint()

    def test_flush_without_files(self):
        assert Autohint().flush([]) == []

    def test_process(self, tmp_path):
        source = SourceFile(FIXTURE, FIXTURE, tmp_path)
        result = Autohint().process(source)
        assert result.content_path.exists()
        assert result.content_path.read_bytes() != FIXTURE.read_bytes()
