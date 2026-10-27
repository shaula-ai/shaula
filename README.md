# Shaula

A shared Python namespace for domain-specific tools and AI components. Python 3.10+.
The base package provides `shaula.core`; install domain extras for additional tools.

## Report preview

![English terminal report: two-model comparison](https://raw.githubusercontent.com/shaula-ai/Anomaly-Lab/main/docs/assets/anomaly-report-en.png)

Actual output from the published **shaula-anomaly-compare 0.2.2** CLI, rendered
with its ANSI colors inside a documentation frame. The example uses synthetic
scores; it is not a real model benchmark. No CPU/GPU performance is fabricated.
The package itself displays reports in your terminal and does not generate these PNGs.

## Install from PyPI

```sh
python -m pip install --upgrade "shaula-ai[anomaly]"
python -c "from shaula.anomaly import compare; print(compare.__version__)"
```

The verified releases are `shaula-ai 0.0.3` and `shaula-anomaly-compare 0.2.2`.
For reproducibility, use `python -m pip install "shaula-ai[anomaly]==0.0.3" "shaula-anomaly-compare==0.2.2"`.
To install only this component: `python -m pip install shaula-anomaly-compare`.

```python
from shaula.anomaly import compare
```

`anomaly` is the domain namespace. Installing only `shaula-ai` does not install
this optional component. The earlier generic `from shaula import compare` is not supported.

## Complete runnable example

Save the following as `quickstart.py`, then run `python quickstart.py`.
It prints an English report and explicitly saves the inputs, report and CSV.

```python
"""Runnable synthetic example for the published Shaula Anomaly Compare package."""
import json
from pathlib import Path
from shaula.anomaly import compare

labels = [0, 0, 1, 1]  # 0 = normal; 1 = defective
models = []
for name, scores in [
    ("model-a", [0.1, 0.2, 0.8, 0.9]),
    ("model-b", [0.1, 0.7, 0.6, 0.9]),
]:
    models.append({
        "model_id": name,
        "dataset_fingerprint": "synthetic-demo-v1",
        "preprocessing": {"source": "synthetic scores"},
        "threshold": 0.5,
        "threshold_source": "predefined",
        "metadata": {"synthetic": True},
        "samples": [
            {"sample_id": str(i), "label": label, "score": score}
            for i, (label, score) in enumerate(zip(labels, scores))
        ],
    })

report = compare.compare(models)
print(compare.to_terminal(report))  # English by default

# Explicit exports: the library does not create these automatically.
Path("models.json").write_text(json.dumps(models, indent=2), encoding="utf-8")
Path("comparison.json").write_text(compare.to_json(report), encoding="utf-8")
Path("comparison.csv").write_text(compare.to_csv(report), encoding="utf-8")

```

Expected results from these synthetic inputs:

| Model | Image AUROC | F1 | Missed defects | Normal images falsely flagged |
| --- | ---: | ---: | ---: | ---: |
| model-a | 1.00 | 1.00 | 0 / 2 | 0 / 2 |
| model-b | 0.75 | 0.80 | 0 / 2 | 1 / 2 |

Both catch the two defective images; model-b also flags one normal image.
On this small example, model-a makes fewer errors. This is not a general model
recommendation: validate real models on independent, representative test data.

## CLI: English, Traditional Chinese and Simplified Chinese

Run the example above first to create `models.json` and `comparison.json`.
All commands below use those files.

| Language | Flag | Behavior |
| --- | --- | --- |
| English | omit `--lang`, or use `--lang en` | Default |
| 繁體中文 | `--lang zh-TW` | Traditional Chinese |
| 简体中文 | `--lang zh-CN` | Simplified Chinese |

```sh
# English (default)
shaula-anomaly-compare compare models.json
# English (explicit)
shaula-anomaly-compare compare models.json --lang en
# Traditional Chinese / 繁體中文
shaula-anomaly-compare compare models.json --lang zh-TW
# Simplified Chinese / 简体中文
shaula-anomaly-compare compare models.json --lang zh-CN

# Re-display a saved report without recomputing model predictions
shaula-anomaly-compare report comparison.json --lang zh-TW
# Conclusions only, with ANSI colors
shaula-anomaly-compare report comparison.json --summary --color always
# Explicitly save JSON and CSV
shaula-anomaly-compare compare models.json --output comparison.json --csv comparison.csv
```

If the shell cannot find the executable, use the equivalent module command:

```sh
python -m shaula.anomaly.compare compare models.json --lang zh-CN
```

`--color auto` is the default. Use `--color always` to force colors or
`--color never` for plain text. On Windows, if redirected output has encoding
problems, use `python -X utf8 -m shaula.anomaly.compare report comparison.json`.
Language changes affect the report text, not model IDs, numeric results or JSON keys.

Python callers can also select the language:

```python
print(compare.to_terminal(report))                 # English
print(compare.to_terminal(report, lang="zh-TW"))   # 繁體中文
print(compare.to_terminal(report, lang="zh-CN"))   # 简体中文
```

<details>
<summary>Traditional Chinese report / 繁體中文報告</summary>

![Traditional Chinese terminal report](https://raw.githubusercontent.com/shaula-ai/Anomaly-Lab/main/docs/assets/anomaly-report-zh-TW.png)

</details>

<details>
<summary>Simplified Chinese report / 简体中文报告</summary>

![Simplified Chinese terminal report](https://raw.githubusercontent.com/shaula-ai/Anomaly-Lab/main/docs/assets/anomaly-report-zh-CN.png)

</details>


## Components

| Import | Distribution | Install |
| --- | --- | --- |
| `shaula.core` | `shaula-ai` | `pip install shaula-ai` |
| `shaula.anomaly.compare` | `shaula-anomaly-compare` | `pip install "shaula-ai[anomaly]"` |
| `shaula.router` | `shaula-skill-router` | Separate component; extra not enabled |
| `shaula.maker` | `shaula-skill-maker` | Planned |

[Full comparison documentation and input contract](https://github.com/shaula-ai/Anomaly-Lab/tree/main/anomaly_lab_compare).

Use PEP 420 namespaces: no `shaula/__init__.py` or `shaula/anomaly/__init__.py`.
Future domains may provide their own comparison modules. Upgrade from the yanked
0.0.1 core release, whose root initializer conflicted with the shared namespace.

## Licensing

The core is MIT. Optional components retain their own licenses. Anomaly Compare
0.2.2 is available for noncommercial use; commercial licensing enquiries:
**shaula.ai.dev@gmail.com**. Installing an extra does not grant additional rights.
