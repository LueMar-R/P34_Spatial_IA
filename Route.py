import Graph

class Route:
    """Cette classe sert à générer une route traversant tous les lieux d'un graph."""

    def __init__(self, graph):
        noeuLu = Graph.Graph.matrice_od
        noeuA = noeuLu.iat[0, 0]
        self.ordre = [noeuA]
        while not(noeuLu.empty):
            # print("noeuAct ={}".format(noeuAct))
            # print("noeuLu =\n{}\n".format(noeuLu))
            noeuB = graph.plus_proche_voisin(noeuA, noeuLu)
            noeuLu = noeuLu[noeuLu['LieuA'] != noeuA]
            noeuLu = noeuLu[noeuLu['LieuB'] != noeuA]
            self.ordre.append(noeuB)
            noeuA = noeuB

    def __repr__(self):
        return "<Route : taille = {}>".format(len(self.ordre))

    def __str__(self):
        return "{}".format(self.ordre)

    def calcul_distance_route(self):
        i = 0
        d = 0
        for noeud in self.ordre:
            if i == 0:
                noeudA = noeud
            else:
                noeudB = noeud
                d += noeudA.distance(noeudB)
                noeudA = noeudB
            i += 1
        return d

    
# # Cette fonction renvoie le plus court chemin dans le graphe passant par tous les nœuds.
# def voyageurCommerce(graph, codeSource) :

#     # Nous stockons le meilleur chemin ici
#     meilleureLongueur = float("inf")
#     meilleurChemin = None

#     # Ainsi, la fonction prend en argument les nœuds qui ne sont pas encore visités, le graphe et une position courante.
#     # De plus, on se souvient du chemin actuellement traversé et du poids associé
#     # En fait, on effectue une recherche en profondeur et on étudie la longueur du chemin s'il contient tous les nœuds.
#     def exhaustive(noeudsRestants, noeudActuel, cheminActuel, longueurActuelle, graph) :
        
#         # S'il reste des nœuds, nous effectuons une recherche en profondeur.
#         # Nous augmentons le chemin et sa longueur dans l'appel récursif.
#         # Évidemment, nous ne considérons que les nœuds qui sont accessibles.
#         if not noeudsRestants :
#             print("Chemin Hamiltonien trouvé", repr(cheminActuel), "de taille", longueurActuelle)
#             nonlocal meilleureLongueur, meilleurChemin
#             if longueurActuelle < meilleureLongueur :
#                 meilleureLongueur = longueurActuelle
#                 meilleurChemin = cheminActuel
        
#         # S'il reste des nœuds, nous effectuons une recherche en profondeur.
#         # Nous augmentons le chemin et sa longueur dans l'appel récursif.
#         # Évidemment, nous ne considérons que les nœuds qui sont accessibles.
#         else :
#             for neighbor, weight in graph[currentNode] :
#                 if neighbor in remainingNodes :
#                     otherNodes = [x for x in remainingNodes if x != neighbor]
#                     exhaustive(otherNodes, neighbor, currentPath + [neighbor], currentLength + weight, graph)
    
#     # We initiate the search from the source node
#     otherNodes = [x for x in range(len(graph)) if x != sourceNode]
#     exhaustive(otherNodes, sourceNode, [sourceNode], 0, graph)
    
#     # We return the result
#     return (bestPath, bestLength)

# ###################################################################
 
# # Test graph
# graph = [[(1, 1), (2, 7), (5, 3)], [(0, 1), (2, 1), (5, 1)], [(0, 7), (1, 1)], [(4, 2), (5, 2)], [(3, 2), (5, 5)], [(0, 3), (1, 1), (3, 2), (4, 5)]]
# (result, length) = travellingSalesman(graph, 0)
# print(repr(result))
# print(length)
if __name__ == "__main__":
    lt = 20
    ht = 20
    nb = 5
    gt = Graph.Graph(nb, lt, ht)

    print("graph =\n{}\n".format(gt))


    gt.calcul_matrice_cout_od()

    print("Matrice =\n{}\n".format(Graph.Graph.matrice_od))

    rt = Route(gt)

    print("route =\n{}\n".format(rt))
    print("distance = {}\n".format(rt.calcul_distance_route()))