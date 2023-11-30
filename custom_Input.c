#include<stdio.h>
#include<stdlib.h>
int main(){
    int i=0;
    int j=9;
    int k=100;
    int l=-102;
    if(i>0){
        printf("Test Cases!");
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
}