@echo off
for %%a in (crw_txts_1_depth\*) do (
echo "%%a"
echo "python pre.py %%a"
python pre.py "%%a" >> resultadoCorreos.txt
echo "Terminado"
)