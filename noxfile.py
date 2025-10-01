import os
import shutil
import stat
from pathlib import Path
from typing import Any

import nox

CTT_DIR = Path(".ctt")

nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error = True
nox.options.sessions = [
    "ctt",
]


@nox.session()
def ctt(session: nox.Session):
    session.install("copier-template-tester")

    for git_dir in CTT_DIR.glob("*/.git"):
        try_rmtree(session, git_dir)

    session.run("python", "ctt_strict.py", silent=not is_ci())


@nox.session(python=False)
def clean(session: nox.Session):
    try_rmtree(session, CTT_DIR)


# helper functions


def try_rmtree(session: nox.Session, path: Path):
    if not path.is_dir():
        return

    session.log(f"Removing directory: {path}")
    shutil.rmtree(path, onerror=on_rm_error)


def on_rm_error(func: Any, path: str, exc_info: Any):
    # from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
    path_ = Path(path)
    path_.chmod(stat.S_IWRITE)
    path_.unlink()


def is_ci():
    return os.getenv("CI") == "true"
