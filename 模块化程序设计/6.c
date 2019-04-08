#include<stdio.h>
int fun(int);
int fun(int n){
	static int p=1;
	p=p*n;
    return p;
}
int main(){
	int n,i;
	int f=1;
	printf("input member: ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		f=fun(i);
	printf("%d!=%d\n",n,f);
}
