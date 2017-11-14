@echo off
echo "%1"
echo "Corriendo pre.py con texto %1"
python pre.py "%1"
echo "Corriendo no_server.py"
python no_server.py resultadoPre.flg
echo "Corriendo post.py"
python post.py resultadoFreeling.flg
echo "Terminado"
