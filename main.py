# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:12:01 2019

@author: japesh
"""

from automataTheory import *
import sys
import time

def main():
    inp = "(01*1)*1"
    if len(sys.argv)>1:
        inp = sys.argv[1]
    print ("Regular Expression: ", inp)
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()
    print ("\nNFA: ")
    nfaObj.displayNFA()
    
    
    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()
    minDFA = dfaObj.getMinimisedDFA()
    print ("\nDFA: ")
    dfaObj.displayDFA()
    print ("\nMinimised DFA: ")
    dfaObj.displayMinimisedDFA()

if __name__  ==  '__main__':
    t = time.time()
    try:
        main()
    except BaseException as e:
        print ("\nFailure:", e)
    print ("\nExecution time: ", time.time() - t, "seconds")
