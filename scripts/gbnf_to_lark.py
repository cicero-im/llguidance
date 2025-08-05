#!/usr/bin/env python3

# For standalone use, please use this:
# https://github.com/guidance-ai/llguidance/blob/main/python/llguidance/gbnf_to_lark.py

import os
import subprocess
import sys
from security import safe_command

p = os.path.join(os.path.dirname(__file__), "../python/llguidance/gbnf_to_lark.py")
r = safe_command.run(subprocess.run, ["python3", p] + sys.argv[1:], stdout=sys.stdout, stderr=sys.stderr)
sys.exit(r.returncode)
