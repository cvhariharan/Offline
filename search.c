#include<stdio.h>
#include<string.h>
main(int argc, char *argv[])
{
    FILE *fp;
    if(argc > 2)
    {
    int i,j,n;
    char command[150],out[200],ip[25],filename[200];
   // strcpy(command, "ncp -v -l -p 4444 > stdout");
    //system(command);
    strcpy(ip,argv[2]);
    strcpy(filename,argv[3]);
    strcpy(command,"ncp ");
    strcat(command, ip);
    strcat(command, " ");
    strcat(command, "4133 < ");
    strcat(command, filename);
    fp = popen(command,"r");
    fgets(out,10,fp);
    pclose(fp);
    }
}
