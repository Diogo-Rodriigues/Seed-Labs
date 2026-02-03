#include <stdio.h>

void main(){
	char* shell = getenv("MYSHELL");
	if (shell)
		printf("%x\n", (unsigned int)shell);
	char* flag = getenv("MYFLAG");
	if (flag)
		printf("%x\n", (unsigned int)flag);
	return 0;
}