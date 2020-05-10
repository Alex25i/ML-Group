from builtins import print

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
