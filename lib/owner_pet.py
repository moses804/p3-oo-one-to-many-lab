class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of this owner's pets."""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign this owner to the pet."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")

        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

        # If owner passed in
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            owner.add_pet(self)

        Pet.all.append(self)
