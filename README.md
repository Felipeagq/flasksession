# Flask Session
Estas cookies necesitan de una clave segura que debe ser configurada, tambien tendremos un gestor de usuarios

### Llave secreta
````python
app["SECRET_KEY"] = "SOME_SECRET_KEY"
````

### Modificando session
````python
# AGREGAR VALOR A SESSION
session["key"] = value

# EXTRAER VALOR DE SESSION
print(f"{escape(session['key'])}")


# ELIMINAR VALOR DE SESSION
session.pop("key",None)
````

### Crifrado de constraseñas
````python
from werkzeug.security import generate_password_hash, check_password_hash

# GENERAR HASH 
hashed_pw = generate_password_hash(password,method="sha256")

# VERIFICAR HASH 
check_password_hash(hashed_pw, password)
````