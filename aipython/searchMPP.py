# searchMPP.py - Searcher with multiple-path pruning
# AIFCA Python3 code Version 0.7.1 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from aipython.searchGeneric import AStarSearcher, test
from aipython.searchProblem import Path
from aispace2.jupyter.search import visualize


class SearcherMPP(AStarSearcher):
    """returns a searcher for a problem.
    Paths can be found by repeatedly calling search().
    """

    def __init__(self, problem):
        super().__init__(problem)
        self.explored = set()

    @visualize
    def search(self):
        """returns next path from an element of problem's start nodes
        to a goal node.
        Returns None if no path exists.
        """
        self.display(2, "Ready")
        while not self.empty_frontier():
            path = self.frontier.pop()
            self.display(3, "Checking: ", path, "(cost: ", path.cost, ")")
            if path.end() not in self.explored:
                self.display(2, "Expanding: ", path, "(cost: ", path.cost, ")")
                self.explored.add(path.end())
                self.num_expanded += 1
                if self.problem.is_goal(path.end()):
                    # self.display(1, self.num_expanded, "paths have been expanded and", len(self.frontier), "paths remain in the frontier", "\nPath found: ", path)
                    self.display(1, "Solution found:", path, "(cost: ", path.cost, ")")
                    self.solution = path   # store the solution found
                else:
                    neighs = self.problem.neighbors(path.end())
                    self.display(3, "Neighbors are", neighs)
                    for arc in neighs:
                        self.add_to_frontier(Path(path, arc))
            else:
                self.display(3, "The end of this path (", path.end(), ") has already been explored, so prune it")
            self.display(3, "Frontier:", self.frontier)
        self.display(1, "No more solutions since the frontier is empty. Total of", self.num_expanded, "paths expanded")


if __name__ == "__main__":
    test(SearcherMPP)

# import aipython.searchProblem
# searcherMPPcdp = SearcherMPP(searchProblem.search_cyclic_delivery)
# print(searcherMPPcdp.search())  # find first path
