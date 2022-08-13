from ursina import *
from math import *

app = Ursina()

vertices = []

connecting = []

rx = 40

rz = 40

for x in range(rx):
    for z in range(rz):
        fy = sin(x) + sin(z)
        vertices.append((x,fy,z))

#print(len(vertices))
#print(len(vertices) / rz)


for x in range(1,rx):
    for y in range(rz - 1):
        values = ((rz * x - rz) + y,(rz * x) + y, (rz * x + 1) + y)
        valuesreverse = ((rz * x + 1) + y,(rz * x) + y,(rz * x - rz) + y)
        values2 = ((rz * x - rz) + y, (rz * x - rz) + 1 + y, (rz * x) + 1 + y)
        valuesreverse2 = ((rz * x) + 1 + y, (rz * x - rz) + 1 + y,(rz * x - rz) + y)
        print(values2)
        connecting.append(values)
        connecting.append(valuesreverse)
        connecting.append(values2)
        connecting.append(valuesreverse2)




mesh = Mesh(vertices=vertices,triangles=connecting)


## dummy points
mesh2 = Mesh(vertices=vertices,mode="point", thickness=10)

entity = Entity(model=mesh, color=color.orange)

## dummy points put into scene
entity2 = Entity(model=mesh2, color=color.yellow)

### these were my testing points

x = 1



point = Entity(model="sphere", scale=0.1, color=color.red, position=vertices[x - 1])

point2 = Entity(model="sphere", scale=0.1, color=color.red, position=vertices[rz * x])

point3 = Entity(model="sphere", scale=0.1, color=color.red, position=vertices[rz * x + 1])

#point4 = Entity(model="sphere", scale=0.2, color=color.blue, position=vertices[0])

#point5 = Entity(model="sphere", scale=0.2, color=color.blue, position=vertices[1])

#point6 = Entity(model="sphere", scale=0.2, color=color.blue, position=vertices[3])

EditorCamera()

app.run()
