import numpy as np


class EvolutionTrainer:


    def __init__(self, nn):
        # how many times to test ai in case it was just unlucky
        self.tests_per_ai = 3
        # number of ai per generation
        self.ai_per_generation = 1000
        # percent of top that are immune and will mutate but keep a copy of itself
        self.top_immunity = .01 #  best 1%
        # all of the entries are mutated to this amount except the bottom half
        self.cutoff = 0.5 # so generation has 1000 then top 500 are mutated and bottom
        # 500 are replaced
        # based on mutations this will result in a larger amount but they will be ordered
        # and then cut off afterwards
        self.mutatations = 2
        # note when mutations are done all of them are tested again before shaving
        # best nn has weights biases and avg score when tested
        self.bestnn = (0,0,0)

        self.currgen = 1
        self.nns = np.array()
        self.nn = nn # nn object that will be used to process nns
        #test


    # this will evaluate a generation
    # get the best nn
    # and then generate the next generation
    def evalGeneration(self):
        # if generation is 1 then we generate random for all and then test it
        # if generation is higher than 1 then we take cut off and mutate and add those
        # then we add the other cutoff amount as random
        # test all of these and give scores and then cut off
        # make sure to save best performer per gen
        # also remember even if an ai did well last gen it needs to perform just as well
        # in the next gen or it dies so retesting them is important
        if self.currgen == 1:
            for i in range(self.ai_per_generation):
                self.nn.randomize()
                self.nns.append((self.nn.getweights,self.nn.getbias))

