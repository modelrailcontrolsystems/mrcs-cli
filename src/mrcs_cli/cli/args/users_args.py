"""
Created on 20 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

https://realpython.com/command-line-interfaces-python-argparse/
"""

from mrcs_cli.cli.args.cli_args import CLIArgs


# --------------------------------------------------------------------------------------------------------------------

class UsersArgs(CLIArgs):
    """unix command line handler"""

    def __init__(self, description):
        super().__init__(description)

        group = self._parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-s', '--self', action='store_true',
                           help='find myself')

        group.add_argument('-l', '--list', action='store_true',
                           help='list all users (must be ADMIN)')

        group.add_argument('-d', '--delete', action='store', type=str,
                           help='delete the given user (must be ADMIN)')

        self._args = self._parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def self(self):
        return self._args.self


    @property
    def list(self):
        return self._args.list


    @property
    def delete(self):
        return self._args.delete


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return (f'UsersArgs:{{self:{self.self}, list:{self.list}, delete:{self.delete}, '
                f'indent:{self.indent}, verbose:{self.verbose}}}')
