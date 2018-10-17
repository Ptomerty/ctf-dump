#include <stdlib.h>
#include <stdio.h>

void get_flag()
{
	system("/bin/cat flag.txt");
}

void do_format()
{
	int user_inpt = 0;
	char buff[72];
	int secret = rand();
	printf("Enter your name: ");
	fgets(buff, 72, stdin);
	printf("Your name is: ");
	printf(buff);

	puts("\nEnter your secret password (in hex)");
	scanf("%x", &user_inpt);

	if (user_inpt == secret)
	{
		get_flag();
	}
}

int main(int argc, char** argv)
{
	gid_t gid = getegid();
	setresgid(gid,gid,gid);
	srand(time(0));
	do_format();
	return 0;
}

