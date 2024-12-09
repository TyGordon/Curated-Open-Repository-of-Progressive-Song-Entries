# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['corpus_explorer.py'],
    pathex=[],
    binaries=[],
    datas=[('full_corpus.xml', '.'), ('resources.qrc', '.'), ('corpus_gui.ui', '.'), ('Images', 'Images')],
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
    name='corpus_explorer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Images\\uk_icon.ico'],
)
