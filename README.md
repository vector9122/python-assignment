# python-assignment

Python program to make 3 letter abbreviation using any no. of words in the name. Rules to make these abbreviations
i) If a letter is the first letter of a word in the name then it has score 0.(ii) Otherwise, if a letter is the last letter of a word in the name then it has score 5,unless the letter is E, in which case the score is 20.(iii) If a letter is neither the first nor last letter of a word, then its score is the sum ofa position value, which is 1 for the second letter of a word, 2 for the third letterand 3 for any other position, plus a value based on how common/uncommonthis letter is in English: 1 for Q,Z, 3 for J,X, 6 for K, 7 for F,H,V,W,Y, 8 forB,C,M,P, 9 for D,G, 15 for L,N,R,S,T, 20 for O,U, 25 for A,I and 35 for E.
