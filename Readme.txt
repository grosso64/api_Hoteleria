#Español
# Hotel Management API


## Instalación



1. Instalar las dependencias:

    pip install -r requirements.txt


2. Configurar la base de datos en el archivo `klapi.py`.


    

3. Ejecutar la aplicación:
   
    gunicorn app:app  # Para wsl con ubuntu(instalar dependecias de requirements.txt en el wsl)
 
   

## Uso

- **Registro**: `/auth/registro` (POST)
- **Login**: `/auth/login` (POST)
- **Crear Habitación**: `/api/habitaciones` (POST)
- **Eliminar Habitación**: `/api/habitaciones/<int:id>` (DELETE)
- **Actualizar Habitación**: `/api/habitaciones/<int:numero>` (PUT)
- **Buscar Habitaciones**: `/api/habitaciones` (GET)
- **Buscar Habitaciones por Rango de Fechas**: `/api/habitaciones/buscar` (GET)
- **Buscar Habitaciones por Precio**: `/api/habitaciones/precio_menor` (GET)
- **Buscar Disponibilidad de Habitaciones por Día**: `/api/habitaciones/disponibilidad_dia` (GET)
- **Reservar Habitación**: `/api/reservas` (POST)
- **Listar Reservas**: `/api/reservas` (GET)

## Integrantes del Grupo
- Denis Grosso
-------------------------------------------------------------------------------------------------------------
#English
#Hotel Management API


## Facility



1. Install the dependencies:

    pip install -r requirements.txt


2. Configure the database in the `klapi.py` file.


    

3. Run the application:
   
    gunicorn app:app # For wsl with ubuntu (install dependencies from requirements.txt in wsl)
 
   

## Use

- **Registration**: `/auth/registration` (POST)
- **Login**: `/auth/login` (POST)
- **Create Room**: `/api/rooms` (POST)
- **Delete Room**: `/api/rooms/<int:id>` (DELETE)
- **Update Room**: `/api/rooms/<int:number>` (PUT)
- **Search Rooms**: `/api/rooms` (GET)
- **Search for Rooms by Date Range**: `/api/rooms/search` (GET)
- **Search Rooms by Price**: `/api/rooms/price_lower` (GET)
- **Search for Room Availability by Day**: `/api/rooms/availability_day` (GET)
- **Reserve Room**: `/api/reservas` (POST)
- **List Reservations**: `/api/reservas` (GET)

## Group members
-Denis Grosso

