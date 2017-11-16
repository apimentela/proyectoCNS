@echo off
echo "%1"
echo "Corriendo pre.py con texto %1"
python pre.py "%1"
echo "Corriendo freeling.py"
python freeling.py resultadoPre.flg
echo "Corriendo post.py"
python post.py resultadoFreeling.flg
echo "Terminado"
