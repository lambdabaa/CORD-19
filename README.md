Download the CORD-19 dataset from [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

Clusters
========

### Social Science
- [Pandemics](https://github.com/lambdabaa/CORD-19/blob/master/clusters/16.csv)
- [Public Policy](https://github.com/lambdabaa/CORD-19/blob/master/clusters/6.csv)

### Treatment
- [Case Studies I](https://github.com/lambdabaa/CORD-19/blob/master/clusters/17.csv)
- [Case Studies II](https://github.com/lambdabaa/CORD-19/blob/master/clusters/18.csv)
- [Drug Design](https://github.com/lambdabaa/CORD-19/blob/master/clusters/12.csv)
- [Immunology & Vaccination](https://github.com/lambdabaa/CORD-19/blob/master/clusters/14.csv)
- [Medical Care](https://github.com/lambdabaa/CORD-19/blob/master/clusters/13.csv)

### Epidemiology
- [Epidemiology](https://github.com/lambdabaa/CORD-19/blob/master/clusters/4.csv)
- [Respiratory Illness](https://github.com/lambdabaa/CORD-19/blob/master/clusters/9.csv)
- [Virology](https://github.com/lambdabaa/CORD-19/blob/master/clusters/5.csv)

### Biology

- [Animal Studies](https://github.com/lambdabaa/CORD-19/blob/master/clusters/2.csv)
- [Biochemical Engineering](https://github.com/lambdabaa/CORD-19/blob/master/clusters/3.csv)
- [Cell Biology](https://github.com/lambdabaa/CORD-19/blob/master/clusters/1.csv)
- [Genomics](https://github.com/lambdabaa/CORD-19/blob/master/clusters/7.csv)
- [Microbiology](https://github.com/lambdabaa/CORD-19/blob/master/clusters/19.csv)

### Modeling

- [Mathematical Modeling](https://github.com/lambdabaa/CORD-19/blob/master/clusters/11.csv)

### Transmission, Detection, & Surveillance
- [Transmission](https://github.com/lambdabaa/CORD-19/blob/master/clusters/0.csv)
- [Detection & Surveillance](https://github.com/lambdabaa/CORD-19/blob/master/clusters/8.csv)

### Foreign Language

- [French](https://github.com/lambdabaa/CORD-19/blob/master/clusters/15.csv)
- [German](https://github.com/lambdabaa/CORD-19/blob/master/clusters/10.csv)


Usage
=====

```sh
python3 -m pip install -r requirements.txt
./preprocessing.py  # extract_text()
./preprocessing.py  # extract_titles()
./bpe.sh
./preprocessing.py  # apply_bpe()
./doc2vec.py
./kmeans.py ./docvec > clusters.csv
./preprocessing.py > titles.csv  # extract_titles()
./csvmerge.py > docs.csv
```
