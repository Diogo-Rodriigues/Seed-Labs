# include <stdio.h>
# include <unistd.h>

int main(){
    printf("Malicious ls executed. ruid=%d euid=%d\n", getuid(), geteuid());
    return 0;
}