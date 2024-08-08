# Instructions

## 0. Create workspace

Open [Gitpod](https://gitpod.io). Use the link of this repository (https://github.com/vrrodovalho/nf-core-training) to create a new workspace.
Then, start typing the commands below.


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

## 4. Create pandas environment  

`
mamba create --name pandas python=3.12 pandas -c conda
`

`
mamba activate pandas
`


## 5. Run Nextflow/nf-core

Now, use the sequences in *data* to run the pipeline nf-core/ampliseq! For that, you need a sample sheet, a metadata file, params files and the nextflow command.

### Samplesheet

To get the samplesheet, run generate_samplesheet.py

`
python generate_samplesheet.py --input data --pattern "(.+)_1(.fq.gz)" --paired False
`

Check samplesheet content.

`
cat samplesheet.tsv
`

Copy samplesheet.tsv file to create a metadata.tsv file.

`
cp samplesheet.tsv metadata.tsv
`

Edit the metadata.tsv file.

`
nano metadata.tsv
`

Edit the file, so that it looks like this:

ID |condition
--- | ---
HB1 | HB 
HB2 | HB 
HB3 | HB 
N1 | N 
N2 | N 
N3 | N 

After editing the file, use ctrl + X to save. Type Y and Enter to confirm.

Also get the models in nextflow_models directory.

`
cp nextflow_models/ampliseq-training/params.yaml .
`

`
cp nextflow_models/ampliseq-training/run_nextflow.sh .
`

Now that you have all the files in the current directory, run nextflow:

`
bash run_nextflow.sh
`

All other info you need: https://nf-co.re/ampliseq/2.10.0


## 6. Halla (optional)

If you also want to install and run Halla, follow the instructions below.


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

### Run Halla


Now, inside the halla directory, use the halla_command.sh to run Halla.

`
bash halla_command.sh 
`

That's it! Congratulations!
