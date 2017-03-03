#include<stdio.h>
#include<windows.h>
#include<string.h>
#include<conio.h>
main()
{
    int i=0,ret;
    FILE *fp;
    char command[200],username[30],password[30],c,a[61],out[10];
    printf("Username: ");
    scanf("%s",username);
    getchar();
    printf("\nPassword: ");
    do
    {
        c = getchar();
        if(c!='\n' && i<30)
        {
            password[i] = c;
            i++;
        }
        else
            break;

    }while(c!='\n');
    password[i] = '\0';
    strcpy(a,username);
    strcat(a,"++");
    strcat(a,password);
    //printf("%s",a);
    strcpy(command, "echo ");
    strcat(command,a);
    strcat(command," | ncp 127.0.0.1 31337 ");
    fp = popen(command,"r");
    fgets(out,10,fp);
    if(!strcmp(out,"1"))
    {
        printf("Authenticated\n");
    }
    getchar();
    getchar();
    /*strcpy(command, username);
    strcat(command, "++");
    strcat(command, password);
    system(command);*/
    //printf("\nu:%s",command);
}
