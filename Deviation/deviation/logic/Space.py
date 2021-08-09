
class Space:
    """  We use this to generate and process the set of all tuples whose
    corrdinates are less than an upper bound and above a lower bound:

    (a0, ..., aN)  such that
         ai >= self.origin[i]
         ai <= self.bounds

    N.B. the self.N is arbitrary
    """
    def __init__(self, bounds, point=None):
        self.N = len(bounds)
        assert self.N > 0
        self.bounds = bounds
        if point is not None:
            assert len(point) == self.N
            self.origin = point
        else:
            self.origin = [0] * self.N
        slist = list(self.tower(self.origin))
        slist.sort()
        self.search_space = tuple(slist)
        self.cardinality = len(self.search_space)
        self.current_position = -1


    def finished(self):
        return self.current_position + 1 == self.cardinality

    def nextElement(self):
        candidate = self.current_position + 1
        while candidate < self.cardinality:
            elem = self.search_space[candidate]
            self.current_position = candidate
            return elem
        return None

    def reset(self):
        self.current_position = -1


    # computes the set of all tuples above point.
    def tower(self, point=None):
        retval = set()
        if point is None:
            point = self.origin
        for i in range(point[0], self.bounds[0]):
            element = [None] * self.N
            element[0] = i
            retval.add(tuple(element))
        for i in range(1, self.N):
            old = retval
            retval = set()
            for elem in old:
                for j in range(point[i], self.bounds[i]):
                    nelem = list(elem)
                    nelem[i] = j
                    retval.add(tuple(nelem))
        return retval
