# Birthday-Attack-
To find a collision where two arbitrary messages hash to the same first 40 bits using sha256 encryption


The Birthday Paradox states that from a set of independent identically disputed integers r1…  rn {1…B}, when n = 1.2 * B^½ the probability that i not equal j, ri is equal to rj. This algorithm can be used to find two different messages that hash to the same value. For the project by using the first 40 bits we are able to choose 2^40/2 messages. For each iteration up to 2^40/2 (i = 1.. 2^40/2) compute the hash function of a unique message, then compare it to the next hash function to see if it is equal. The probability of a collision will be 50%, so if there is no found collision repeat the steps. The expected number of times to run the code will be 2. 
