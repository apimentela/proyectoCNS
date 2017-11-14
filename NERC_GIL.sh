 #!/bin/bash
 
python3 pre.py "$1"
analyze -f /usr/share/freeling/config/es.cfg < resultadoPre.flg > resultadoFreeling.flg
python3 post.py resultadoFreeling.flg
