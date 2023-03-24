from datetime import date

# 1. Imprimir
print("Hello, world!")

# 2. Variables
sum = 1 + 2
product = sum * 2
print("Producto:", product)

# 3. Tipos de datos
planets_in_solar_system = 8  #  int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367  #  float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11"  # string

print("planets_in_solar_system:", type(planets_in_solar_system))
print("distance_to_alpha_centauri:", type(distance_to_alpha_centauri))
print("can_liftoff:", type(can_liftoff))
print("shuttle_landed_on_the_moon:", type(shuttle_landed_on_the_moon))

# 4. Operadores aritméticos
1 + 1  # 2
1 - 2  # -1
10 / 2  # 5
2 * 2  # 4

# 5. Operadores de asignación
x = 2  # Asiganción - x: 2
x += 7  # Incremento - x: 9
x -= 1  # Reducción - x: 8
x /= 2  # División - x: 4
x *= 3  # Multiplicación - x: 12
print("x:", x)

# 6. Fechas
print(date.today())

# 7. Conversión de tipos de datos
print("Today's date is: " + str(date.today()))
