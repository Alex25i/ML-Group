## 3 kNN for Text Classifcation
The nlp library spacy is used for text preprocessing.

####How do you represent the text?

Text is represented as pre-trained word-vectors from "GloVe". "GloVe is an unsupervised learning algorithm for obtaining vector representations for words" - GloVe.
Spacy provides an easy meathod to do so:

```
import spacy

print("Loading spacy...")
nlp = spacy.load("en_core_web_md")
print("Spacy loaded.")

doc = nlp("GloVe is an unsupervised learning algorithm for obtaining vector representations for words")

if doc.has_vector:
    print(doc.vector) 
```

Output: 
[-1.84245501e-02  9.53656659e-02 -1.43615901e-01 -6.27929941e-02
  2.72547845e-02  9.27842557e-02  9.23746750e-02  9.48258415e-02 [...]
]

This vector has 300 dimensions.

####What distance function do you use?

The cosine similarity is used as a distance fuction.
Here, Spacy is offering a easy-to-use function, too:

```
apples = nlp("I like apples")
oranges = nlp("I like oranges")
apples_oranges = apples.similarity(oranges)
print(apples_oranges)
```

####What decision rule do you use?
Choose the class which has the most of the k-nearest neighbors (in sense of cosine similarity).
In case of a draw choose the class with the lowest overall cosine similarity.

####Example and explaination
TODO
