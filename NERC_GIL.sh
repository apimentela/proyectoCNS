 #!/bin/bash

input="$1"
output="$2"

python3 pre.py "$input"
python3 freeling_linux.py "$input"
python3 post.py "$input" "$output"
