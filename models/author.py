class Author:
    def __init__(self, name):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'<Author {self.name}>'
    
    # -----> Getting the property then later on setting it.
        
    @property
    def name(self): 
        return self._name  # Return the private _name attribute
    
    # -----> Setting the conditions that a name should be a type string and more than 0 characters
    @name.setter
    def name(self, name): 
        if isinstance(name, str) and len(name) > 0: 
            if hasattr(self, '_name'):
                raise AttributeError("Name cannot be changed after initialization.")
            self._name = name
        else: 
            raise ValueError("Names must be of type string")
