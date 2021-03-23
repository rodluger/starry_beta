<p align="center">
  <img width = "450" src="https://github.com/rodluger/starry/blob/master/docs/starry.png?raw=true"/>
  <br>
  This is the frozen beta version of <a href="https://github.com/rodluger/starry">starry</a>, used
  internally for testing. You probably want <a href="https://github.com/rodluger/starry">this repo</a> instead.
</p>
<p align="center">
  <a href="https://docs.google.com/viewer?url=https://github.com/rodluger/starry_beta/raw/master-pdf/tex/starry.pdf"><img src="https://img.shields.io/badge/read-the_paper-7d93c7.svg?style=flat"/></a>
  <a href="https://rodluger.github.io/starry/"><img src="https://img.shields.io/badge/read-the_docs-7d93c7.svg?style=flat"/></a>
</p>

## Installing

Thecode here is no longer maintained and may no longer be compatible with
recent versions of Python or the various packages it depends on. That said,
I was able to install `starry_beta` (2021/03/23) in a fresh conda environment
by running

```
conda create -n starry_beta python=3.7
conda activate starry_beta
pip install pybind11==2.2
python setup.py install
```