# pull official base image
FROM python:3.7.7-slim

WORKDIR /app
RUN mkdir -p /app/static
RUN mkdir -p /app/media

RUN apt-get update && apt-get install -yq curl wget r-base
RUN R -e "install.packages('jsonlite',dependencies=TRUE, repos='http://cran.rstudio.com/')"

ARG OS_TYPE=x86_64
ARG CONDA_VER=4.5.4 
RUN curl -LO "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh"
RUN bash Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh -p /miniconda -b
RUN rm Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN conda init
RUN conda config --add channels defaults
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda
RUN conda install -c bioconda -y quasitools 
RUN conda config --set auto_activate_base false

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./hivseqdb /app/hivseqdb
ADD ./docker /app/docker

RUN chmod +x /app/docker/hivseqdb/server-entrypoint.sh
RUN chmod +x /app/docker/hivseqdb/worker-entrypoint.sh