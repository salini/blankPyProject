# -*- mode: python -*-

execfile(SPECPATH+"/common.spec")


exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    name=project_name,
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon=icon_path,
)
