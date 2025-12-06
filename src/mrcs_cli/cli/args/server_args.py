"""
Created on 6 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

https://realpython.com/command-line-interfaces-python-argparse/
"""

from mrcs_core.cli.args.mrcs_args import MRCSArgs


# --------------------------------------------------------------------------------------------------------------------

class ServerArgs(MRCSArgs):
    """unix command line handler"""

    def __init__(self, description):
        super().__init__(description)

        self._parser.add_argument('-s', '--set', action='store', nargs=3, help='set HOST PORT IS_SECURE')

        self._args = self._parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    # noinspection PyStatementEffect
    def is_valid(self):
        if not self.do_set:
            return True

        try:
            self.port
            self.is_secure
            return True

        except ValueError:
            return False


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def do_set(self):
        return bool(self._args.set)


    @property
    def host(self):
        return self._args.set[0] if self._args.set else None


    @property
    def port(self):
        return int(self._args.set[1]) if self._args.set else None


    @property
    def is_secure(self):
        return bool(int(self._args.set[2])) if self._args.set else None


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return f'ServerArgs:{{test:{self.test}, set:{self._args.set}, indent:{self.indent}, verbose:{self.verbose}}}'
