import sat_interface

def tt1():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller

    return a list containing all entailed propositions or negated propositions
    '''
    print("Truth-tellers and liars I")
    print("-------------------------")
    ttprob = sat_interface.KB(["~A ~B",
                                "B A",
                                "~B ~C",
                                "C B",
                                "~C ~A",
                                "~C ~B",
                                "A B C"])

    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt2():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars II")
    ttprob = sat_interface.KB([
                                "~A C",
                                "~B ~C",
                                "C B",
                                "~C B ~A",
                                "C ~B",
                                "C A"])
    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def tt3():
    '''Propositions:
        A: Amy is a truth-teller
        B: Bob is a truth-teller
        C: Cal is a truth-teller
    '''
    print("Truth-tellers and liars III")
    ttprob = sat_interface.KB([
                                "A C",
                                "~A ~C",
                                "B A C",
                                "~B ~C",
                                "~B ~A",
                                "C ~B",
                                "~C B"])
    entailed = []
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Amy is a liar")
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Amy is a truth-teller")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bob is a liar")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bob is a truth-teller")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("Cal is a liar")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("Cal is a truth-teller")
    print("-------------------------")
    return entailed

def salt():
    '''Propositions:
        A: Caterpillar is telling the truth
        B: Bill the lizard is telling the truth
        C: the Cheshire Cat is telling the truth
        SA: Caterpillar stole the salt
        SB: Bill stole the salt
        SC: Cat stole the salt
    '''
    print("A salt and battery")
    ttprob = sat_interface.KB([ 
                                "A B C",
                                "~A ~B ~C",
                                
                                "~A SB",
                                "~A ~SA",
                                "~A ~SC",
                                "A ~SB",
                                "A SA SC",

                                "~B A",
                                "B ~A",
                                "~B SB",
                                "~B ~SA",
                                "~B ~SC",
                                "B ~SB",
                                "B SA SC",

                                "~C ~SC",
                                "~C SA SB",
                                "C SC",
                                "C ~SA",
                                "C ~SB"
                                ])    
    entailed = []
    if ttprob.test_literal("~A") == False:
        entailed.append('A')
        print("Caterpillar is telling the truth")
    if ttprob.test_literal("A") == False:
        entailed.append('~A')
        print("Caterpillar is lying")
    if ttprob.test_literal("~B") == False:
        entailed.append('B')
        print("Bill the lizard is telling the truth")
    if ttprob.test_literal("B") == False:
        entailed.append('~B')
        print("Bill the lizard is lying")
    if ttprob.test_literal("~C") == False:
        entailed.append('C')
        print("the Cheshire Cat is telling the truth")
    if ttprob.test_literal("C") == False:
        entailed.append('~C')
        print("the Cheshire Cat is lying")
    if ttprob.test_literal("~SA") == False:
        entailed.append('SA')
        print("Caterpillar stole the salt")
    if ttprob.test_literal("SA") == False:
        entailed.append('~SA')
        print("Caterpillar did not steal the salt")
    if ttprob.test_literal("~SB") == False:
        entailed.append('SB')
        print("Bill stole the salt")
    if ttprob.test_literal("SB") == False:
        entailed.append('~SB')
        print("Bill did not steal the salt")
    if ttprob.test_literal("~SC") == False:
        entailed.append('SC')
        print("Cat stole the salt")
    if ttprob.test_literal("SC") == False:
        entailed.append('~SC')
        print("Cat did not steal the salt")
    print("-------------------------")
    return entailed

def main():
    tt1()
    tt2()
    tt3()
    salt()

if __name__ == '__main__':
    main()
