#include<stdio.h>
#include<string.h>
void main(int argc, char* argv[])
{
    char *cmd;
    cmd = (char *)malloc(150*sizeof(char));
    if(argc>=2)
    {
        char *dst = argv[1];
        char *src = argv[2];
        printf("Dst: %s, Src: %s",dst,src);
        strcpy(cmd,"mklink /D ");
        strcat(cmd,dst);
        strcat(cmd," ");
        strcat(cmd,src);
        system(cmd);
    }
    getchar();
}
