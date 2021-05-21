from Graph import Graph

class TSP_BF:
    """Classe permettant de résoudre itérativement le problème du plus court circuit visitant tous les lieux et retournant au point de départ en utilisant un algorithme brute force."""

    def __init__(self, g):
        L = list(g.liste_lieux) + [g.liste_lieux[0]]
        print("L =", L)
        # t = len(g.liste_lieux)+1
        # print("t =", t)
        # i = [0] * t
        # print("i =", i)
        # while i[0] < t:
        #     print("i =", i)
        #     cb = []
        #     present = []
        #     for k in i:
        #         if k in present:
        #             present.append(k)
        #         else:
        #             j = -2
        #             i[- 1] += 1
        #             while i[j] >= t:
        #                 i[j] += 1
        #                 j -= 1
        #             continue
        #         cb.append(L[k])
        #     print(cb)

        #     j = -2
        #     i[-1] += 1
        #     while i[j] >= t:
        #         i[j] += 1
        #         j -= 1

if __name__ == "__main__":
    lt = 20
    ht = 20
    nb = 5
    gt = Graph(nb, lt, ht)

    print("graph =\n{}\n".format(gt))

    bt = TSP_BF(gt)