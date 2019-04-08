#include<stdio.h>
int sum1(int);
int factorial(int);
int factorial(int x){
	int s=1,i;
	for(i=1;i<=x;i++){
	s=s*i;}
	return s;
}
int sum1(int n){
	int s=0,i,j;
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			s=s+factorial(j);
		}
	}
	return s;
}
int main(){
	int n;
	scanf("%d",&n);
	printf("%d",sum1(n));
}