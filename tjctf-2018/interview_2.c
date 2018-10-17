#include <stdio.h>
#include <stdlib.h>

int main() {
    int i = 0;
	srand(time(NULL)); 
   for (i = 0; i < 10; i++) {
        printf("%x\n", rand());
    }
    return 0;
}
