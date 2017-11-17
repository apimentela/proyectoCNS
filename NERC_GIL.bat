@echo off
echo "%1"
echo "Corriendo pre.py"
python pre.py "%1"
echo "Corriendo freeling.py"
python freeling.py "%1"
echo "Corriendo post.py"
python post.py "%1" "%2"
echo "Terminado"
