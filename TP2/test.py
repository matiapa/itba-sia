from main.individual import Individual


class A:

    bar : str

    def __init__(self):
        self.bar = "Bar"
        self._foo()
  
    def _foo(self):
        raise NotImplementedError
             
class B(A):

    def _foo(self):
        print(self.bar)  

b = B()


# class BagIndividual(Individual):

#     @staticmethod
#     def genome_size() -> int:
#         return 100

#     def __initialize_genes(self):
#         for i in range(0,100):
#             self.genes[i] = 1 if random() > 0.5 else 0
