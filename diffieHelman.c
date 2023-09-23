/* Solves a Diffie-Helman problem given the minimum necessary information.
Intended for use on small integers ONLY. 
compile with $ gcc diffieHelman.c -o diffieHelman.o
run with $ ./diffieHelman.o
*/

#include <stdio.h>

int p;
int q;
int remA;
int remB;

/* brute forces the power to which p was raised
checking the if result mod q equals the remainder.
returns suitable exponent.
WARNING will continue indefinitely
until a suitable exponent is found! */
int findExp(int remainder) {
    int exp = 0;
    int num;
    int next;
    while (exp == 0) {
        num++;
        next = p^num % q;
        if (next == remainder) {
            exp = num;
            break;
        }
    }
    return exp;
}

/* prompts user for variable input for use in calculation */
int main(int argc, char *args[]) {
    printf("enter p, q, A, B\n");
    scanf("%i %i %i %i", &p, &q, &remA, &remB);
    int a = findExp(remA);
    int b = findExp(remB);
    int k = a^b % p;
    printf("a: %i  b: %i  shared key: %i\n", a, b, k);
    return 0;
}