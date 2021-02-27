from solution import word_mesh
import codewars_test as test

@test.it("Basic tests")
def iloveyou():
    test.assert_equals(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")
    test.assert_equals(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")
    test.assert_equals(word_mesh(["abandon", "donation", "onion", "ongoing"]), "dononon")
    test.assert_equals(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]), "ownhippuscartpher")