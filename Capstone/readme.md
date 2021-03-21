
## Transformer based model to write python code

Goal : From the raw input file which contains English text and python code, curate a dataset and train a transformer model which can predict python code from the input text.

### Dataset Curation [code](https://github.com/sridevibonthu/END/blob/main/Capstone/END_Dataset_Curation.ipynb)

The initial dataset given is [here](https://drive.google.com/file/d/1rHb0FQ5z5ZpaY2HpyFGY6CeyDG0kTLoO/view) which is both english text and python code as text file. This file can not be used directly for training the model. It needs lot of preprocessing.

Observation on the given input file by manual inspection and some EDA :

* Some of the code snippets are repeated.
* All source code snippets are of varying sizes ranging from 25 characters to 7000 characters.
* my initial thought was to use the lines which start with # (comment) as English Text and the rest as python code. But I have observed that there are lot of source codes contain lot of comments. These should be properly handled to separate questions and source code.
* Few of the snippets are as it is copied from some other source

Final Dataset creation
* Removed all the blank lines, After removing all the blanks, we have 32994 lines in our input file.
* Captured all the line numbers of english text (Comments whose length is more than 25 and those which do not have comments on top or below of it)
* From the English text line numbers, captured the source code in between those line numbers. Total identified english text and source code pairs are 4325 and a sample pair is shown below.
``` 
data[3]

['write a program to find and print the largest among three numbers',
 "num1 = 10\nnum2 = 12\nnum3 = 14\nif (num1 >= num2) and (num1 >= num3):\n   largest = num1\nelif (num2 >= num1) and (num2 >= num3):\n   largest = num2\nelse:\n   largest = num3\nprint(f'largest:{largest}')\n"]
```
* Ths statistics of these pairs is little amazing. Maximum text length is 309 and average length is only 68, Maximum source code length is 7199 characters, where as average is 129. 
* There are many source code snippets, whose length is less than 20 characters, but they are looking meaningfull. Someof them are shown below.
```
1. print("")\n
2. a=6\nprint(bin(a))\n
3. a,b = b,a\n
```
* Removed those records whose code length is exceeding 1000 characters. Now, the number of records are 4299.
* Saved them into a csv file and it is found [here](https://github.com/sridevibonthu/TSAI_END_P1/blob/main/Capstone/TexttoPython2.csv). 

### Word Embeddings for Python Code [Code](https://github.com/sridevibonthu/END/blob/main/Capstone/traingwordembeddings.ipynb)

* For this problem, Source is an english text and target is a python source code. regular embeddings created using nn.Embeddings or pre-trained word vectors are enough for the source sequence. Coming to target, nn.Embeddings can only train on the dataset. But most of the vocabulary is set of identifiers used in the code and not part of python tokens like keywords, special characters etc.
* With this intuition, I have trained code embeddings by using Gensim library and [conala-corpus](http://www.phontron.com/download/conala-corpus-v1.1.zip).
* Regular spacy tokenizer is not helping with Python code. Adopted the following method from a library to tokenize python code.
```
def getTokenizer(python_code):
    '''
    Function that returns tokenized python code
    :return: tokenized code
    '''
    tokens = []
    try:
        a = list(tokenize(BytesIO(python_code.encode('utf-8')).readline))
        #print(a)
        for i__ in a[1:-1]:
            if i__.exact_type == 3:
                string_tokens = [k__ for k__ in i__[1]]
                tokens = tokens + string_tokens
            else:
                tokens.append(i__[1])
    except Exception:
        print("Error in tokenization")

    return tokens
 ```
 and it worked well.
 ```
 getTokenizer('for i in range(10):\n    print(i)')
 ['for',  'i', 'in',  'range', '(', '10', ')', ':', '\n', '    ', 'print', '(', 'i', ')', '', '']
 
 * Care taken to check whether all space strings are multiple of four or not.
 * With the help of Word2Vec class from gensim.models trained the code embeddings and saved as vectors.kv keyed vectors file.
 
### Model

### Sample Results
The applications of neural machine translation (NMT) to programming languages have been limited
so far, mainly because of the lack of parallel resources available in this domain.
