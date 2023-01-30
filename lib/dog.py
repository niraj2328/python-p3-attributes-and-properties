#!/usr/bin/env python3

import ipdb

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def get_name(self) -> str:
        return self._name

    def set_name(self, name) -> None:
        if (type(name) == str and len(name) > 1 and len(name) < 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.") 

    def get_breed(self) -> str:
        return self._breed

    def set_breed(self, breed) -> None:
        if(breed in Dog.approved_breeds):
            self._breed = breed;
        else: 
            print("Breed must be in list of approved breeds.")
            

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

# ipdb.set_trace()
