#!/bin/bash

 nextflow run nf-core/differentialabundance \
     -params-file ./params.yaml \
     -profile rnaseq,docker \
     -r 1.4.0
