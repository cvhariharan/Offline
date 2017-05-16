#include<stdio.h>
#include<windows.h>
#include<string.h>
#include<stdlib.h>
#include <unistd.h>
#include<time.h>
#include<dos.h>
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}
main()
{
    int i=0;


    while(1)
    {
        FILE *fp;
        char command[150],out[500];
   // strcpy(command, "ncp -v -l -p 4444 > stdout");
    //system(command);

    strcpy(command,"dir /b | ");
    strcat(command, "ncp 127.0.0.1 6666");
    fp = popen(command,"r");
    printf("%d\n",i);
    fclose(fp);

    i++;
    Sleep(1000);
}

}

