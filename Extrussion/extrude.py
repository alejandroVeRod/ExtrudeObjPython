import objLoader
import sys
obj =objLoader.ObjLoader()
obj.load_model('CubeTriangulate.obj')

d=10


vertex_array=[]
#WHAT THE HEcK ude how d i continu?
for key,val in obj.vert_coords:
    vertex_array.append(val)





# file = open('result.obj',"w") 

# for vertex in obj._vertex:
#     file.write("v {0} {1} {2}\n".format(vertex[0],vertex[1],vertex[2]))
# for faces in objloader._faces:
#     file.write("f {0} {1} {2}\n".format(faces[0],faces[1],faces[2]))


 
# file.close() 

print('')