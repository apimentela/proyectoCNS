@echo off
for %%i in (crw_txts_1_depth\*) do (
echo "%%i"
echo "Corriendo pre.py con %%i..."
python pre.py "%%i"
echo "Corriendo freeling.py"
python freeling.py resultadoPre.flg
echo "Corriendo post.py"
python post.py resultadoFreeling.flg
echo "Terminado"
)
