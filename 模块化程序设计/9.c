#include<stdio.h>
int flower(int);
int flower(int n){
    if((n/100)*(n/100)*(n/100)+(n/10%10)*(n/10%10)*(n/10%10)+(n%10)*(n%10)*(n%10)==n)
		return 1;
	else
		return 0;
	
}
int main(){
	int x;
	scanf("%d",&x);
	printf("%d",flower(x));
}