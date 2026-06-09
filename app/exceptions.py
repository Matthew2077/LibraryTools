class LibraryToolsError(Exception):
    """Eccezione base del progetto"""
    pass

# SAVE CAN'T SAVE AN OBJECT WITH A UNIQUE VALUE TWO TIMES 
class DuplicateResourceError(LibraryToolsError):
    # source: dove, quale layer.
    # id: id oggetto manipolato
    def __init__(self, source: str, id: int):
        super().__init__(f"This resource is already in use! Info: {source}, {id}")
        self.source = source
        self.id = id

# DELETE HAD AN OBJECT THAT DOESN'T EXIST
class ResourceNotFoundError(LibraryToolsError):
    def __init__(self, resource_type: str, id: int):
        super().__init__(f"This resource does not exist! Info: {resource_type}, {id}")
        self.resource_type = resource_type
        self.id = id

class UnableToUpdateThisResource(LibraryToolsError):
    def __init__(self, resource_type: str, id: int):
        super().__init__(f"Unable to update the required resource. Info: {resource_type}, {id}")
        self.resource_type = resource_type
        self.id = id
        
# SERVICES LAYER 
class NoValuesFound(LibraryToolsError):
    def __init__(self, resource_type: str):
        super().__init__(f"Unable to find any resource of this type. Resource type: {resource_type}")
        self.resource_type = resource_type
