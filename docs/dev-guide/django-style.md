# Sigma Pi, Gamma Iota Chapter Website: Python Style Guide

[_(Back to developer guide)_](https://github.com/sigmapi-gammaiota/sigmapi-web/tree/master/docs/dev-guide/index.md)

## Tools

* We use `djlint` to speed up and simplify the process of formatting our django templates.
* Install `djlint` through pip using:

```bash
pip install djlint #Or use whatever pip alias you have
```

* Run `djlint` by executing the following command in the top level of the repo
* Do this before all commits

```bash
djlint --reformat --quiet . #Run djlint on the repo. Remove --quiet if you'd like to see the diff generated
```
