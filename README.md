SublimeLinter-contrib-ameba
================================

[![Build Status](https://travis-ci.org/epergo/SublimeLinter-contrib-ameba.svg?branch=master)](https://travis-ci.org/epergo/SublimeLinter-contrib-ameba)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [ameba](https://github.com/veelenga/ameba). It will be used with files that have crystal syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install both SublimeLinter and the linter plugin.

Before installing this plugin, you must ensure that `ameba` is installed on your project. Add `ameba` to your `shard.yml` file, in `development_dependencies`:

```crystal
development_dependencies:
  ameba:
    github: veelenga/ameba
```

Run `shards install`, this will place an `ameba` executable in a `bin` folder inside your project's folder.

That executable will be used by default, if you want to use another executable just specify it in SublimeLinter User settings.

If an `.ameba.yml` config file is located in your project's root path, it will be used.

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

- Custom `ameba` executable:

```json
// SublimeLinter Settings - User
{
  "linters": {
    "ameba": {
      "executable": "path_to_ameba_executable"
    }
  },
}
```
