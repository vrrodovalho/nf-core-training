#!/bin/bash

nextflow run nf-core/ampliseq \
    -params-file params.yaml \
    -profile docker \
    -r 2.10.0 \
    --max_cpus 8 \
    --max_memory '16.GB'
