import objLoader
import Model
import Face
import Vertex
import sys


obj =objLoader.ObjLoader()
obj.load_model('Extrussion/CubeTriangulate.obj')
model=Model()
d=10

# file = open('result.obj',"w") 

# for vertex in obj._vertex:
#     file.write("v {0} {1} {2}\n".format(vertex[0],vertex[1],vertex[2]))
# for faces in objloader._faces:
#     file.write("f {0} {1} {2}\n".format(faces[0],faces[1],faces[2]))


 
# file.close() 

print('')