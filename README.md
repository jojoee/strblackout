# strblackout

[![CI and CD](https://github.com/jojoee/strblackout/actions/workflows/continuous-integration.yml/badge.svg?branch=master)](https://github.com/jojoee/strblackout/actions/workflows/continuous-integration.yml)
[![PyPI version fury.io](https://badge.fury.io/py/strblackout.svg)](https://pypi.python.org/pypi/strblackout/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/strblackout/branch/master/graph/badge.svg)](https://codecov.io/gh/jojoee/strblackout)

String replacement or Blackout text with *** e.g. 08*****123

## Installation

```
pip install strblackout
```

## Usage

```python
from strblackout import blackout

blackout("123456789") == "123456789"
blackout("123456789", left=5) == "*****6789"
blackout("123456789", right=3) == "123456***"
blackout("123456789", left=3, replacement="x") == "xxx456789"
blackout("123", left=10, right=20) == "***"
```
