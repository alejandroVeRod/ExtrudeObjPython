class Face():
    def __init__():
        self.index=0
        self.vertexes=[]
        self.normal
    def addVertex(self,vertex):
        self.vertexes.append(vertex)
    def calculateNormal(self):
        p1=np.array([self.vertexes[0].x,self.vertexes[0].y,self.vertexes[0].z],dtype='float32')
        p2=np.array([self.vertexes[1].x,self.vertexes[1].y,self.vertexes[1].z],dtype='float32')
        p3=np.array([self.vertexes[2].x,self.vertexes[2].y,self.vertexes[2].z],dtype='float32')
        normal = np.cross(p2-p1, p3-p1)
        normalArray=[normal[0:3][0],normal[0:3][1],normal[0:3][2]]
        self.normal=normalArray
        