from .database import Base, engine
from .models import User, Note, Tag, Category


# questo file serve per gli import
# Metodo 1 nei file lasciando init vuoto: from .core.models import User 
# Metodo 2: metti in init from .models import User e poi nel file fai from models import User
# PS dipende dalla path btw

