from SublimeLinter.lint import Linter


class Ameba(Linter):
    regex = (r'^.+:(?P<line>\d+):(?P<col>\d+): ((?P<error>E)|(?P<warning>W|C)): (?P<message>.+)$')
    multiline = False

    tempfile_suffix = '-'

    defaults = {
        'selector': 'source.crystal',
        'executable': '${folder}/bin/ameba'
    }

    def cmd(self):
        settings = self.get_view_settings()
        return (settings['executable'], '--format', 'flycheck', '${file}')
