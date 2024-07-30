#!/bin/bash

nextflow run nf-core/ampliseq \
    -params-file params.yaml \
    -profile docker \
    -r 2.8.0
