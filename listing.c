#include<stdio.h>
#include<windows.h>
#include<string.h>
main()
{
    int i=0;
    FILE *fp;

    //fp = popen("ncp -v -l -p 4444","r"); //This returns the output to the stream
    char command[150],*out[500];
   // strcpy(command, "ncp -v -l -p 4444 > stdout");
    //system(command);
    strcpy(command,"dir /b | ");
    strcat(command, "ncp 127.0.0.1 6666");
    fp = popen(command,"r");
    fgets(out,10,fp);
    pclose(fp);
}

