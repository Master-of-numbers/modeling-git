# Інструкція розгортання Marimo

## Table Of Contents

- [Setup windows](#setup-windows)

### Setup windows

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv tool install marimo

marimo edit notebook.py --sandbox
```
