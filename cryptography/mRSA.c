#include <stdlib.h>
#include "mRSA.h"

const uint64_t a[ALEN] = {2,3,5,7,11,13,17,19,23,29,31,37};

static uint64_t gcd(uint64_t a, uint64_t b){
    uint64_t temp;
    //최대 공약수 : a%b == 0인 지점의 b
    while(!(a%b==0)){
        temp = b;
        b = a % b;
        a = temp;
    }
    return b;
}

static uint64_t mul_inv(uint64_t a, uint64_t m){
    uint64_t d0 = a, d1 = m;
    uint64_t x0 = 1, x1 = 0;
    uint64_t q, temp; // temporature store for swapping two value
    int8_t sign = -1; // signed의 과정에서 보았을 때 음수인 경우
    
    while (d1 > 1) {
        q = d0 / d1;
        temp = d0 - q*d1; d0 = d1; d1= temp;
        temp = x0 + q*x1; x0 = x1; x1= temp; 
        // (-)-(+) : 절대값을 더하는 것과 같고
        // (+)-(-) : 절대값을 더하는 것과 같다.
        // --> +만 진행해도 무방하다.
        sign = ~sign;
    }
    
    if (d1 == 1)
        return (sign ? m-x1 : x1);
    else
        return 0;
}

static uint64_t mod_add(uint64_t a, uint64_t b, uint64_t m){
    a = a % m;
    b = b % m;

    if(a >= m-b) return a-(m-b);
    return a+b;
}

static uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t m){
    uint64_t r = 0;
    while (b > 0) {
        if (b & 1)
            r = mod_add(r, a, m);
        b = b >> 1;
        a = mod_add(a, a, m);
    }
    return r;
}

static uint64_t mod_pow(uint64_t a, uint64_t b, uint64_t m){
    uint64_t r = 1;
    while (b > 0) {
        if (b & 1)
            r = mod_mul(r, a, m);
        b = b >> 1;
        a = mod_mul(a, a, m);
    }
    return r;
}

static int miller_rabin(uint64_t n){
	if (n == 2) return PRIME;
	if (n%2 == 0) return COMPOSITE;
	
    uint64_t q = n-1;
    int k = 0;
    int pass = 0;

    while(!(q & 1)){
        q = q >> 1;
        k += 1;
    }

    for(int i=0; i<12; i++){
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

static uint64_t mul(uint64_t a, uint64_t b){
    uint64_t n = 0;
    while (b > 0) {
        if (b & 1)
            n = n+a;
        b = b >> 1;
        a = a+a;
    }
    return n;
}
/*
 * mRSA_generate_key() - generates mini RSA keys e, d and n
 * Carmichael's totient function Lambda(n) is used.
 */
void mRSA_generate_key(uint64_t *e, uint64_t *d, uint64_t *n)
{
    uint64_t p,q;
    uint64_t lambdaN;
    
    while(1){
        //random 한 소수 찾기
        do{ 
            p = arc4random();
        }while(!miller_rabin(p));
        do{
            q = arc4random();
        }while(!miller_rabin(q));

        //n의 값을 만족하는 p, q를 계속해서 찾음
        *n = mul(p,q);
        if(*n > MINIMUM_N) break;        
    }
    lambdaN = mul(p-1,q-1)/gcd(p-1,q-1);
    
    while(1){
        //조건을 만족하는 PU key {e, n} 생성
        arc4random_buf(e, sizeof(uint64_t));
        if(gcd(*e,lambdaN)==1 && *e < lambdaN)
            break;
    }
    *d = mul_inv(*e, lambdaN);
}


/*
 * mRSA_cipher() - compute m^k mod n
 * If data >= n then returns 1 (error), otherwise 0 (success).
 */
int mRSA_cipher(uint64_t *m, uint64_t k, uint64_t n)
{
    if(*m >= n) return 1;
    *m = mod_pow(*m,k,n);
    return 0;
}