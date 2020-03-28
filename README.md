Overview
========

Download the CORD-19 dataset from [Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

```sh
python3 -m pip install -r requirements.txt
./preprocessing.py  # extract_text()
./bpe.sh
./preprocessing.py  # apply_bpe()
./doc2vec.py
./kmeans.py ./docvec > clusters.csv
```
