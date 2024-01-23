#!/usr/bin/env python3

class MyString:
  def __init__(self,property=""):
    self.property = property

  def get_property(self):
    return self._property
  
  def set_property(self, new_property):
    if type(new_property) == str:
      self._property = new_property
    print("The value must be a string.")

  #returns True
  def is_sentence(self):
    if self._property[-1] == ".":
      return True
    return False
  
  #s_question()
  def is_question(self):
    if self._property[-1] == "?":
      return True
    return False
  
  # is_exclamation
  def is_exclamation(self):
    if self._property[-1] == "!":
      return True
    return False
  
  # count_sentences
  def count_sentences(self):
    checker = ["?","!"]
    value = self._property
    for fullstop in checker:
      value = value.replace(fullstop, ".")
      
    print(value)

    number = 0
    list_of_sentence = [broken_sentence.strip() for broken_sentence in value.split(".")]
    for word_count in list_of_sentence:
      if word_count != "":
        number += 1
    return number
    
  property =property(get_property, set_property)

mystring = MyString()  
mystring.property = "This is a string! It has three sentences. Right?"
mystring.count_sentences()


