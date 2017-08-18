#include<stdio.h>
#include<string.h>
void main(int argc, char* argv[])
{
    char *cmd;
    cmd = (char *)malloc(100*sizeof(char));
    if(argc>=3)
    {
        strcpy(cmd,"Server-win.exe --username ");
        strcat(cmd, argv[1]);
        strcat(cmd, " --password ");
        strcat(cmd, argv[2]);
        strcat(cmd , " -p ");
        strcat(cmd, argv[3]);
        //strcat(cmd, " > Server.log");
        //printf("%s",cmd);
    }

    while(1)
    {
        system(cmd);
    }
}
