 #!/bin/bash

input="$1"
output="$2"

python3 pre.py "$input"
analyze -f /usr/share/freeling/config/es.cfg < "${input}_resultadoPre.flg" > "${input}_resultadoFreeling.flg"
python3 post.py "$input" "$output"
