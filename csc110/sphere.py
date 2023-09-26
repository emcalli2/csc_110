def sphere_volume (radius):
    volume = (4 / 3) * 3.1415 * radius**3
    return round(volume, 2)


def sphere_area(radius):
  area = 4 * 3.1415 * radius**2
  return round(area, 2)

r = 2
v = sphere_volume(r)
a = sphere_area(r)
print (v,a)
