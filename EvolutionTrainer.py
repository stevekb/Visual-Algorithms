import numpy as np
from SnakeGame import SnakeGame
from neuralnet import NeuralNet

class EvolutionTrainer:


#tester is how to score nn's
    def __init__(self, nn, tester):
        # how many times to test ai in case it was just unlucky
        self.tests_per_ai = 5
        # number of ai per generation
        self.ai_per_generation = 100
        # percent of top that are immune and will mutate but keep a copy of itself
        self.top_immunity = .01 #  best 10%
        # all of the entries are mutated to this amount except the bottom half
        self.cutoff = 0.1 # so generation has 1000 then top 500 are mutated and bottom
        # 500 are replaced
        # based on mutations this will result in a larger amount but they will be ordered
        # and then cut off afterwards
        self.mutatations = 5
        # note when mutations are done all of them are tested again before shaving
        # best nn has weights biases and avg score when tested
        self.bestnn = [] # will fill with w and b and score of each generation's best
        self.bestscore = 0
        self.currgen = 1
        self.nns = []
        self.nn = nn # nn object that will be used to process nns
        self.tester = tester # this is the class object that will test the nn
        #test
        self.shape = nn.getshape()
        self.w_shapes = list(zip(self.shape[1:], self.shape[:-1]))


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
        rank = []
        if self.currgen == 1:
            for i in range(self.ai_per_generation):
                self.nns.append((self.create()))

        else: # otherwise we wanna evolve
            newnns = []
            for i in range(self.ai_per_generation):
                if(i < self.ai_per_generation * self.cutoff):
                    if(i < self.ai_per_generation * self.top_immunity):
                        newnns.append(self.nns[i])
                        for j in range(self.mutatations - 1):
                            newnns.append(self.mutate(self.nns[i],0.5))
                    else:
                        for j in range(self.mutatations):
                            newnns.append(self.mutate(self.nns[i],0.5))
                else: # rest after cutoff add in as random
                    newnns.append(self.create())

            self.nns = newnns

        #  after anything is made we test
        #  then reorder based on results and then
        #  then cutoff to ai_per_gen
        scores = []
        for n in range(len(self.nns)):
            avgscore = 0
            #set our nn to have the weights and biases we want
            self.nn.setvalues(self.nns[n][0],self.nns[n][1])
            for i in range(self.tests_per_ai):
                avgscore += self.tester.getscore(self.nn)
                # print(avgscore)
            avgscore /= self.tests_per_ai
            scores.append(avgscore)

        #now we have all the scores so now we want to order the results

        self.nns = [x for _, x in sorted(zip(scores, self.nns), reverse=True, key=lambda pair: pair[0])]

        #finally we only add some
        self.nns = self.nns[:self.ai_per_generation]

        # print(len(self.nns))
        print("gen: " +str(self.currgen) + " best: " + str(max(scores)))
        self.currgen += 1


    #takes in weights and bias pair and mutates a bit
    def mutate(self,wb, mutate_amount):
        w, b = wb
        for i in range(len(w)):
            for j in range(len(w[i])):
                for k in range(len(w[i][j])):
                    w[i][j][k] += + np.random.standard_normal() * mutate_amount

        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] + np.random.standard_normal()* mutate_amount
        return w, b

    def create(self):
        w = [np.random.standard_normal(s) / s[1] ** .5 for s in self.w_shapes]
        b = [np.array([np.random.standard_normal(s) / s ** .5]).T for s in self.shape[1:]]
        return w, b



