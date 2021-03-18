import dist
import indexer
# Method to find distance between any two stations:
def distance(origin,destination):
    x=indexer.indexer(origin)
    y=indexer.indexer(destination)
    return dist.dist[x][y]