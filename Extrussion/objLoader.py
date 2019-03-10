import numpy as np
class ObjLoader:
    def __init__(self):
        self.vert_coords = []
        self.vertex_index = []
        self.model = []

    def load_model(self, file):
        indexVertex=0
        indexFace=0
        for line in open(file, 'r'):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue

            if values[0] == 'v':
                self.vert_coords.append(values[1:4])
            if values[0] == 'f':
                face_i=[]
                for v in values[1:4]:
                    face_i.append(v)
                self.vertex_index.append(face_i)

    
    def createModel(self,file):
        pass
