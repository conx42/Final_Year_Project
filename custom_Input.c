#include<stdio.h>
#include<stdlib.h>
int main(){
    int i=0;
    int j=9;
    int k=100;
    int l=-102;
    int x=99;
    int y=11, w=0,p=78,z=1,a=0;
    if(i>0){
        printf("Test Cases!");
        if(x>99){
            if(y<100){
                printf("print");
            }
        }
    }
    else{
        exit(0);
    }

    if(j>0){
        if(k>100){
            if(l>1){
                printf("Taking Nested Loop!");
            }
        }
    }

    if(w>0){
        printf("Test");
        if(p>0){
            printf("Test");
            if(z<0){
                if(a>10){
                    exit(0);
                }
            }
        }
    }
}