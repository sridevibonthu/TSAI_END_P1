
## Transformer based model to write python code

Goal : From the raw input file which contains English text and python code, curate a dataset and train a transformer model which can predict python code from the input text.

### Dataset Curation

The initial dataset given is here https://drive.google.com/file/d/1rHb0FQ5z5ZpaY2HpyFGY6CeyDG0kTLoO/view which is both english text and python code as text file. This file can not be used directly for training the model. It needs lot of preprocessing.

Observation on the given input file by manual inspection and some EDA :

* Some of the code snippets are repeated.
* All source code snippets are of varying sizes ranging from 25 characters to 7000 characters.
* my initial thought was to use the lines which start with # (comment) as English Text and the rest as python code. But I have observed that there are lot of source codes contain lot of comments. These should be properly handled to separate questions and source code.
* Few of the snippets are as it is copied from some other source

Final Dataset creation
* Removed all the blank lines, After removing all the blanks, we have 32994 lines in our input file.
* Captured all the line numbers of english text (Comments whose length is more than 25 and those which do not have comments on top or below of it)
* From the English text line numbers, captured the source code in between those line numbers. Total identified english text and source code pairs are 4326 and a sample pair is shown below.
* ``` data[3] ```
* 
* 

xt



### Word Embeddings for Python Code

### Model

### Sample Results
The applications of neural machine translation (NMT) to programming languages have been limited
so far, mainly because of the lack of parallel resources available in this domain.
