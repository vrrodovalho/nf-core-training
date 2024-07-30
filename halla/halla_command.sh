#!/bin/bash


halla_input1=metabolomics.csv
halla_input2=taxonomy.csv

echo -ne "\n\n>>> Computing ${files[$idxA]} x ${files[$idxB]} associations for group ${group}...\n\n"
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
    -o output_${group}_${files[$idxA]}_x_${files[$idxB]}
