def DuplicateResourceError(source: str, id: int):
    # Gestisce errori di duplicazione
    return {f"This resource is already in use! Info: {source}, {id}"}


def LibraryToolsError(source: str, func: str, id: int):
    # Errori comuni, indica:
    # source: dove, quale layer.
    # func: nome funzione da dove viene l'errore
    return {f"Error in layer {source}, in the function {func} using the resource with id {id}"}

