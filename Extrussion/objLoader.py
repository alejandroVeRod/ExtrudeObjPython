#!/usr/local/bin/python3

import numpy as np
class Vertex:
    def __init__(self,x,y,z):
        self.id=0
        self.x=x
        self.y=y
        self.z=z
class Face:
    
    def __init__(self):
        self.id=0
        self.vertexes=[]
        self.normal=[]
    def add_vertex(self,vertex):
        self.vertexes.append(vertex)
    def calculateNormal(self):
        p1=np.array([self.vertexes[0].x,self.vertexes[0].y,self.vertexes[0].z],dtype='float32')
        p2=np.array([self.vertexes[1].x,self.vertexes[1].y,self.vertexes[1].z],dtype='float32')
        p3=np.array([self.vertexes[2].x,self.vertexes[2].y,self.vertexes[2].z],dtype='float32')
        normal = np.cross(p2-p1, p3-p1)
        normalArray=[normal[0:3][0],normal[0:3][1],normal[0:3][2]]
        self.normal=normalArray

class ObjLoader:
    def __init__(self):
        self.vert_coords = {}
        self.face_index = {}
        self.model = []

    def load_model(self, file):
        indexVertex=0
        indexFace=0
        for line in open(file, 'r'):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue

            if values[0] == 'v':
                indexVertex+=1
                v=Vertex(values[1],values[2],values[3])
                v.id=indexVertex
                self.vert_coords[indexVertex]=v
            if values[0] == 'f':
                indexFace+=1
                f=Face()
                f.id=indexFace
                for v in values[1:4]:
                    f.add_vertex(self.vert_coords[int(v)])
                f.calculateNormal()
                self.face_index[indexFace]=f    
                    

