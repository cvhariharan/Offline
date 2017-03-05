#include<stdio.h>
#include<windows.h>
#include<string.h>
#include<conio.h>
main()
{
    int i=0,ret,auth=0;
    FILE *fp;
    char command[200],username[30],password[30],c,a[61],out[10];
    while(auth==0)
    {
    printf("Username: ");
    scanf("%s",username);
    getchar();
    printf("Password: ");
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
        auth=1;
        break;
    }
    else if(!strcmp(out,"0"))
    {
        printf("Could not authenticate!\n");
    }
    strcpy(out,"");
    i=0;
    }
    if(auth==1)
    {
        system("listing jabssfkueg54af");
        printf("Files listed.\n");
    }
    getchar();
    /*strcpy(command, username);
    strcat(command, "++");
    strcat(command, password);
    system(command);*/
    //printf("\nu:%s",command);
}
