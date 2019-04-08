#include<stdio.h>
int power(int,int);
int power(int y,int n){
	int i ,p=1;
	for(i=1;i<=n;i++) p=p*y;
    return p;
}
int main(){
	
	int x,n,s;
	scanf("%d %d",&x,&n);
	s=power(x,n);
	printf("%d",s);
}