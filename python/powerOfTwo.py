# 2^7=128 is the first power of two whose leading digits are "12".
# The next power of two whose leading digits are "12" is 2^80

# Define p(L,n)
# to be the nth-smallest value of j such that the base 10 representation of 2^j begins with the digits of L.
# So p(12,1)=7 and p(12,2)=80

# You are also given that p(123,45)=12710

# Find p(123,678910)

from time import time


def powerOfTwo(searching, nth):

    searching = str(searching)
    exp = 0
    
    i = 0
    while ( True ):
        i += 1
        num = 2**i
        if ( searching == str(num)[:len(searching)] ):
            exp += 1
            print(f'{exp=} a los { round( (time() - start) , 3) }')

            if ( exp == nth ):
                return i

if __name__ == '__main__':

    start = time()

    print(f'El exponete buscado es: { powerOfTwo(123,678910) } \nEl calculo se realizo en { round( (time() - start) , 3) }')
