from ttfautohint import ttfautohint as _autohint

from hellbox import Chute, Hellbox


class Autohint(Chute):
    """Autohint runs ttfautohint on a TTF file."""

    def process(self, file):
        Hellbox.info(f"Autohinting: {file.name}")
        copy = file.copy()
        hinted = _autohint(in_buffer=copy.read_bytes())
        copy.content_path.write_bytes(hinted)
        return copy
