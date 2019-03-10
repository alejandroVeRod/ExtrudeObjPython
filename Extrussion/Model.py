import Face
import Vertex
class Model():
    def __init__(self,obj):
        for vertex in obj.vertexes:
            self.vertexes.append(vertex)
        for face in obj.faces:
            self.faces.append(face)
    def createVertexes(self):
        index=0
        for v in self.vertexes:
            index+=1
            vertex = Vertex(index)
            vertex.setCoordinates(v.x , v.y , v.z)

    def getBoundaryEdges(self):
        pass
