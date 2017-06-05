
block_cipher = None

data = [
    ('../myProject/widgets/ui', 'myProject/widgets/ui'),
    ("../myProject/resources/project_logo.ico",  "myProject/resources/"),
]

icon_path=SPECPATH+"/../myProject/resources/project_logo.ico"
project_name="myProject"

hiddenimports=[
    'atexit',
]


analysis = Analysis(
    ['../scripts/main.py'],
    pathex=[SPECPATH+"/../"],
    binaries=None,
    datas=data,
    hiddenimports=hiddenimports,  
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(
    analysis.pure,
    analysis.zipped_data,
    cipher=block_cipher
)