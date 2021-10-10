// gf8_mul(a, b) - a * b mod x^8+x^4+x^3+x+1

uint8_t gf8_mul(uint8_t a, uint8_t b)
{
    uint8_t r = 0;

    while(b > 0){
        if (b & 1) 
            r = r ^ a;
        b = b >> 1;
        a = ((a<<1) ^ ((a>>7) & 1 ? 0x1B : 0)); // xtime for a
    }
    return r;
}

// gf8_pow(a,b) - a^b mod x^8+x^4+x^3+x+1

uint8_t gf8_pow(uint8_t a, uint8_t b)
{
    uint8_t r = 1;

    while(b > 0){
        if(b&1)
        //multiplication should proceed with gf8_mul() [mod x^8+x^4+x^3+x+1]
            r = gf8_mul(r,a);
        b = b >> 1;
        a = gf8_mul(a,a);
    }
    return r;
}


 // gf8_inv(a) - a^-1 mod x^8+x^4+x^3+x+1

uint8_t gf8_inv(uint8_t a)
{
    return gf8_pow(a, 0xfe);
}