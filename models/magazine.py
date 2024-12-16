class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    # -----> Getting the property
    @property
    def name(self): 
        return self._name
    
    # -----> Setting the name so that a new author can be created according to the conditional statements.
    @name.setter
    def name(self, name): 
        if isinstance(name, str) and 2 <= len(name) <= 16: 
            self._name = name
        else: 
            raise ValueError("Names must be between 2 and 16 characters")
    
    # -----> Getting the property and later setting it
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0: 
            self._category = category
        else:
            raise ValueError("Categories should be more than 0 characters")
