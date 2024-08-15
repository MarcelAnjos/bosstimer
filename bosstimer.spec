# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bosstimer.py'],
    pathex=[],
    binaries=[],
    datas=[('CAPA.PNG', '.'), ('alarme.mp3', '.'), ('foto1.png', '.'), ('foto2.png', '.'), ('foto3.png', '.'), ('foto4.png', '.'), ('foto5.png', '.'), ('foto6.png', '.'), ('foto7.png', '.'), ('foto8.png', '.'), ('foto9.png', '.'), ('foto10.png', '.'), ('foto11.png', '.'), ('foto12.png', '.'), ('foto13.png', '.'), ('foto14.png', '.'), ('foto15.png', '.'), ('foto16.png', '.'), ('foto17.png', '.'), ('foto18.png', '.'), ('foto19.png', '.'), ('foto20.png', '.'), ('foto21.png', '.'), ('foto22.png', '.'), ('foto23.png', '.'), ('foto24.png', '.'), ('foto25.png', '.'), ('foto26.png', '.'), ('foto27.png', '.'), ('foto28.png', '.'), ('foto29.png', '.'), ('foto30.png', '.'), ('foto31.png', '.'), ('foto32.png', '.')],
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
    name='bosstimer',
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
    icon=['ícone.ico'],
)
