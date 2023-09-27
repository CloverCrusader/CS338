/* Script to find secret key d from e and N
given that d < 1000000.
compile with $ gcc findD.c -o findD.o
run with $ ./findD.o */

#include <stdio.h>

int main(int argc, char *args[]) {
    int e;
    int phiN;
    printf("Enter: e, PHI(N)\n");
    scanf("%i, %i", &e, &phiN);
    int i = 1;
    while (i <= 1000000) {
        if ((e * i) % phiN == 1) {
            printf("d: %i\n", i);
            return 0;
        }
        i++;
    }
    printf("Abort: d is over one million.");
    return 1;
}