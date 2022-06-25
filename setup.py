import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="idosasEfuriosas.py", icon="assets/iconCivic.ico"
)]


cx_Freeze.setup(
    name="Idosas e Furiosas",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)

