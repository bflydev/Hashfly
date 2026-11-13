import os
import sys
import hashlib
from pathlib import Path

# t_root is the path for your file path to the hashfly folder in your IDE
# t_root = Path("pathtoyourtest")
# then replace all calls of x_root with t_root to test it

x_root = Path(os.path.dirname(sys.executable))
hashes_path = x_root / "hashes"

def run(cdir: Path, ctarget: Path):
    ctarget.mkdir(parents=True, exist_ok=True)
    try:
        items = os.listdir(cdir)
    except PermissionError:
        return
    for i in items:
        citem_dir = cdir / i
        if citem_dir.resolve() == Path(hashes_path).resolve():
            continue
        if getattr(sys, "frozen", False) and citem_dir.resolve() == Path(sys.executable).resolve():
            continue
        if citem_dir.is_dir():
            tdir = ctarget / i
            run(citem_dir, tdir)
        elif citem_dir.is_file():
            cfile = citem_dir.stem + ".txt"
            tdir = ctarget / cfile
            rd = citem_dir.read_bytes()
            cf_hash = hashlib.sha256(rd).hexdigest()
            tdir.write_text(cf_hash, encoding="utf-8")
run(x_root, hashes_path)