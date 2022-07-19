import os
import getpass
from tempfile import gettempdir
username = getpass.getuser()
username_in_users=gettempdir()[::-1][19:][::-1][9:]
