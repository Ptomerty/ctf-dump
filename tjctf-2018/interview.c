#include <stdio.h>
#include <stdlib.h>

#define FLAG "-----REDACTED-----"

void interview(int secret) {

    int i, j;
    int canary[10];
    char name[64];
    int check[10];

    for (i = 0; i < 10; ++i) {
        canary[i] = check[i] = rand();
    }

    printf("Welcome to the Future Canary Lab!\n");
    printf("What is your name?\n");
    gets(name);

    for (j = 0; j < 10; ++j) {
        if (canary[j] != check[j]) {
            printf("Alas, it would appear you lack the time travel powers we desire.\n");
            exit(0);
        }
    }

    if (secret - i + j == 0xdeadbeef) {
        printf("You are the one. This must be the choice of Stacks Gate!\n");
        printf("Here is your flag: %s\n", FLAG);
    } else {
        printf("Begone, FBI Spy!\n");
    }

    exit(0);
}

int main() {

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    setbuf(stdout, NULL);

    srand(time(NULL));

    interview(0);

    return 0;
}