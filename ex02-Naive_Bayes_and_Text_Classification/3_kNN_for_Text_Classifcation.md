## 3 kNN for Text Classifcation
The nlp library spacy is used for text preprocessing.

####How do you represent the text?

Text is represented as pre-trained word-vectors from "GloVe". "GloVe is an unsupervised learning algorithm for obtaining vector representations for words" - GloVe.
Spacy provides an easy method to do so:

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
 
Loading spacy...

Spacy loaded.

[-1.84245501e-02  9.53656659e-02 -1.43615901e-01 -6.27929941e-02
  2.72547845e-02  9.27842557e-02  9.23746750e-02  9.48258415e-02
  6.26826808e-02  1.63919079e+00 -1.26975060e-01  1.30534172e-01
 -1.03830837e-01  4.49180370e-03 -6.23999201e-02  5.50583005e-03
 -1.41941309e-01  1.47311163e+00 -1.35884598e-01 -5.21441549e-03
 -5.01364209e-02 -1.20127499e-01 -3.28517169e-01  4.39139418e-02 [...] ]

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

####Example and explanation

```
import spacy


print("Loading spacy...")
nlp = spacy.load("en_core_web_md")
print("Spacy loaded.")

# new data
apples = nlp("I like apples")

# 2 classes
fruit = nlp("I like oranges")
cars = nlp("I like cars")

class_fruit = apples.similarity(fruit)
class_cars = apples.similarity(cars)
print(class_fruit, class_cars)

if class_fruit > class_cars:
    print("\"I like apples\" is classified as fruit.")
if class_cars > class_fruit:
    print("\"I like apples\" is classified as cars.")
if class_cars == class_fruit:
    print("\"I like apples\": both classes are equal likely.")
``` 

Output:


Loading spacy...

Spacy loaded.

0.9421722950109431 0.7834721385720737

"I like apples" is classified as fruit.

Word counting as a word vector is a bad idea because similar documents can have very different vectors in term of distance (length of vector plays a big role).
Cosine similarity doesn't have that effect.
Cosine is monotone declining in the interval of [0, 1/2 pi].
So, the similarity can be directly compared.
Higher values are better.
This approach may have a higher memory complexity because of the pre-trained word vectors which have to be stored.
