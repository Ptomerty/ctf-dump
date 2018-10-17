    /* guess.c */
    #include<stdio.h>
    #include<time.h>
    #include<stdlib.h>

    int main(void)
    {
     int rand_num;
     srand(time(0)); //seed with current time
     rand_num = rand();
     printf("%x\n", rand_num);
     return 0;
    }
