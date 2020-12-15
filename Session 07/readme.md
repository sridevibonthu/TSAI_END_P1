## Session 07

Sentiment Analysis on Stanford Data [here](https://github.com/sridevibonthu/TSAI_END_P1/blob/main/Session%2007/Sentiment_Analysis_on_stanford_data_using_LSTM_RNN.ipynb)

* maximum accuracy achieved with two labels - 71.5 %   [code](https://github.com/sridevibonthu/TSAI_END_P1/blob/main/Session%2007/binary_labels_Sentiment_Analysis_on_stanford_data_using_LSTM_RNN.ipynb)

* maximum accuracy achived with 5 labels - 36.25%

#### Code for applying Augmentations
```
def augment(text):
  rate = random.random()
  #print(rate, end=' ')
  if rate<0.2:
    text = random_deletion(text)
  elif rate<0.45:
    text = random_swap(text)
  elif rate<0.5:
    text = list(googletranslate(text).split(' '))
  return text
  
  ```
  #### to apply augmentation only for training data
  ```
  for i in range(len(train)):
  train.examples[i].sentence = augment(train.examples[i].sentence)
  ```

Observations :
Accuracy using LSTM
bidirectional LSTM
using GRU
bidirectional GRU
