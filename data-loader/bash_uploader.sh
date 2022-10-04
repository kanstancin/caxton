
#!/bin/bash

OUTPUT=$(python cax_to_s3_gen.py)

IFS='^' read -ra array <<< "$OUTPUT"

for i in "${array[@]}"; do
  eval "$i"
  echo "***"
done

pwd
