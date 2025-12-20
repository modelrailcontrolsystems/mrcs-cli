"""
Created on 20 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

https://realpython.com/command-line-interfaces-python-argparse/
"""

from mrcs_cli.cli.args.cli_args import CLIArgs


# --------------------------------------------------------------------------------------------------------------------

class MessagesArgs(CLIArgs):
    """unix command line handler"""

    def __init__(self, description):
        super().__init__(description)

        self._parser.add_argument('-l', '--list', action='store', type=int, required=True,
                                  help='the number of messages to list')

        self._args = self._parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def list(self):
        return self._args.list


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return f'MessagesArgs:{{list:{self.list}, indent:{self.indent}, verbose:{self.verbose}}}'
