# Instructions

## 1. Install Nextflow

`
curl -s https://get.nextflow.io | bash ; chmod +x nextflow ; sudo mv nextflow /usr/local/bin
`

### Check your Nextflow installation

`
nextflow info
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

## 4. Install Halla

### Install R:

`
sudo apt update
`

`
sudo apt -y upgrade
`

`
sudo apt -y install r-base
`

### Inside R:


Enter R:

`
R
`

Install the packages:

`
install.packages("eva")
`

`
install.packages("XICOR")
`

Exit R:

`
q()
`

### Install Halla

`
pip install halla 
`


## 5. Create pandas environment  


`
mamba create --name pandas python=3.12 pandas -c conda
`

`
mamba activate pandas
`


Run generate_samplesheet.py!


## 6. DIY

Now, use the sequences in *data* to run the pipeline nf-core/ampliseq!
All info you need: https://nf-co.re/ampliseq/2.10.0

