@echo off
echo "%1"
echo "Corriendo pre.py"
python pre.py "%1"
echo "Corriendo no_server.py"
python no_server.py "%1"
echo "Corriendo post.py"
python post.py "%1" "%2"
echo "Terminado"
