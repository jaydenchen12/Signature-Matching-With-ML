# Signature-Matching-With-Tensorflow

Signature verification through handwriting analysis is one of the most common tasks in forensic document analysis. It is very important to compare questioned writing/signatures with the genuine one, when it comes to data protection and identity management. We are utilizing machine learning techniques to perform handwriting analysis by matching images of a questioned handwriting with the genuine ones to authenticate writing/signatures. Machine Learning algorithms will adapt and improve their performance as the number of handwriting samples increase for learning and do more accurate analysis.

Tech Stack:
Python
Flask
Tensorflow
MongoDB backend
Objectstore

To run the pipeline do the following in order

```bash
cd  /rabbitmq
chmod 755 start.sh
./start.sh

cd ../mongo
chmod 755 build-run.sh
./build-run.sh

cd ../model
chmod 755 *
./start.sh

cd ../api
chmod 755 *
./build.sh
./start.sh
```
