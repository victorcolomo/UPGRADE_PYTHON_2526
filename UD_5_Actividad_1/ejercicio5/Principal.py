
from datetime import date, timedelta

hoy = date.today()
fecha1 = date(2026, 1, 12)
print(fecha1 == hoy)
print(fecha1 < hoy)

manana = hoy + timedelta(days=1)
print(manana)

print((manana - hoy).days)

