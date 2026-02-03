# include <stdio.h>
# include <unistd.h>

int main(){
    printf("UIDs: real=%d effective=%d\n", getuid(), geteuid());
    sleep(1);
    return 0;
}