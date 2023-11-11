# HIVSeqDB

[![](https://img.shields.io/badge/uses-docker-orange)](https://docs.docker.com/get-docker)
[![](https://img.shields.io/badge/uses-conda-yellowgreen)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
[![](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Twitter Follow](https://img.shields.io/twitter/follow/alfred_ug.svg?style=social)](https://twitter.com/alfred_ug) 

## Introduction

Portable resource for management and analysis of NGS-based HIV Drug Resistance Data. Secure management of uploaded NGS data, matched with sample data. HIVseqDB provides a searchable database protected through user authentication. NGS-based HIVDR data is asynchronously analysed using state of the art tools. Results are given off in user friendly pages and exportable in various formats. HIVseqDB can be deployed on different computing environments. It is distributed with guidelines for setting it up for on-prem and cloud-based compute solutions. A quick demonstration of HIVseqDB in production is available at [https://hivseqdb.org/](https://hivseqdb.org/).

## Quick installation

HIVseqDB requires **docker** to pull and run the containerised services, if you have docker available, proceed to next steps. Otherwise, install it from [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/).

Download HIVseqDB from GitHub.
```bash
git clone https://github.com/AlfredUg/hivseqdb-docker.git
cd hivseqdb-docker
```

First, build HIVseqDB using the `docker-compose` command.

```bash
sudo docker-compose build
```

Secondly, run all the containers.

```bash
sudo docker-compose up
```

If everything looks good, deploy HIVseqDB.

```bash
sudo docker-compose up --build -d
```

The server will be running at: [http://127.0.0.1](http://127.0.0.1). We are almost there. We need to set up the database and create a super user, which we can do by interactively running the server container of HIVseqDB.

```bash
sudo docker exec -it hivseqdb-docker_server_1 bash
```

Create a super user for the admin role.

```bash
python manage.py createsuperuser
```

## Usage

Below is a quick video of the HOW-TOs of HIVseqDB. 

NOTE: The NGS data used in this demonstration is publically available at the NCBI Sequence Read Archive (SRA) and the European Nucleotide Archive (ENA), Bioproject accession PRJNA340290. Corresponding sample data was obtained from the associated publication. Many thanks to Avila-Ríos, Santiago, et al. "HIV drug resistance in antiretroviral treatment-naïve individuals in the largest public hospital in Nicaragua, 2011-2015." PLoS One 11.10 (2016): e0164156.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/JFPegaIcD7w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Test data

To demonstrate the usage of HIVseqDB, download real HIV-1 NGS data from the European Nucleotide Archive (ENA), Bioproject accession PRJNA340290. 

```bash
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR407/007/SRR4071737/SRR4071737_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR407/007/SRR4071737/SRR4071737_2.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR407/008/SRR4071738/SRR4071738_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR407/008/SRR4071738/SRR4071738_2.fastq.gz
gunzip *.gz
```

Get corresponding sample data from the associated publication. Again, many thanks to Avila-Ríos, Santiago, et al. We use the formatted version of the data, but the original file is available [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0164156#sec024).

```bash
wget https://github.com/AlfredUg/hivseqdb-docker/raw/main/data/Santiago_Nicagura_2016.csv
```

Follow the instructions as demonstrated in the video to upload, analyse and browse.

## Dependancies

Below is the list of key tools that are used by HIVseqDB. See `requirements.txt` for other dependancies.

Web, server, data management
+ [Django](#)
+ [Redis](#)
+ [Celery](#)
+ [Postgres](#)
+ [Nginx](#)
+ [Gunicorn](#)

HIVseqDB UI/UX
+ [Data tables](#)
+ [Bootstrap](#)
+ [Highcharts](#)

Analysis of HIV drug resistance
+ [Quasitools](https://phac-nml.github.io/quasitools/)
+ [Sierra-local](https://github.com/PoonLab/sierra-local)
+ R package, Jsonlite

## Troubleshooting

Kindly report any issues at [https://github.com/AlfredUg/hivseqdb-docker/issues](https://github.com/AlfredUg/hivseqdb-docker/issues).

## License

HIVseqDB is licensed under GNU GPL v3.

## Citation

**This work is currently under peer review. A formal citation will be availed in due course.**
