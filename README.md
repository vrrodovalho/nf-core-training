# Instructions

## 1. Install Nextflow

`
curl -s https://get.nextflow.io | bash
chmod +x nextflow
sudo mv nextflow /usr/local/bin
`

### Check your Nextflow installation

`
nextflow info
`

### Check your Nextflow version

`
nextflow -version
`

## 2. Install Mamba 

`
bash mamba/Miniforge3-Linux-x86_64.sh
`

Restart terminal.

## 3. Install nf-core

`
mamba create --name nf-core python=3.12 nf-core nextflow -c bioconda
`

### Activate the Mamba environment for nf-core

`
mamba activate nf-core
`

### Check the pipelines available from nf-core

`
nf-core list
`

## 4. DIY

Now, use the sequences in *data* to run the pipeline nf-core/ampliseq!
All info you need: https://nf-co.re/ampliseq/2.10.0

