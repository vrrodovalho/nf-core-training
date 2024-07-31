#!/bin/bash


halla_input1=metabolomics.csv
halla_input2=taxonomy.csv

echo -ne "\n\n>>> Computing ${halla_input1} x ${halla_input2} associations...\n\n"
halla \
    -y ${halla_input1} \
    -x ${halla_input2} \
    -m spearman \
    --hallagram \
    --clustermap \
    --fdr_method fdr_bh \
    --fdr_alpha 0.05 \
    -n -1 \
    --diagnostic_plot \
    -o output_${halla_input1}_x_${halla_input2}
