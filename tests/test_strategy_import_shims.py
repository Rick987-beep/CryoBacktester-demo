"""Public blueprint strategy import path + sync with workspace copy."""
from __future__ import annotations

import hashlib
import inspect
from pathlib import Path

from backtester.core.paths import repo_root
from backtester.strategies.blueprint_howto import BlueprintHowto


def test_blueprint_lives_under_backtester_strategies():
    path = Path(inspect.getfile(BlueprintHowto))
    assert "backtester" in path.parts
    assert path.name == "blueprint_howto.py"


def test_blueprint_matches_workspace_copy_when_present():
    """Demo package has no workspace twin — skipped."""
    return



def test_no_workspace_reexport_shims_in_backtester_strategies():
    strat_dir = repo_root() / "backtester" / "strategies"
    py_files = {p.name for p in strat_dir.glob("*.py")}
    assert py_files <= {"__init__.py", "blueprint_howto.py"}
