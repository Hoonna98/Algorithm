#include <stdint.h>
#include <stdio.h>

#define ALEN 12
#define PRIME 1
#define COMPOSITE 0

uint64_t mod_add(uint64_t a, uint64_t b, uint64_t m)
{
    a = a % m;
    b = b % m;

    if(a >= m-b) return a-(m-b);
    return a+b;
}
uint64_t mod_sub(uint64_t a, uint64_t b, uint64_t m)
{
    a = a % m;
    b = b % m;
    if(a>b) return a-b;
    return a + (m-b);
}
uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t m)
{
    uint64_t r = 0;
    while (b > 0) {
        if (b & 1)
            r = mod_add(r, a, m);
        b = b >> 1;
        a = mod_add(a, a, m);
    }
    return r;
}
uint64_t mod_pow(uint64_t a, uint64_t b, uint64_t m)
{
    uint64_t r = 1;
    while (b > 0) {
        if (b & 1)
            r = mod_mul(r, a, m);
        b = b >> 1;
        a = mod_mul(a, a, m);
    }
    return r;
}

/*
 * Miller-Rabin Primality Testing against small sets of bases
 *
 * if n < 2^64,
 * it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.
 *
 * if n < 3,317,044,064,679,887,385,961,981,
 * it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41.
 */
const uint64_t a[ALEN] = {2,3,5,7,11,13,17,19,23,29,31,37};

/*
 * miller_rabin() - Miller-Rabin Primality Test (deterministic version)
 *
 * n > 3, an odd integer to be tested for primality
 * It returns 1 if n is prime, 0 otherwise.
 */
int miller_rabin(uint64_t n)
{
	if (n == 2) return PRIME;
	if (n%2 == 0) return COMPOSITE;
	
    uint64_t q = n-1;
    int k = 0;
    int pass = 0;

    while(!(q & 1)){
        q = q >> 1;
        k += 1;
    }

    for(int i=0; i<ALEN; i++){
    	if(n <= a[i]) {
    		break;
    	}
        if(mod_pow(a[i],q,n) == 1) {
        	pass += 1;
        }
        else{
            for(int j=0; j<k; j++){
            if(mod_pow(mod_pow(a[i],q,n),mod_pow(2,j,n),n) == n-1) pass+=1;
            }
        }
        if(pass == 0) {
        	return COMPOSITE;
        }
        pass = 0;
    }
    return PRIME;
}
