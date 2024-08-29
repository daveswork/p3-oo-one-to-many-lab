class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        my_pets = []
        for pet in Pet.all:
            print(pet.owner.name)
            if pet.owner.name == self.name:
                my_pets.append(pet)
        return my_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
    
    def get_sorted_pets(self):
         sorted_list = sorted(Pet.all, key=lambda x: x.name)
         return sorted_list