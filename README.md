# Shaula

A shared Python namespace for domain-specific tools and AI components.
Python 3.10+. The lightweight base package provides `shaula.core`.

## Anomaly model comparison

With the 0.0.3 core and 0.2.2 comparison releases:

```sh
python -m pip install --upgrade "shaula-ai[anomaly]"
```

```python
from shaula import core
from shaula.anomaly import compare

report = compare.compare(model_results)
print(compare.to_terminal(report))
```

See [Anomaly Compare examples and input format](https://github.com/shaula-ai/Anomaly-Lab/tree/main/anomaly_lab_compare).
The extra installs `shaula-anomaly-compare`; it does not put a generic
`compare` module at the root of `shaula`.

| Import | Distribution | Status |
| --- | --- | --- |
| `shaula.core` | `shaula-ai` | Base package |
| `shaula.anomaly.compare` | `shaula-anomaly-compare` | `anomaly` extra |
| `shaula.router` | `shaula-skill-router` | Separate component; extra not enabled yet |
| `shaula.maker` | `shaula-skill-maker` | Planned |

## Component layout

Use shared PEP 420 namespaces. Do not add `shaula/__init__.py` or
`shaula/anomaly/__init__.py`. Components live below their domain; future domains
may have their own `compare` modules. Enable extras only when their dependencies
are available on PyPI. Upgrade from 0.0.1, whose root initializer conflicted
with the namespace; that release has been yanked.

## Licensing

The core package is MIT. Each optional component has its own license.
Anomaly Compare 0.2.2 is available for noncommercial research and education;
commercial use requires a separate written license. Contact shaula.ai.dev@gmail.com.
Installing an extra does not grant additional rights to its components.
