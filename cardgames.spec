# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project_dir = Path(SPECPATH)
assets_dir = project_dir / "assets"
datas = [
    (str(path), str(path.parent.relative_to(project_dir)))
    for path in assets_dir.rglob("*")
    if path.is_file()
]

a = Analysis(
    ['cardgames.py'],
    pathex=[str(project_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cardgames',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
