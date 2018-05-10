SublimeLinter-contrib-ameba
================================

[![Build Status](https://travis-ci.org/epergo/SublimeLinter-contrib-ameba.svg?branch=master)](https://travis-ci.org/epergo/SublimeLinter-contrib-ameba)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [ameba](https://github.com/veelenga/ameba). It will be used with files that have crystal syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `ameba` is installed on your project.

In order for `ameba` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-ameba settings:

|Setting|Description    |
|:------|:--------------|
|foo    |Something.     |
|bar    |Something else.|
