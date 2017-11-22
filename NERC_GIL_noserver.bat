@echo off
echo "%1"
echo "Corriendo pre.py"
python C:\freeling\bin\pre.py "%1"
echo "Corriendo no_server.py"
python C:\freeling\bin\no_server.py "%1"
echo "Corriendo post.py"
python C:\freeling\bin\post.py "%1" "%2"
echo "Terminado"
