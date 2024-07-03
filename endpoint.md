# Documentación de Endpoints

## Autenticación

### Registro de Usuarios
**Ruta**: /auth/registro
**Método**: POST

**Descripción**:  
Registra un nuevo usuario en el sistema.

**Parámetros de entrada**:
- username: Nombre de usuario (string)
- password: Contraseña (string)
- role: Rol del usuario (string) [Cliente, Empleado]

**Parámetros de salida**:
- status: Código de estado HTTP
- message: Mensaje adicional (string)

### Login de Usuarios
**Ruta**: /auth/login  
**Método**: POST

**Descripción**:  
Autentica a un usuario y genera un JWT.

**Parámetros de entrada**:
- username: Nombre de usuario (string)
- password: Contraseña (string)

**Parámetros de salida**:
- status: Código de estado HTTP
- access_token: Token JWT (string)
- message: Mensaje adicional en caso de error (string)

## Gestión de Habitaciones

## Crear habitación
### Ruta:  /api/habitaciones
### Método: POST
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Crea una nueva habitación.

**Parámetros de entrada:**
- `numero`: Número de la habitación.
- `precio_por_dia`: Precio por día de la habitación.

**Parámetros de salida:**
- `status`: 201 si la creación fue exitosa, 400 si hubo algún error de validación, 500 en caso de error del servidor.
- `message`: Información adicional sobre el resultado de la operación.

---

## Eliminar habitación
### Ruta: /api/habitaciones/<int:id>
### Método: DELETE
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Elimina una habitación existente.

**Parámetros de entrada:**
- `id`: ID de la habitación a eliminar.

**Parámetros de salida:**
- `status`: 200 si la eliminación fue exitosa, 404 si la habitación no fue encontrada.
- `message`: Información adicional sobre el resultado de la operación.

---

## Actualizar habitación
### Ruta: /api/habitaciones/<int:numero>
### Método: PUT
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Actualiza los detalles de una habitación existente.

**Parámetros de entrada:**
- `numero`: Número de la habitación.
- `precio_por_dia` (opcional): Nuevo precio por día de la habitación.
- `activa` (opcional): Estado de la habitación.

**Parámetros de salida:**
- `status`: 200 si la actualización fue exitosa, 400 si hubo algún error de validación, 404 si la habitación no fue encontrada.
- `message`: Información adicional sobre el resultado de la operación.

---

## Obtener habitaciones
### Ruta: /api/habitaciones
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Obtiene una lista de todas las habitaciones.

**Parámetros de entrada:**
Ninguno.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa.
- `data`: Lista de habitaciones.

---

## Obtener habitación por número
### Ruta: /api/habitaciones/<int:numero>
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Obtiene los detalles de una habitación por su número.

**Parámetros de entrada:**
- `numero`: Número de la habitación.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa, 404 si la habitación no fue encontrada.
- `data`: Detalles de la habitación.

---

## Buscar habitaciones por rango de fechas
### Ruta: /api/habitaciones/buscar
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Busca habitaciones disponibles en un rango de fechas.

**Parámetros de entrada:**
- `fecha_inicio`: Fecha de inicio en formato YYYY-MM-DD.
- `fecha_fin`: Fecha de fin en formato YYYY-MM-DD.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa, 400 si hubo algún error de validación.
- `data`: Lista de habitaciones disponibles.

---

## Buscar habitaciones por precio máximo
### Ruta:  /api/habitaciones/precio_menor
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Busca habitaciones con un precio por día menor o igual al precio máximo especificado.

**Parámetros de entrada:**
- `precio_max`: Precio máximo.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa, 400 si hubo algún error de validación.
- `data`: Lista de habitaciones que cumplen con el criterio.

---

## Disponibilidad de habitaciones por día
### Ruta: /api/habitaciones/disponibilidad_dia
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Obtiene la disponibilidad de habitaciones para una fecha específica.

**Parámetros de entrada:**
- `fecha`: Fecha en formato YYYY-MM-DD.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa, 400 si hubo algún error de validación.
- `data`: Lista de habitaciones con su estado (Disponible/Ocupada).

---

## Crear reserva
### Ruta: /api/reservas
### Método: POST
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Crea una nueva reserva.

**Parámetros de entrada:**
- `habitacion_numero`: Número de la habitación.
- `fecha_inicio`: Fecha de inicio en formato YYYY-MM-DD.
- `fecha_fin`: Fecha de fin en formato YYYY-MM-DD.

**Parámetros de salida:**
- `status`: 201 si la creación fue exitosa, 400 si hubo algún error de validación, 500 en caso de error del servidor.
- `message`: Información adicional sobre el resultado de la operación.

---

## Obtener reservas
### Ruta: /api/reservas
### Método: GET
### Autorización: Bearer [aqui pones el JWT Token, sin los [],  y separado del bearer]

**Descripción:**
Obtiene una lista de todas las reservas.

**Parámetros de entrada:**
Ninguno.

**Parámetros de salida:**
- `status`: 200 si la operación fue exitosa.
- `data`: Lista de reservas.

---