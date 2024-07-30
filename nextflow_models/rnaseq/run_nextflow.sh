#!/bin/bash

nextflow run nf-core/rnaseq \
    -params-file ./params.yaml \
    -profile docker \
    -r 3.14.0 

    #-resume 
        

