# hellbox-ttfautohint

A [hellbox](https://github.com/hellboxpy/hellbox) plugin that runs [ttfautohint](https://freetype.org/ttfautohint/) on TTF files using [ttfautohint-py](https://github.com/fonttools/ttfautohint-py).

## Usage

```python
from hellbox import Hellbox
from hellbox.jobs.ttfautohint import Autohint

with Hellbox("hint") as task:
    task.read("build/*.ttf") >> Autohint() >> task.write("hinted")
```

## Installation

```sh
hell add hellbox-ttfautohint
```

## Development

```sh
uv sync
uv run pytest
```
