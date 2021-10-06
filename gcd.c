#include <stdio.h>
#include <stdlib.h>
/*
 * gcd() - Euclidean algorithm
 *
 * 유클리드 알고리즘 gcd(a,b) = gcd(b,a mod b)를 사용하여 최대공약수를 계산한다.
 * 만일 a가 0이면 b가 최대공약수가 된다. 그 반대도 마찬가지이다.
 * a, b가 모두 음이 아닌 정수라고 가정한다.
 * 재귀함수 호출을 사용하지 말고 while 루프를 사용하여 구현하는 것이 빠르고 좋다.
 */
int gcd(int a, int b)
{
    int tmp; //before computing B, save B temporarily
    while(b != 0){
        tmp = b;
        b = a % b;
        a = tmp;    
    }
    return a;
}

/*
 * xgcd() - Extended Euclidean algorithm
 *
 * 확장유클리드 알고리즘은 두 수의 최대공약수와 gcd(a,b) = ax + by 식을 만족하는
 * x와 y를 계산하는 알고리즘이다. 강의노트를 참조하여 구현한다.
 * a, b가 모두 음이 아닌 정수라고 가정한다.
 */
int xgcd(int a, int b, int *x, int *y)
{
    //initial value creation
    int d0 = a, d1 = b, x0 = 1, x1 = 0, y0 = 0, y1 = 1;
    int q = (d0/d1);
    int d = d0 - q*d1;
    while(d != 0){ // when d(k+1) = 0 
        //save the next x,y's value at the address of x,y
        *x = x0-q*x1; 
        *y = y0-q*y1;

        //next value for "x"
        x0 = x1;
        x1 = *x;
        //next value for "y"
        y0 = y1;
        y1 = *y; 
        //next value for "d, q"
        d0 = d1;
        d1 = d;
        q = (d0/d1);
        d = d0 - q*d1;
    }
    return d1; // d(k)

}

/*
 * mul_inv() - computes multiplicative inverse a^-1 mod m
 *
 * 모듈로 m에서 a의 곱의 역인 a^-1 mod m을 구한다.
 * 만일 역이 존재하지 않는다면 0을 리턴해야 한다.
 * 확장유클리드 알고리즘을 변형하면 구할 수 있다. 강의노트를 참조한다.
 */
int mul_inv(int a, int m)
{
    int d0 = a, d1 = m;
    int x0 = 1, x1 = 0, q;
    int temp; // temporature store for swapping two value
    while(d1>1){
        q = d0/d1;
        
        d0 = d0 - q*d1;
        //swap(d0, d1)
        temp = d1;
        d1 = d0;
        d0 = temp;
        
        x0 = x0 - q*x1;
        //swap(x0,x1)
        temp = x1;
        x1 = x0;
        x0 = temp;
    }
    if(d1 == 1)
        return (x1 > 0 ? x1 : x1+m); // replace positive number
    else
        return 0; 
}

/*
 * umul_inv() - computes multiplicative inverse a^-1 mod m
 *
 * 입력이 unsigned 64 비트 정수로 되어 있는 특수한 경우에
 * 모듈로 m에서 a의 곱의 역인 a^-1 mod m을 구한다.
 * 만일 역이 존재하지 않는다면 0을 리턴해야 한다.
 * 확장유클리드 알고리즘을 변형하면 구할 수 있다.
 * 입출력 모두가 unsigned 64 비트 정수임을 고려해서 구현한다.
 */
uint64_t umul_inv(uint64_t a, uint64_t m)
{
    uint64_t d0 = a, d1 = m;
    uint64_t x0 = 1, x1 = 0;
    uint64_t q, temp; // temporature store for swapping two value
    int nx = 1; // x1 is below 0
    int turn = 0, i = 0; 
    /* 
    turn은 x1이 0보다 작아진 순간부터 횟수를 나타낸다.
    i는 turn이 초기화가 잘 되었는지 확인하는 변수
    */
    
    while (d1 > 1) {
        q = d0/d1;

        // d는 0보다 작아지지 않아 unsigned와 int의 차이가 없다.
        temp = d0 - q*d1; d0 = d1; d1 = temp;

        if (nx==1)
        {
            if (x0 < q*x1){
                temp = q*x1 - x0;
                nx = 0;
                turn = 0; // turn count start
            }
            else{
                temp = x0 - q*x1;
                nx = 1;
            }
        }
        else{
            temp = x0 + q*x1; // 한번 음수가 되면 x0 에 q*x1을 계속 더해준다.
        }

        x0 = x1; x1 = temp;
        turn++; i++; 
    }
    
    if (d1 == 1)
        // turn이 홀수이면 마지막 x1의 값은 0보다 작은 값을 가지기에 m에서 빼주어야하고
        // turn이 짝수이면 양수이기에 그냥 x1을 리턴한다.
        if (turn % 2 == 1 & turn != i) return m-x1;
        else return x1;
    else
        return 0;
}
