"""
Created on 18 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

https://realpython.com/command-line-interfaces-python-argparse/
"""

from mrcs_cli.cli.args.cli_args import CLIArgs


# --------------------------------------------------------------------------------------------------------------------

class SessionArgs(CLIArgs):
    """unix command line handler"""


    def __init__(self, description):
        super().__init__(description)

        group = self._parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-s', '--set-email', action='store', type=str,
                           help='store the given email address')

        group.add_argument('-e', '--erase-email', action='store_true',
                           help='erase the stored email address')

        group.add_argument('-c', '--create-session', action='store_true',
                           help='create a new API session')

        group.add_argument('-d', '--delete-session', action='store_true',
                           help='delete the current API session')

        self._args = self._parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def set_email(self):
        return self._args.set_email


    @property
    def erase_email(self):
        return self._args.erase_email


    @property
    def create_session(self):
        return self._args.create_session


    @property
    def delete_session(self):
        return self._args.delete_session


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return (f'SessionArgs:{{set_email:{self.set_email}, erase_email:{self.erase_email}, '
                f'create:{self.create_session}, delete:{self.delete_session}, '
                f'indent:{self.indent}, verbose:{self.verbose}}}')
