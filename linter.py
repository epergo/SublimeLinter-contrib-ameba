from SublimeLinter.lint import Linter


class Ameba(Linter):
    regex = (r'^.+:(?P<line>\d+):(?P<col>\d+): ((?P<error>E)|(?P<warning>.)): (?P<message>.+)$')
    multiline = False

    tempfile_suffix = '-'

    defaults = {
        'selector': 'source.crystal',
        'auto_fix': false,
        'executable': '${folder}/bin/ameba'
    }

    def cmd(self):
        settings = self.get_view_settings()
        if settings['auto_fix']:
            return (settings['executable'], '--format', 'flycheck', '--fix', '${file}')
        else:
            return (settings['executable'], '--format', 'flycheck', '${file}')
