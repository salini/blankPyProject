# -*- mode: python -*-

execfile(SPECPATH+"/common.spec")


exe = EXE(
    pyz,
    analysis.scripts,
    exclude_binaries=True,
    name=project_name,
    debug=False,
    strip=False,
    upx=True,
    console=True,
    icon=icon_path,
)

coll = COLLECT(
    exe,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    strip=False,
    upx=True,
    name=project_name
)
